from pyecharts import options as opts
from pyecharts.charts import Page, Pie

v1 = ["中南","西北","西南","東北","華北","華東"]
v2 = [26,5,9,17,17,26]

#繪製環圈圖
def pie_radius() -> Pie:
    c = (
        Pie()
        #設定圓環的寬度
        .add("",[list(z) for z in zip(v1, v2)],radius=["40%", "75%"])  
        #設定圓環的顏色
        .set_colors(["blue", "green", "purple", "red", "silver"])    
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2020年上半年不同收入群體的購買力分析",title_textstyle_opts=opts.TextStyleOpts(font_size=20)),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(orient="vertical", pos_top="35%", pos_left="2%",textstyle_opts=opts.TextStyleOpts(font_size=16))
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}",font_size = 16))
    )
    return c

#資料視覺化圖表
pie_radius().render("pie-radius.html")