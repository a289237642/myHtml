Last login: Tue Jul  2 11:43:31 on ttys001
bogon:~ a289237642$ ls
Applications    Downloads       Movies          Public          go
Desktop         IdeaProjects    Music           PycharmProjects py3
Documents       Library         Pictures        dbs
bogon:~ a289237642$ cd Desktop/
bogon:Desktop a289237642$ ls
demo           myHtml         project_h5_api tv_api         zhijianlive
goproject      newProject     share_h5       tv_dist
bogon:Desktop a289237642$ git clone git@47.92.207.84:a289237642/bjLive.git
正克隆到 'bjLive'...
remote: Counting objects: 94, done.
remote: Compressing objects: 100% (84/84), done.
remote: Total 94 (delta 18), reused 0 (delta 0)
接收对象中: 100% (94/94), 48.04 KiB | 1.26 MiB/s, 完成.
处理 delta 中: 100% (18/18), 完成.
bogon:Desktop a289237642$ ls
bjLive         goproject      newProject     share_h5       tv_dist
demo           myHtml         project_h5_api tv_api         zhijianlive
bogon:Desktop a289237642$ ls
bjLive         goproject      newProject     share_h5       tv_dist
demo           myHtml         project_h5_api tv_api         zhijianlive
bogon:Desktop a289237642$ ls
bjLive         goproject      newProject     share_h5       tv_dist
demo           myHtml         project_h5_api tv_api         zhijianlive
bogon:Desktop a289237642$ ls
bjLive         goproject      newProject     share_h5       tv_dist
demo           myHtml         project_h5_api tv_api         zhijianlive
bogon:Desktop a289237642$ 
bogon:Desktop a289237642$ 
Display all 1434 possibilities? (y or n)
bogon:Desktop a289237642$ 
bogon:Desktop a289237642$ ls
bjLive         goproject      newProject     share_h5       tv_dist
demo           myHtml         project_h5_api tv_api         zhijianlive
bogon:Desktop a289237642$ ls
bjLive         goproject      newProject     share_h5       tv_dist
demo           myHtml         project_h5_api tv_api         zhijianlive
bogon:Desktop a289237642$ 
bogon:Desktop a289237642$ ssh root@101.132.186.25 
root@101.132.186.25's password: 
Welcome to Ubuntu 14.04.5 LTS (GNU/Linux 4.4.0-93-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

Welcome to Alibaba Cloud Elastic Compute Service !

Last login: Tue Jul  2 12:12:22 2019 from 106.38.108.50
root@iZuf6ay3rmus2m6o26tir7Z:~# ls
envs  py3  test
root@iZuf6ay3rmus2m6o26tir7Z:~# cd /www/
root@iZuf6ay3rmus2m6o26tir7Z:/www# ls
celery_tasks  envs	zjlive	    zjlive.tar.bz2
cert	      uwsgitop	zjlive_new  zjvue_new
root@iZuf6ay3rmus2m6o26tir7Z:/www# cd zjlive_new/
root@iZuf6ay3rmus2m6o26tir7Z:/www/zjlive_new# ls
zhijian  zj_spider
root@iZuf6ay3rmus2m6o26tir7Z:/www/zjlive_new# cd zj_spider/
root@iZuf6ay3rmus2m6o26tir7Z:/www/zjlive_new/zj_spider# ls
ghostdriver.log  huixiu  huxiu	huxiu.base
root@iZuf6ay3rmus2m6o26tir7Z:/www/zjlive_new/zj_spider# ll
-bash: ll: command not found
root@iZuf6ay3rmus2m6o26tir7Z:/www/zjlive_new/zj_spider# ls -l
total 64
-rw-r--r-- 1 root root  3136 Jun 17 15:15 ghostdriver.log
-rw-r--r-- 1 root root 18471 Jun 17 11:09 huixiu
-rw-r--r-- 1 root root 18472 Jun 17 14:22 huxiu
-rw-r--r-- 1 root root 18359 May 28 11:28 huxiu.base
root@iZuf6ay3rmus2m6o26tir7Z:/www/zjlive_new/zj_spider# ls
ghostdriver.log  huixiu  huxiu	huxiu.base
root@iZuf6ay3rmus2m6o26tir7Z:/www/zjlive_new/zj_spider# 
root@iZuf6ay3rmus2m6o26tir7Z:/www/zjlive_new/zj_spider# ls
ghostdriver.log  huixiu  huxiu	huxiu.base
root@iZuf6ay3rmus2m6o26tir7Z:/www/zjlive_new/zj_spider# 
root@iZuf6ay3rmus2m6o26tir7Z:/www/zjlive_new/zj_spider# ls
ghostdriver.log  huixiu  huxiu	huxiu.base
root@iZuf6ay3rmus2m6o26tir7Z:/www/zjlive_new/zj_spider# ls
ghostdriver.log  huixiu  huxiu	huxiu.base
root@iZuf6ay3rmus2m6o26tir7Z:/www/zjlive_new/zj_spider# ls
ghostdriver.log  huixiu  huxiu	huxiu.base
root@iZuf6ay3rmus2m6o26tir7Z:/www/zjlive_new/zj_spider# vi huxiu.base 

  1 
  2 # -*- coding:utf-8 -*-
  3 # author: will
  4 import re
  5 
  6 import datetime
  7 import time, redis
  8 from bs4 import BeautifulSoup
  9 from lxml import etree
 10 
 11 import requests
 12 from pymongo import MongoClient
 13 from pymysql import connect
 14 from selenium import webdriver
 15 from selenium.webdriver import DesiredCapabilities
 16 
 17 
 18 class ArticleFilter(object):
 19     def __init__(self, title, content):
 20         self.redis_client = redis.StrictRedis(host='101.132.186.25', port='6379', db=9)
 21 
 22         self.first_keywords = str(self.redis_client.get('first_keywords')).split(',')
 23         self.second_keywords = str(self.redis_client.get('second_keywords')).split(',')
 24         self.title = title
 25         self.content = content
 26         self.group_id_list = list()
 27 
 28     # 一级关键词在内容中的频次
 29     def article_content_filter(self):
 30         first_keyword_dict = dict()
 31         second_keyword_dict = dict()
 32 
 33         # 内容查找
 34         if isinstance(self.content, list):
 35             text = ''.join([item.get('text') for item in self.content if item.get('text')])
 36             # 查询文章内容含有的频次最高的一级关键词
 37             for first_keyword in self.first_keywords:
 38                 num = 0
 39                 num += text.count(first_keyword)
 40                 if num > 0:
 41                     first_keyword_dict[first_keyword] = num
 42             first_res = self.select_high(first_keyword_dict)
 43             if len(first_res) == 1:
 44                 keyword, num = first_res[0][0], first_res[0][1]
 45                 keyword = {'first_keywords': keyword}
 46             else:
 47                 # 频次最高的一级关键词没有或者有多个,采用二级属性词分类标准
 48                 for second_keyword in self.second_keywords:
                                                                                                                                                                   1,0-1         Top
