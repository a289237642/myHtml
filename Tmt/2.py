# -*- coding:utf-8 -*-
# author: will
import re

import datetime
import time, redis
from bs4 import BeautifulSoup
from lxml import etree

import requests
from pymongo import MongoClient
from pymysql import connect
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class ArticleFilter(object):
    def __init__(self, title, content):
        self.redis_client = redis.StrictRedis(host='101.132.186.25', port='6379', db=9)

        self.first_keywords = str(self.redis_client.get('first_keywords')).split(',')
        self.second_keywords = str(self.redis_client.get('second_keywords')).split(',')
        self.title = title
        self.content = content
        self.group_id_list = list()

    # 一级关键词在内容中的频次
    def article_content_filter(self):
        first_keyword_dict = dict()
        second_keyword_dict = dict()

        # 内容查找
        if isinstance(self.content, list):
            text = ''.join([item.get('text') for item in self.content if item.get('text')])
            # 查询文章内容含有的频次最高的一级关键词
            for first_keyword in self.first_keywords:
                num = 0
                num += text.count(first_keyword)
                if num > 0:
                    first_keyword_dict[first_keyword] = num
            first_res = self.select_high(first_keyword_dict)
            if len(first_res) == 1:
                keyword, num = first_res[0][0], first_res[0][1]
                keyword = {'first_keywords': keyword}
            else:
                # 频次最高的一级关键词没有或者有多个,采用二级属性词分类标准
                for second_keyword in self.second_keywords:
                    num = 0
                    num += text.count(second_keyword)
                    if num > 0:
                        second_keyword_dict[second_keyword] = num
                second_res = self.select_high(second_keyword_dict)
                if len(second_res) == 1:
                    keyword, num = second_res[0][0], second_res[0][1]
                    keyword = {'second_keywords': keyword}
                elif len(second_res) > 1:
                    # 频次最高的二级属性词有多个,文章分别上架到二级属性词对应的文章分类
                    keyword = [x[0] for x in second_res]
                    keyword = {'second_keywords': keyword}
                else:
                    # 没有匹配到二级属性词,但频次最高的一级关键词有多个,文章分别上架到一级关键词对应的文章分类
                    if len(first_res) > 1:
                        keyword = [x[0] for x in first_res]
                        keyword = {'first_keywords': keyword}
                    else:
                        return False
            return keyword
        return False

    # 标题查找
    def article_title_filter(self):
        first_keyword_dict = dict()

        for first_keyword in self.first_keywords:
            num = 0
            num += self.title.count(first_keyword)
            if num > 0:
                first_keyword_dict[first_keyword] = num
        first_res = self.select_high(first_keyword_dict)
        if len(first_res) == 1:
            keyword, num = first_res[0][0], first_res[0][1]
            first_keywords = {'first_keywords': keyword}
            return first_keywords
        return False

    # 关键词查找--主函数,返回文章关键词对应的分类ID
    def article_filter(self):
        # 1.标题查找
        title_keyword = self.article_title_filter()
        if title_keyword:
            first_keywords = title_keyword.get('first_keywords')
            group_id = self.get_keyword_group_id(first_keywords)
            self.group_id_list.append(group_id)
        else:
            # 2.内容查找
            content_keyword = self.article_content_filter()
            if content_keyword:
                first_keywords = content_keyword.get('first_keywords')
                if isinstance(first_keywords, str):
                    group_id = self.get_keyword_group_id(first_keywords)
                    self.group_id_list.append(group_id)

                elif isinstance(first_keywords, list):
                    for first_keyword in first_keywords:
                        group_id = self.get_keyword_group_id(first_keyword)
                        self.group_id_list.append(group_id)

                else:
                    second_keywords = content_keyword.get('second_keywords')
                    if isinstance(second_keywords, str):
                        group_id = self.get_keyword_group_id(second_keywords)
                        self.group_id_list.append(group_id)

                    elif isinstance(second_keywords, list):
                        for second_keyword in second_keywords:
                            group_id = self.get_keyword_group_id(second_keyword)
                            self.group_id_list.append(group_id)
                    else:
                        self.group_id_list = None
            else:
                self.group_id_list = None

        return self.group_id_list

    # 选取出现频次最高的关键字
    @staticmethod
    def select_high(keyword_dict):
        ls = sorted(list(keyword_dict.items()), key=lambda a: a[1], reverse=True)
        index = 0
        for i, x in enumerate(ls):
            if x[1] == ls[0][1]:
                index = i + 1
            else:
                break
        print((ls[:index]))
        return ls[:index]

    # Redis取出关键词对应的文章分类ID
    def get_keyword_group_id(self, keyword):
        article_group_id = self.redis_client.hget('group_id_of_keyword', keyword)
        return article_group_id

    # 文章敏感词过滤
    def sensitive_words_filter(self):
        try:
            sensitive_words = self.redis_client.get('sensitive_words')
            if sensitive_words:
                sensitive_words = sensitive_words.split(',')
                text = ''.join([item.get('text') for item in self.content if item.get('text')])
                for sensitive_word in sensitive_words:
                    resp_title = self.title.find(sensitive_word)
                    resp_content = text.find(sensitive_word)
                    if resp_title != -1 or resp_content != -1:
                        return True
                    else:
                        return False
            else:
                return False
        except Exception as e:
            return False


