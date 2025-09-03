# 销售数据可视化分析系统

这是一个用于处理和可视化销售数据的Python项目。项目通过面向对象编程设计，能够读取不同格式（TXT/JSON）的原始数据，进行清洗和聚合，并利用PyEcharts库生成交互式的每日销售额柱状图。

## 项目结构

Sales-Data-Visualization/
├── data/ # 原始数据目录
│ ├── 一月.txt # 一月份销售数据（TXT格式）
│ └── 二月.txt # 二月份销售数据（JSON格式）
├── src/ # 源代码目录
│ ├── file_Define.py # 数据实体类定义
│ ├── file_Reader.py # 数据读取类（支持TXT和JSON）
│ └── main.py # 主程序，负责数据整合与图表生成
├── output/ # 输出结果目录
│ └── 每日销售额柱状图.html # 生成的可视化图表
└── README.md # 项目说明

## 技术栈

- **Python 3**
- **PyEcharts** (用于数据可视化)
- 面向对象编程（OOP）

## 核心功能

1.  **数据封装**：使用自定义类`Rscord`封装每条订单数据，保证数据安全。
2.  **多格式读取**：通过继承实现`Txt_Read_Data`和`Json_Read_Data`类，分别处理TXT和JSON格式文件。
3.  **数据聚合**：按日期对销售额进行累加统计。
4.  **可视化**：使用PyEcharts生成直观的柱状图，展示每日销售趋势。

## 如何运行

1.  确保你的环境已安装Python 3.x。
2.  安装依赖库：`pip install pyecharts`
3.  进入`src`目录，运行主程序：
    ```bash
    cd src
    python main.py
    ```
4.  程序运行成功后，可在 `output` 目录下打开 `每日销售额柱状图.html` 查看可视化结果。

## 学习说明

本项目是我在学习Python数据处理和可视化过程中完成的实践项目，通过它我深入理解了面向对象编程、文件操作以及PyEcharts库的使用。