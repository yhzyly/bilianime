#-----1. 番剧索引界面抓包获取动态界面api的url info(title order link)
#-----2. 进入link获取评分 <div class="media-rating"><h4 class="score">8.9</h4>
#-----3. 保存至csv

import csv
import pprint
from turtle import write
import requests
import json
import re

def Crawler(url):
    # 伪装头
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
    }
    # requests模块获取相应
    response=requests.get(url=url,headers=headers)
    print(type(response.text))

    # str 转json字典 然后根据字典规则提取
    json_data=json.loads(response.text)
    pprint.pprint(json_data)

    inner_url = ['' for x in range(20)]
    title = ['' for x in range(20)]
    love = ['' for x in range(20)]
    score = ['' for x in range(20)]
    for i in range(json_data['data']['size']):#其实就是一页的大小20
        inner_url[i]=json_data['data']['list'][i]['link']
        title[i]=json_data['data']['list'][i]['title']
        love[i]=json_data['data']['list'][i]['order']
        score[i]=json_data['data']['list'][i]['score']

    #-----2. 进入link获取评分 正则匹配 同时获取media信息url从而获取番剧类型
    
    # media_url = ['' for x in range(20)]#第三层番剧类型界面
    media_tags = ['' for x in range(20)]
    playtime = ['' for x in range(20)]
    for i in range(20):
        response2=requests.get(url=inner_url[i],headers=headers)

        media_tags[i]=re.findall('"styles":(.*?),"actors"',response2.text)[0]
        
        playtime[i]= re.findall('已观看(.*?)次',response2.text)[0]
        if "亿" in playtime[i]:
            playtime[i] = str(float(playtime[i][:-1])*1000)+"万"



    #----- 3. 保存数据
    animelist=[]
    for i in range(20):
        animelist.append([title[i],love[i],score[i],media_tags[i],playtime[i]])
    with open('animeList.csv',mode='a',encoding='utf-8-sig',newline='')as f:
        writer=csv.writer(f)
        writer.writerows(animelist)
        f.close()


if __name__ == '__main__':
    header_list=['title','love','score','tags','play_times']
    with open('animeList.csv',mode='w',encoding='utf-8-sig',newline='')as f:
        writer=csv.writer(f)
        writer.writerow(header_list)
        f.close()

    #-----1. 数据获取 url动态变化，page值递增
    # url
    page_num = 0
    while(page_num<20):#while循环条件的判断条件是爬虫爬取的次数，即番剧列表的页数，10即为10页，每页20个番剧信息
        page_num=page_num+1
        url = 'https://api.bilibili.com/pgc/season/index/result?season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page='+str(page_num)+'&season_type=1&pagesize=20&type=1'
        Crawler(url)
    


