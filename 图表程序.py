# -*- coding:utf-8 -*-
# py-2
from pyecharts import Bar
from pyecharts import Map
from pyecharts import Geo
from pyecharts import EffectScatter
from pyecharts import Pie
from pyecharts import Radar 
import random
import pandas as pd

# 危化品折线图两个变量
bar=Bar(" "," ")#主副标题
t = ["2004","2005","2006", "2007", "2008", "2009", "2010", "2011", "2012",
 "2013", "2014", "2015", "2016", "2017", "2018"]
y = [196,126,161,98,96,87,76,77,52,37,36,32,33,31,25]
e = [295,223,291,166,164,157,143,140,116,76,54,55,52,72,56]
bar.add("事故起数",t,y,is_more_utils=True)#标题
bar.add("伤亡人数",t,e,is_more_utils=True)#标题
bar.show_config()
bar.render("zha1.html")



#2个系列的5个维度的数据
value1 = [[99,69,102,105,104,113,111,98,96,89,86,92]]
#用于调整雷达各维度的范围大小
c_schema= [{"name": "一月", "max": 120, "min": 0},
           {"name": "二月", "max": 120, "min": 0},
           {"name": "三月", "max": 120, "min": 0},
           {"name": "四月", "max": 120, "min": 0},
           {"name": "五月", "max": 120, "min": 0},
           {"name": "六月", "max": 120, "min": 0},
           {"name": "七月", "max": 120, "min": 0},
           {"name": "八月", "max": 120, "min": 0},
           {"name": "九月", "max": 120, "min": 0},
           {"name": "十月", "max": 120, "min": 0},
           {"name": "十一月", "max": 120, "min": 0},
           {"name": "十二月", "max": 120, "min": 0}]
radar = Radar("ABCDE的雷达图",title_pos='left')
radar.config(c_schema=c_schema,radar_text_size=20)
radar.add(" ", value1, item_color='#2525f5', 
          symbol=None,aarea_opacity=0.3,
          legend_top='bottom',line_width=3)
radar.render("Rader.html")
#f9713c


attr=['生产过程火灾爆炸事故','生产过程中毒伤害事故','储存过程中重特大事故',
'运输过程中火灾爆炸事故','运输过程中毒伤害事故','使用、销售过程中造成的重特大伤亡事故',
'储罐、管道重特大泄漏事故的应急救援','运输车辆、船舶重特大泄漏事故的应急救援','危险化学品其他重特大事故']
v1=[94,55,27,19,15,15,7,8,19]
#v2=[85,24,39,80,27]
pie=Pie(" ",title_pos='left',width=1000,height=300)
pie.add('1',attr,v1, center=[50,60],radius=[30,75],is_label_show=True)
#pie.add('2',attr,v2, center=[75,50],radius=[30,75],is_label_show=True)
pie.render('kongqi5.html')
#'生产过程火灾爆炸事故','生产过程中毒伤害事故','储存过程中重特大事故',
#'运输过程中火灾爆炸事故','运输过程中毒伤害事故','使用、销售过程中造成的重特大伤亡事故',
#'储罐、管道重特大泄漏事故的应急救援','运输车辆、船舶重特大泄漏事故的应急救援','危险化学品其他重特大事故'


a=[("新疆",3),("内蒙古",11),("黑龙江",12),
("吉林",2),("辽宁",16),("甘肃",11),("北京",10),
("宁夏",6),("河北",81),("天津",9),("西藏",5),
("四川",59),("重庆",6),("陕西",12),
("山西",15),("山东",116),("河南",81),("江苏",151),
("安徽",21),("湖北",140),("云南",59),("湖南",16),
("江西",9),("浙江",59),("广西",8),("广东",11),
("福建",8),("澳门",0),("海南",0),("青海",0),("上海",0),("贵州",0)]
a=pd.DataFrame(a)
a.columns=['city','popu']
map=Map("各省市人口数", "单位：万人", title_color="#fff", 
	title_pos="center", width=1200,  height=600)
attr=a['city']
value=a['popu']
map.add("", attr, value, visual_range=[0, 120], visual_text_color="#fff",
	symbol_size=15, is_visualmap=True,is_label_show=True)
map.render('wq.html')
#map背景参数, background_color='#404a59'
