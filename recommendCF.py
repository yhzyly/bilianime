#协同过滤CF 根据新番标签预测播放量
import numpy as np
import ast
from operator import itemgetter # 导入定位的头方便定位按照哪里排序
import csv

#输入新番标签
new_anime=['热血','奇幻','校园']



#默认追番量降序
#读取第4列类型标签tags，row[3]表示 row迭代器 第4列
similarity=[]
play_time=[]

total_row=[]
with open('C:\\Users\\yhzyl\\Desktop\\animeList.csv',encoding='utf-8')as f:
    f_csv=csv.reader(f)
    headers=next(f_csv)
    for row in f_csv:
        i=0 #记录匹配tag数
        # print(type(row[3]))
        # print(row[3])

        for target in new_anime:
            if target in row[3]:
                # print('in it')
                i=i+1
  
        list_list = ast.literal_eval(row[3])#形如list的字符串转list
        total_row=total_row+list_list

        if i==0:
            continue

        #生成两组tag占比list
        if(len(new_anime)<=len(list_list)):
            cords1 = [0. for x in range(len(list_list))]#new cords用来存tag权重
            cords2 = [1.0/len(list_list) for x in range(len(list_list))]

            for m in range(len(list_list)):
                for n in range(len(new_anime)):
                    if list_list[m]==new_anime[n]:
                        cords1[m]=1.0/i
                        print('匹配：'+list_list[m]+str(m))
        else:
            cords1 = [1.0/len(new_anime) for x in range(len(new_anime))]#new cords用来存tag权重
            cords2 = [0. for x in range(len(new_anime))]

            for m in range(len(new_anime)):
                for n in range(len(list_list)):
                    if list_list[n]==new_anime[m]:
                        cords2[m]=1.0/i
                        print('匹配：'+new_anime[m]+str(m))                   

        #避免算不出值
        cords1.append(1.0)
        cords2.append(1.0)    

        # 这里可以获得相似性矩阵(共现矩阵)
        # tmp=np.corrcoef(np.array(cords1), np.array(cords2))
        similarity.append(np.corrcoef(np.array(cords1), np.array(cords2))[0][1])
        # print(similarity)

        if '万' in row[4]:
            num=float(row[4].strip('万'))
            # num = float(re.search(r'\d(.\d)?', row[4]).group())
            # print(num)
            play_time.append(num)
        else:
            play_time.append(row[4])


    print(total_row)
    f.close()




"""计算前n个相似的用户"""
ziped=zip(play_time,similarity)
simi_list=list(ziped)
# print(list(ziped))

n = 15

table_sorted = sorted(simi_list,key=itemgetter(1),reverse=True) #精确的按照第1列排序
selected=table_sorted[:n]


# similarity_tags = similarity.sort_values(ascending=False)[:n]   
print(selected)





"""计算最终得分"""
# base_score = np.mean(np.array(selected))
base_score = np.mean(selected[0])
weighted_scores = 0.
corr_values_sum = 0.
for turple in selected:  # [2, 3]
    corr_value = turple[1]            # 两个用户之间的相似性
    weighted_scores += corr_value * turple[0]     # 加权分数
    corr_values_sum += corr_value
final_scores = weighted_scores / corr_values_sum
print('预测该番剧稳定后播放量为: ', final_scores,'万')


