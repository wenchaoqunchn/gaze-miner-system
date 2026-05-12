# Gaze-Miner: 一种基于眼动追踪的交互可用性测试与自动分析系统

## 🌟 系统概述

**Gaze-Miner** 是一个专门为 HCI（人机交互）和软件工程研究者设计的眼动数据采集与分析框架。系统通过前端 UI 探针与后端硬件驱动的协同，实现了测试场景模拟、视线坐标实时捕获、界面自动对齐截图以及多维度数据切片。

本系统特别解决了传统眼动实验中“数据采集与业务状态脱节”的痛点，能够自动将长序列眼动原始数据（Raw Data）与具体的交互界面（AOI/View）进行时间轴匹配。

## 🚀 核心功能

* **实时硬件控制**：基于 Python 多进程架构，稳定驱动 Tobii Interaction SDK。
* **多模态对齐**：通过 Vue Router 拦截器，在用户切换页面瞬间自动触发系统级截图与时间戳打点。
* **自动 AOI 提取**：内置 DOM 语义探针，支持一键导出网页组件的物理坐标与业务语义。
* **自动化切片分析**：内置基于 Pandas 的离线处理工具链，将全局轨迹自动拆解为单页视图序列。
* **可视化支持**：支持导出用于绘制热力图、注视轨迹图（Scanpath）的结构化 CSV。

## 🛠️ 系统架构

系统采用前后端分离的解耦架构：

* **Frontend (Vue 3 + Vite)**: 充当实验场景载体，通过 Axios 实时同步交互状态。
* **Backend (Flask + Python)**: 核心守护进程，负责 Tobii 眼动仪数据流持久化与 Win32 GUI 截图。
* **Data Storage**: 基于会话（Session）的资产管理模式。

## 📦 快速开始

### 1. 后端配置 (Python 3.8+)

```bash
cd backend
# 建议重建 venv 环境
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
# 安装依赖
pip install -r requirements.txt
# 运行服务
python run.py

```

> **注意**：由于涉及硬件调用，请确保本地已安装 [Tobii Experience]

### 2. 前端配置 (Node.js 16+)

```bash
cd frontend
npm install
npm run dev

```

## 📂 数据结构说明

每次实验会话生成的 `data/session_xx` 目录结构如下：

```text
/session_xx
  ├── raw_data.csv        # 原始眼动点序列 (timestamp, x, y)
  ├── view_switch.csv     # 业务状态迁移节点 (view_name, timestamp)
  ├── img/                # 对应每个视图的自动全屏截图
  └── split_data/         # [后期处理] 对应截图的眼动子序列

```

## 🔮 未来规划 (Gaze-Reasoner)

我们正致力于将本系统与 **多模态大模型 (VLM)** 结合，通过 **GazeReasoner** 算法实现从“发现缺陷”到“自动生成诊断报告”的跨越。相关模块即将更新。
