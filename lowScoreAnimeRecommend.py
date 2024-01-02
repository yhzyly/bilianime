#显示数据
#词云图

import ast
import wordcloud#词云库
from operator import itemgetter # 导入定位的头方便定位按照哪里排序
import csv


#根据评分降序排列
datas = [] # 开个列表存放类型关键词
with open('C:\\Users\\yhzyl\\Desktop\\animeList.csv','r',encoding='utf-8') as f:
    f_csv=csv.reader(f)
    headers=next(f_csv)
    table=[]
    for line in f_csv:
        print(line)
        line[2] = float(line[2])
        # line[1] = line[1].strip()
        table.append(line)
    table_sorted = sorted(table,key=itemgetter(2),reverse=False) #精确的按照第1列排序
    for row in table_sorted:
        # datas.append(row)
        # print(datas)
        if row[2]<=7:
            list_list = ast.literal_eval(row[3])#形如list的字符串转list
            datas=datas+list_list
    print(datas)
f.close()


#list转字符串
# total_row=total_row+datas     
string1=" ".join(datas)
print(string1)


#画图
w=wordcloud.WordCloud(width=1000,
                      height=700,
                      background_color='white',
                      font_path='msyh.ttc',
                      scale=15,
                      stopwords={' '},
                    #   contour_width=5,
                    #   contour_color='red'
)
w.generate(string1)
w.to_file('C:\\Users\\yhzyl\\Desktop\\b站烂番词云.png')                      
