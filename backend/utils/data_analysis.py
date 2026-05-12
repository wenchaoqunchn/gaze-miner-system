import csv
import json
from typing import List, Tuple  # 导入 csv 模块，用于处理 CSV 文件
import numpy as np  # 导入 NumPy 模块，进行数组操作和数值计算
from .session_tools import View
from lib import detectors
from lib import gazeplotter as gp


class DataAnalyzer:
    def __init__(self, resolution, fix_threshold=None, sac_threshold=None):
        self.resolution = resolution
        self.f_thresh = (
            fix_threshold
            if fix_threshold is not None
            else {"maxdist": 25, "mindur": 50}
        )
        self.s_thresh = (
            sac_threshold
            if sac_threshold is not None
            else {"minlen": 5, "maxvel": 40, "maxacc": 340}
        )
        self.fixlist = []
        self.saclist = []
        self.xlist = []
        self.ylist = []
        self.nodata = False

    def extract(self, view: View):
        """
        分析给定路径的眼动追踪数据文件，提取注视和扫视信息。

        参数:
        filepath (str): CSV 文件的路径
        maxdist (float): 眼动点之间的最大距离，用于确定注视
        mindur (float): 最小注视持续时间
        minlen (float): 最小扫视长度
        maxvel (float): 最大扫视速度
        maxacc (float): 最大扫视加速度

        返回:
        tuple: 包含注视列表、扫视列表、X坐标列表和Y坐标列表
        """
        filepath = view.path["split"]
        maxdist = self.f_thresh["maxdist"]
        mindur = self.f_thresh["mindur"]
        minlen = self.s_thresh["minlen"]
        maxvel = self.s_thresh["maxvel"]
        maxacc = self.s_thresh["maxacc"]

        with open(filepath, "r") as file:  # 打开指定路径的 CSV 文件
            reader = csv.reader(file)  # 创建 CSV 读取器
            next(reader)  # 跳过 CSV 文件的表头
            data = list(reader)  # 将剩余数据读入列表中
        if data:
            self.nodata = False
            data_array = np.array(data)  # 将数据转换为 NumPy 数组

            # 将时间、X 坐标和 Y 坐标从数据数组中提取并转换为浮点数
            tlist = data_array[:, 0].astype(float)  # 提取时间列表
            xlist = data_array[:, 1].astype(float)  # 提取 X 坐标列表
            ylist = data_array[:, 2].astype(float)  # 提取 Y 坐标列表

            # 获取注视列表和扫视列表，仅使用第三方开源函数的第二个返回值
            _, fixlist = detectors.fixation_detection(
                xlist, ylist, tlist, maxdist, mindur
            )  # 调用函数获取注视信息
            _, saclist = detectors.saccade_detection(
                xlist, ylist, tlist, minlen, maxvel, maxacc
            )  # 调用函数获取扫视信息

            # 返回注视列表、扫视列表、X坐标列表和Y坐标列表
            self.fixlist = fixlist
            self.saclist = saclist
            self.xlist = xlist
            self.ylist = ylist
            print("Finish calculating.")
        else:
            self.nodata = True
            print("No data to be extracted.")

    def draw(self, view: View):
        if not self.nodata:
            res = self.resolution

            ori = view.path["origin"]
            fix = view.path["fixation"]
            raw = view.path["rawpoint"]
            scan = view.path["scanpath"]
            heat = view.path["heatmap"]

            fixl = self.fixlist
            sacl = self.saclist
            xl = self.xlist
            yl = self.ylist

            gp.draw_fixations(fixl, res, ori, fix)
            gp.draw_heatmap(fixl, res, ori, heat)
            gp.draw_raw(xl, yl, res, ori, raw)
            gp.draw_scanpath(fixl, sacl, res, ori, 0.5, scan)
            print("Finish drawing.")
        else:
            print("No data to be drawn.")

    def calculate(self, view: View):
        self.load_aoi_data("data/AOI.json", view.name)
        self.assign_aoi_to_fixations(self.fixlist)
        self.assign_aoi_to_saccades(self.saclist)
        m = self.calculate_metrics(self.fixlist, self.saclist, self.aoi_path)

        print(m)

    def load_aoi_data(self, aoi_json_path, view_name):
        with open(aoi_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        view_aoi = data.get(view_name)
        self.aoi_list = view_aoi.get("AOIs")
        self.aoi_path = view_aoi.get("path")

    def assign_aoi_to_fixations(self, Efix):
        for fixation in Efix:
            endx, endy = fixation[3], fixation[4]
            for aoi in self.aoi_list:
                pos = aoi["pos"]
                if (pos["x1"] <= endx <= pos["x2"]) and (
                    pos["y1"] <= endy <= pos["y2"]
                ):
                    fixation.append(aoi["id"])  # 将 AOI ID 添加到注视中
                    break

    def assign_aoi_to_saccades(self, Esac):
        for saccade in Esac:
            startx, starty = saccade[3], saccade[4]
            endx, endy = saccade[5], saccade[6]

            start_aoi, end_aoi = None, None
            for aoi in self.aoi_list:
                pos = aoi["pos"]
                if (pos["x1"] <= startx <= pos["x2"]) and (
                    pos["y1"] <= starty <= pos["y2"]
                ):
                    start_aoi = aoi["id"]
                if (pos["x1"] <= endx <= pos["x2"]) and (
                    pos["y1"] <= endy <= pos["y2"]
                ):
                    end_aoi = aoi["id"]

            saccade.append(start_aoi)  # 添加起始 AOI ID
            saccade.append(end_aoi)  # 添加结束 AOI ID

    def calculate_metrics(self, Efix, Esac, task_aoi_sequence):
        metrics = {}

        # 计算注视指标
        for aoi in task_aoi_sequence:
            aoi_fixations = [f for f in Efix if f[-1] == aoi]  # 根据 AOI 过滤注视

            metrics[aoi] = {
                "fixation_count": len(aoi_fixations),
                "total_fixation_duration": sum(f[2] for f in aoi_fixations),  # 累加时长
                "mean_fixation_duration": (
                    (sum(f[2] for f in aoi_fixations) / len(aoi_fixations))
                    if aoi_fixations
                    else 0
                ),
            }

        # 计算扫视指标
        for aoi in task_aoi_sequence:
            aoi_saccades = [s for s in Esac if s[-2] == aoi]  # 结束 AOI 过滤扫视

            metrics.setdefault(aoi, {}).update(
                {
                    "saccade_count": len(aoi_saccades),
                    "total_saccade_duration": sum(
                        s[2] for s in aoi_saccades
                    ),  # 累加时长
                }
            )

        return metrics
