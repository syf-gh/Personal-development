from file_Define import Rscord
from file_Reader import Txt_Read_Data,Json_Read_Data,Reader
import json
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
txt_read_data = Txt_Read_Data("D:/一月.txt")
json_read_data = Json_Read_Data("D:/二月.txt")
yiyue_data = txt_read_data.read_data() #获取一月数据
eryue_data = json_read_data.read_data() #获取二月数据
#将数据总合
all_data:list[Rscord] = yiyue_data +eryue_data
data_dict:dict = {}
for rscord in all_data:
    if rscord.date in data_dict.keys():#相同日期相加金额
        data_dict[rscord.date] += rscord.money
    else:   #不在的开新键date
        data_dict[rscord.date] = rscord.money
#开始图表开发
bar = Bar()
bar.add_xaxis(list(data_dict.keys()))  #添加x数据
bar.add_yaxis("销售额",list(data_dict.values()))# 添加y数据
bar.set_global_opts(
    title_opts=TitleOpts(
        is_show=True,
        title= "每日销售额",
        pos_left= "center",pos_bottom= "1%"
    )
)
bar.render("每日销售额柱状图.html")