class huxiu_spider(object):
    def __init__(self):
        self.base_url = 'https://www.huxiu.com/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}

    def send_request(self, url):

        response = requests.get(url, headers=self.headers)
        text = response.text
        return text

    # 文章列表
    def first_analysis(self, text):

        selector = etree.HTML(text)
        results = selector.xpath('//div[@class="container"]/div[2]/div[2]/div')
        # //*[@id="index"]/div[1]/div[2]/div[9]/div[1]/a/div/@style
        # //div[@class="container"]/div[2]/div[2]/div   --new
        # //*[@id="index"]/div[1]/div[2]/div   --old
        new_list = []
        i = 1
        for res in results:
            res_dict = {}
            web_name = '虎嗅网'
            res_dict['web_name'] = web_name
            # 文章标题
            title = res.xpath('div/h2/a/text()')[0]
            print('正在爬取第%s篇文章,标题是:%s' % (i, title))
            num = self.get_title(title, web_name)
            print('查看文章是否存在=====')
            if num == 0:
                print('文章不存在～～～')
                url = res.xpath('div/h2/a[starts-with(@href, "/article")]/@href')[0]
                article_link = 'https://www.huxiu.com' + url
                article_content, article_time = self.second_analysis(article_link)
                if article_content != 1:
                    print('敏感词开始过滤')
                    # 本地敏感关键词过滤
                    article_filter_obj = ArticleFilter(title, article_content)
                    resp = article_filter_obj.sensitive_words_filter()
                    if resp:
                        print('文章存在敏感词汇')
                    else:
                        # 文章内容
                        res_dict['content'] = article_content
                        # 文章发布时间
                        res_dict['date'] = article_time
                        # 文章内容链接
                        res_dict['article_link'] = article_link
                        # 文章标题
                        res_dict['title'] = title
                        # 文章简介
                        summary = res.xpath('div/div[2]/text()')[0]
                        res_dict['summary'] = summary
                        # 文章作者
                        name = res.xpath('div/div/a/span/text()')[0]
                        res_dict["name"] = name
                        # 文章作者链接
                        # res_dict["author_link"] = 'https://www.huxiu.com' + res.xpath('div/div/a/@href')[0]

                        # 文章列表主图
                        if res.xpath('div/a/img/@data-original'):
                            min_pic = res.xpath('div/a/img/@data-original')[0]
                            oss_url = self.upload_oss(min_pic)
                            # oss_url = oss_url.replace('http', 'https')
                            res_dict["min_pic"] = oss_url
                        elif res.xpath('a/div/img/@data-original'):
                            min_pic = res.xpath('a/div/img/@data-original')[0]
                            oss_url = self.upload_oss(min_pic)
                            # oss_url = oss_url.replace('http', 'https')
                            res_dict["min_pic"] = oss_url
                        elif res.xpath('div/a/div/@style'):
                            # 截取图片是视频样式的
                            mystr = res.xpath('div/a/div/@style')[0]
                            print(111, mystr)
                            start_index = mystr.find('(', 0, len(mystr))
                            end_index = mystr.find('?', 0, len(mystr))
                            min_pic = mystr[start_index + 2:end_index]
                            print(123, min_pic)
                            oss_url = self.upload_oss(min_pic)
                            print(321, oss_url)
                            # oss_url = oss_url.replace('http', 'https')
                            res_dict["min_pic"] = oss_url
                        else:
                            oss_url = ''
                            res_dict["min_pic"] = oss_url

                        self.upload_mongo(res_dict)
                        self.upload_mysql(title, name, article_time, oss_url, summary, web_name, article_link)
                        print('成功获取并保存第%s篇文章' % i)
                        i += 1
                        new_list.append(res_dict)
                else:
                    i += 1
                    continue
            else:
                i += 1
                continue
        print('成功获取到%s篇文章' % (i - 1))

    # 文章内容
    def second_analysis(self, url):
        try:
            # 自定义PhantomJS的请求头
            cap = DesiredCapabilities.PHANTOMJS.copy()

            for key, value in self.headers.items():
                cap['phantomjs.page.customHeaders.{}'.format(
                    key)] = value
            # browser = webdriver.PhantomJS(
            # '/Users/fushande/Shande_Zhijian/phantomjs-2.1.1-macosx/phantomjs-2.1.1-macosx/bin/phantomjs')
            browser = webdriver.PhantomJS('/usr/local/lib/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
            # browser = webdriver.PhantomJS('/www/zhijiantest/phantomjs-1.9.7-linux-x86_64/bin/phantomjs')

            browser.get(url)
            time.sleep(3)
            html = browser.page_source

            # 选取文章发布时间
            selector = etree.HTML(html)
            #  //div[@class="column-link-box"]/span[1]/text() ---new
            #  //*[@class="article-author"]/div/span[1]/text() ---old
            if selector.xpath('//div[@class="column-link-box"]/span[1]/text()'):
                article_time = selector.xpath('//div[@class="column-link-box"]/span[1]/text()')[0]
                print(article_time)
            elif selector.xpath('//*[@class="article-author"]/span[2]/text()'):
                article_time = selector.xpath('//*[@class="article-author"]/span[2]/text()')[0]
            else:
                article_time = ''

            # 文章内头图
            if selector.xpath('//div[@class="article-img-box"]/img/@src'):
                article_min_pic = selector.xpath('//div[@class="article-img-box"]/img/@src')[0]
            else:
                article_min_pic = ""
            # 选取文章内容
            content = selector.xpath('//*[@class="article-content-wrap"]')[0]
            result = etree.tostring(content, method='html')
            print('获取到文章内容')
            # 获取bs4对象
            soup = BeautifulSoup(result, 'html.parser', from_encoding='utf-8')
            new_list = []

            # 通过标签来获取内容
            ls = soup.find_all(["p", "img"])
            for table in ls:
                res = {}
                data = table.get_text()
                if data:
                    # # 去除空字符和特殊字符
                    new_data = "".join(data.split())
                    new_data = new_data.replace(u'\ufeff', '')
                    if new_data != "":
                        res["text"] = new_data
                        new_list.append(res)

                link = table.get('src')
                if link:
                    oss_url = self.upload_oss(link)
                    res["img"] = oss_url
                    new_list.append(res)
            if article_min_pic != '':
                article_min_pic = self.upload_oss(article_min_pic)
                # article_min_pic = article_min_pic.replace('http', 'https')
                new_list.insert(0, {'img': article_min_pic})
            browser.quit()
            return new_list, article_time

        except Exception as e:
            print('文章不存在了', e)
            return 1, 1

    # 上传图片到oss
    def upload_oss(self, url):

        kw = {
            'fileurl': url,
            'filepath': 'gander_goose/dev/test2'
        }
        result = requests.post(url='http://api.max-digital.cn/Api/oss/uploadByUrl', data=kw)
        result = result.json()
        oss_url = result.get('oss_file_url')
        oss_url = oss_url.replace('maxpr.oss-cn-shanghai.aliyuncs.com', 'cdn.max-digital.cn')
        oss_url = oss_url.replace('http', 'https')
        return oss_url

    # 数据上传mongo
    def upload_mongo(self, article_dict):
        try:
            client = MongoClient('47.100.63.158', 27017)
            my_db = client.wechat
            my_db.articles.insert_one(article_dict)
            print('上传到mongo成功')
        except Exception as e:
            print('上传到mongo失败:', e)

    # 插入到mysql
    def upload_mysql(self, title, name, date, oss_url, summary, web_name, link):
        try:
            # 上传mysql
            # 创建Connection连接
            # conn = connect(host='localhost', port=3306, database='wechat',
            #                user='root', password='mysql', charset='utf8')
            conn = connect(host='rm-uf6gw23j409s5ui7qmoo.mysql.rds.aliyuncs.com', port=3306,
                           database='zjlivenew',
                           user='maxpr_mysql', password='COFdjwD*$*m8bd!HtMLP4+Az0eE9m', charset='utf8')
            # 获得Cursor对象
            cs1 = conn.cursor()
            # 执行insert语句，并返回受影响的行数：添加一条数据
            # 增加
            now = datetime.datetime.now()
            imgurl = "https://cdn.max-digital.cn/gander_goose/dev/test2/15368082362561.jpg"
            sql1 = "insert into zj_article_info (title,author,wechat_art_date,min_pic,summary,web_name,is_show,is_big,link,round_head_img,create_time) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                title, name, date, oss_url, summary, web_name, 0, 0, link, imgurl, now)
            cs1.execute(sql1)
            # 获取最新插入的文章的ID
            new_article_id = int(conn.insert_id())

            # 修改分类--24小时下文章的自定义排序值
            # sql2 = 'update zj_article_group set sort_num = sort_num + 1 where group_id=1'
            # cs1.execute(sql2)

            # 上线到24小时分类
            sql3 = 'insert into zj_article_group (article_id,group_id,sort_num,create_time) values ("%s", "%s", "%s", "%s")' % (
                new_article_id, 1, 1, now)
            cs1.execute(sql3)

            # 修改文章上线状态
            sql4 = "update zj_article_info set is_show = 1, zj_art_date='%s' where id='%s'" % (now, new_article_id)
            cs1.execute(sql4)

            conn.commit()
            cs1.close()
            conn.close()
            print('上传到mysql成功')
        except Exception as e:
            print('mysql上传失败:', e)

    def get_title(self, title, query):
        # 查询mysql
        conn = connect(host='rm-uf6gw23j409s5ui7qmoo.mysql.rds.aliyuncs.com', port=3306,
                       database='zjlivenew',
                       user='maxpr_mysql', password='COFdjwD*$*m8bd!HtMLP4+Az0eE9m', charset='utf8')
        # 获得Cursor对象
        cs1 = conn.cursor()
        res = 'select * from zj_article_info where title = "%s" and web_name = "%s" ' % (title, query)
        num = cs1.execute(res)

        return num

    def run(self):
        text = self.send_request(self.base_url)
        self.first_analysis(text)


if __name__ == '__main__':
    huxiu = huxiu_spider()
    while True:
        start_time = time.time()
        print('开始时间:', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)))
        huxiu.run()
        time.sleep(3600)
