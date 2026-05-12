import csv
import re
import time
from os import makedirs, listdir
from os.path import join, exists, isdir
from typing import Dict, List, Tuple
import win32gui, win32ui, win32con, win32print
import pandas as pd
from pathlib import Path
from app.config import Config


class Helper:
    # @staticmethod
    # def split(raw_path: Path, split_path: Path, save_dir: Path) -> int:
    #     raw_df = pd.read_csv(raw_path)
    #     split_series = pd.read_csv(split_path)["time"]
    #     split_cnt = len(split_series)
    #     start_index = 0

    #     for i in range(split_cnt):
    #         print(f"Split data segment {i+1}.")
    #         if i < split_cnt:
    #             end_index = raw_df[raw_df["time"] >= split_series[i]].index[0]
    #         else:
    #             end_index = raw_df.index[-1] + 1

    #         sub_df = raw_df.iloc[start_index:end_index]

    #         # 保存为 CSV 文件
    #         split_path = save_paths[i]
    #         sub_df.to_csv(split_path, index=False)

    #         # 更新起始索引
    #         start_index = end_index
    #     print("Split finished.")
    #     return split_cnt
    @staticmethod
    def split(raw_path, view_path, save_dir):
        raw_df = pd.read_csv(raw_path)
        # 读取 view_path 的 CSV 文件
        view_df = pd.read_csv(view_path)
        print(view_path)
        print(view_df)
        print("Columns in view_df:", view_df.columns.tolist())
        # 提取名为 'time' 的列作为 series
        split_series = view_df["time"]

        # 初始化指针
        raw_index = 0
        split_index = 0
        slice_number = 1

        while split_index < len(split_series):
            # 当前切片时间节点
            current_split_time = split_series.iloc[split_index]
            slice_data = []

            # 遍历原始数据
            while (
                raw_index < len(raw_df)
                and raw_df["time"].iloc[raw_index] < current_split_time
            ):
                slice_data.append(raw_df.iloc[raw_index])
                raw_index += 1

            # 如果有数据，保存到切片文件
            if slice_data:
                slice_df = pd.DataFrame(slice_data)
                output_file = save_dir / f"split_data_{slice_number:02}.csv"
                slice_df.to_csv(output_file, index=False)
                print(f"Saved slice {slice_number} to {output_file}")
            else:
                empty_df = pd.DataFrame(columns=raw_df.columns)
                output_file = save_dir / f"split_data_{slice_number:02}.csv"
                empty_df.to_csv(output_file, index=False)
                print(f"Saved empty slice {slice_number} to {output_file}")

            slice_number += 1

            # 移动切片节点指针
            split_index += 1

        # if raw_index < len(raw_df):
        #     slice_data = raw_df.iloc[raw_index:]
        #     if not slice_data.empty:
        #         output_file = save_dir / f"split_data_{slice_number:02}.csv"
        #         slice_df = pd.DataFrame(slice_data)
        #         print(
        #             f"Columns in remaining data: {slice_df.columns.tolist()}"
        #         )  # 打印列名
        #         slice_df.to_csv(output_file, index=False)
        #         print(f"Saved remaining data to {output_file}")

        print("Splitting complete.")

    @staticmethod
    def get_resolution() -> Tuple[int, int]:
        hDC = win32gui.GetDC(0)
        # 横向分辨率
        w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
        # 纵向分辨率
        h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
        return (w, h)

    @staticmethod
    def get_max_index(parent_dir: Path) -> int:
        # 获取指定目录下的所有文件夹
        items = listdir(parent_dir)

        # 定义正则表达式，用于匹配 session 文件夹名
        session_pattern = re.compile(r"session_(\d{2})", re.IGNORECASE)
        max_number = 0

        # 遍历文件夹名，查找最大 session 序号
        for item in items:
            if isdir(join(parent_dir, item)):
                match = session_pattern.search(item)
                if match:
                    session_number = int(match.group(1))
                    max_number = max(max_number, session_number)

        return max_number

    @staticmethod
    def save_screenshot(save_path_str: str, resolution: Tuple[int, int]) -> None:
        import cv2
        import numpy as np

        hwnd = 0
        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()
        w, h = resolution
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)

        # 获取 Bitmap 的像素信息
        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)

        # 转换为 numpy 数组 (注意：win32ui 取出来的图像是 BGRA 格式)
        img = np.frombuffer(bmpstr, dtype=np.uint8).reshape(
            (bmpinfo["bmHeight"], bmpinfo["bmWidth"], 4)
        )

        # 去除 Alpha 通道，保留 BGR，以减小体积，且适用于普通图片
        img_bgr = img[:, :, :3]

        # 如果后缀名为 .jpg，则使用较高压缩比 (可调节质量参数如 85)
        # 如果后缀名为 .png，则依然可以使用 cv2 保存，并可通过 IMWRITE_PNG_COMPRESSION 调整压缩级别
        if save_path_str.lower().endswith(".jpg") or save_path_str.lower().endswith(
            ".jpeg"
        ):
            cv2.imencode(".jpg", img_bgr, [int(cv2.IMWRITE_JPEG_QUALITY), 80])[
                1
            ].tofile(save_path_str)
        else:
            cv2.imencode(".png", img_bgr, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])[
                1
            ].tofile(save_path_str)

        # 释放资源释放
        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwndDC)

    # @staticmethod
    # def update_split_time(save_path: Path) -> None:
    #     # 数据切片时间戳文件
    #     with open(save_path, mode="a") as file:
    #         file.write(f"{int(time.time() * 1000)}\n")

    @staticmethod
    def update_view_sequence(save_path: Path, current_page: str) -> None:
        with open(save_path, mode="a") as file:
            file.write(f"{current_page},{int(time.time() * 1000)}\n")

    @staticmethod
    def check_img_cnt(folder_path: Path) -> int:
        pattern = re.compile(r"origin_(\d{2})\.jpg")  # 正则表达式匹配 origin_xx.jpg
        file_count = 0
        max_number = 0

        for filename in listdir(folder_path):
            match = pattern.match(filename)
            if match:
                # 提取序号并转换为整数
                number = int(match.group(1))
                file_count += 1
                max_number = max(max_number, number)

        # 检查是否连续
        if file_count != max_number:
            return -1

        return file_count


