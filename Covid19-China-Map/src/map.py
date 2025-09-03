from pyecharts.charts import Map
from pyecharts.options import global_options,ToolboxOpts,VisualMapOpts,TitleOpts
import json
#获取数据
f = open("D:/疫情.txt",'r',encoding='UTF-8')
#数据清洗
yq_data = f.read()
#将json转为python
yq_date = json.loads(yq_data)
# print(type(yq_date)) #字典
data_list = []
#获取相关省份数据
yq_date = yq_date["areaTree"][0]["children"]
for i in range(34):
    yq_sf = yq_date[i]["name"]
    yq_qz = yq_date[i]["total"]["confirm"]
    data_list.append((yq_sf,yq_qz))
#地图对象
map = Map()
map.add("各省份确诊人数",data_list,"china")
map.set_global_opts(
    visualmap_opts = VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1-99","color":"#2c9678"},
            {"min":100,"max":999,"label":"100-999","color":"#2983bb"},
            {"min":1000,"max":4999,"label":"1000-4999","color":"#fcd217"},
            {"min":5000,"max":9999,"label":"5000-9999","color":"#ff9900"},
            {"min":10000,"max":49999,"label":"10000-49999","color":"#ef6f48"},
            {"min":50000,"max":99999,"label":"50000-99999","color":"#f43e06"}
        ]
    ),
    title_opts= TitleOpts(
        is_show= True,
        title= "全国疫情省份地图参考",pos_bottom= "1%",pos_left= "center"
    )
)
map.render("疫情map.html")
f.close()