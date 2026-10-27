# bilianime
b站番剧信息爬取+协同过滤相似度根据新番类型预测播放量

大数据项目

https://api.bilibili.com/pgc/season/index/result?season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=1&season_type=1&pagesize=20&type=1

第一行这个就是爬取的首页链接。就跟下面那个url一样


1.aid就是article id的意思，或者说就是视频的av号；

2.pid是page id的意思，也就是说视频的第几个分页；

3.cid是chat id的意思，每个chat id对应一组弹幕池和

播放器：http://interface.bilibili.cn/playurl?cid=
cid获取：http://api.bilibili.cn/view?type=json&id=

## 开发者工具关键词：
视频信息：playinfo 获取音视频


## 爬取页面：
番剧索引：

page 1： https://www.bilibili.com/anime/index/?spm_id_from=333.6.b_7375626e6176.7
                 #season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1
                 &season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=1
                 
page 2： https://www.bilibili.com/anime/index/?spm_id_from=333.6.b_7375626e6176.7
               #season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1
                &season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=2 
                
以上界面网址源代码里没有想要数据，抓包获取

url：https://api.bilibili.com/pgc/season/index/result?season_version=-1&spoken_language_type=-1
       &area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1
       &order=3&st=1&sort=0&page=3&season_type=1&pagesize=20&type=1

番剧类型：https://api.bilibili.com/pgc/season/web/related/recommend?season_id=39433

md28235125 位于上面url源代码字典中，具体内容如下：
<a href="//www.bilibili.com/bangumi/media/md28235125/" target="_blank" class="media-cover"><!----></a>
在该页面的media-tags字段下有番剧类型 根据字典规则查询后返回一个list数据