class Session:
    def __init__(self, parent_dir: Path, index: int, new_session: bool):
        self.parent_dir = Path(parent_dir)
        self.index = index
        self.session_dir = self.parent_dir / f"session_{index:02}"

        self.dir = {}
        self.path = {}
        self.pre = {}

        self.concat_path()

        if new_session:
            self.create_files()

    def concat_path(self):
        """构建各种路径"""
        self.dir["session"] = self.session_dir
        self.dir["img"] = self.session_dir / "img"
        self.dir["split"] = self.session_dir / "split_data"

        self.path["raw"] = self.session_dir / "raw_data.csv"
        # self.path["split"] = self.session_dir / "split_time.csv"
        self.path["view"] = self.session_dir / "view_switch.csv"

        for img_type in SessionManager.IMG_TYPES:
            self.pre[img_type] = str(self.dir["img"] / f"{img_type}_")

        self.pre["split"] = str(self.dir["split"] / "split_data_")

    def create_files(self):
        """创建必要的文件和文件夹"""
        self.session_dir.mkdir()
        self.dir["img"].mkdir()
        self.dir["split"].mkdir()

        with open(self.path["raw"], "w") as f:
            f.write("time,x,y\n")

        # with open(self.path["split"], "w") as f:
        #     f.write("view,time\n")  # 写入表头

        with open(self.path["view"], "w") as f:
            f.write("view,time\n")  # 写入表头


class View:

    def __init__(self, index: int, name: str, prefix: Dict[str, str]):
        self.index = index
        self.name = name
        self.path = {}
        """为每种图像和切片生成路径"""
        for t in SessionManager.IMG_TYPES:
            self.path[t] = Path(prefix[t] + f"{self.index:02}.jpg")
        self.path["split"] = Path(prefix["split"] + f"{self.index:02}.csv")


class SessionManager:
    IMG_TYPES = ("origin", "fixation", "rawpoint", "scanpath", "heatmap")
    RESOLUTION = Helper.get_resolution()
    # RESOLUTION = Config.RESOLUTION
    # VIEWS = [
    #     "News",
    #     "Agenda",
    #     "More",
    #     "Library",
    #     "More2",
    #     "SelectSpace",
    #     "SelectDateEaseOfUse",
    #     "Confirm",
    #     "SelectSeatDeviceEfficiency",
    # ]

    def __init__(self, parent_dir=Path("data")):
        self.parent_dir = parent_dir
        self.session = None
        self.focus_session = 0
        self.new_session = True
        self.view_list = []
        self.switch_cnt = 0

    def init_session(self, focus_session=0):

        self.focus_session = focus_session
        self.new_session = self.focus_session == 0
        self.view_list = []
        self.switch_cnt = 0
        p_dir = self.parent_dir
        max_index = Helper.get_max_index(p_dir)
        if self.new_session:
            if not exists(p_dir):
                makedirs(p_dir)
            s_index = max_index + 1
            self.session = Session(p_dir, s_index, self.new_session)
        else:
            if not exists(p_dir):
                raise FileNotFoundError(f"Folder {p_dir} not found.")
            elif focus_session < 1 or focus_session > max_index:
                raise FileNotFoundError(f"session_{focus_session:02} not found.")

            s_index = self.focus_session
            self.session = Session(p_dir, s_index, self.new_session)

            with open(self.session.path["view"], mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                # 跳过表头
                next(reader)

                # 将内容存储到数组
                view_name = [row[0] for row in reader]  # row[0] 取每一行的第一个元素

            view_num_1 = len(pd.read_csv(self.session.path["view"]))
            view_num_2 = Helper.check_img_cnt(self.session.dir["img"])
            if view_num_1 == view_num_2:
                for i in range(view_num_1):
                    self.view_list.append(View(i + 1, view_name[i], self.session.pre))
            else:
                raise RuntimeError("Broken files.")

    def switch_view(self, current_page: str):
        if self.session is None:
            raise RuntimeError("Session not initialized.")
        elif not self.new_session:
            raise RuntimeError("Switching unavailable in focus session mode.")
        else:
            self.switch_cnt += 1
            index = self.switch_cnt
            img_type = SessionManager.IMG_TYPES[0]
            origin_path = Path(self.session.pre[img_type] + f"{index:02}.jpg")
            # split_path = Path(self.session.path["split"])
            view_path = Path(self.session.path["view"])
            res = SessionManager.RESOLUTION

            # Helper.update_split_time(save_path=split_path)
            Helper.update_view_sequence(save_path=view_path, current_page=current_page)
            Helper.save_screenshot(save_path_str=str(origin_path), resolution=res)

            self.view_list.append(
                View(index=index, name=current_page, prefix=self.session.pre)
            )

    def split_data(self):
        if self.session is None:
            raise RuntimeError("Session not initialized.")
        else:
            raw_path = self.session.path["raw"]
            view_path = self.session.path["view"]
            # save_paths = [v.path["split"] for v in self.view_list]
            save_dir = self.session.dir["split"]

            Helper.split(
                raw_path=raw_path,
                view_path=view_path,
                save_dir=save_dir,
            )


if __name__ == "__main__":
    pd.set_option("display.float_format", "{:.2f}".format)
    mng = SessionManager()
    mng.init_session()
    mng.split_data()
