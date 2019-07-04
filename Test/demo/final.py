# -*- coding: utf-8 -*-
import scrapy, time
from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import Logging


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['weixin.qq.com']
    # allowed_domains = ['jandan.net']

    start_urls = [
        'https://mp.weixin.qq.com/s?__biz=MzA3NDI3MzMzMQ==&mid=2247485130&idx=1&sn=fe4ba4175900edfb01463467814d9818&scene=4#rd',
        'https://mp.weixin.qq.com/s?__biz=MzIyOTc5MzgwMQ==&mid=2247489999&idx=1&sn=640bf56eb003c78c74b9dcafe4532285&scene=4#rd'
    ]

    # start_urls = ['https://mp.weixin.qq.com/s?__biz=MzIyOTc5MzgwMQ==&mid=2247489999&idx=1&sn=640bf56eb003c78c74b9dcafe4532285&scene=4#rd'
    # ]
    # start_urls=['http://jandan.net/2019/06/27/eye-microbiome.html']

    def parse(self, response):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(response.url)
        dicts = {}
        selector = etree.HTML(driver.page_source)
        title = selector.xpath('//*[@id="activity-name"]/text()')[0]
        title = "".join(title.split())
        name = selector.xpath('//*[@id="js_name"]/text()')[0]
        name = "".join(name.split())
        spider_time = time.time()
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(spider_time))
        dicts['title'] = title
        dicts['name'] = name
        dicts['date'] = date
        dicts['web_name'] = name

        is_original = selector.xpath('//*[@id="copyright_logo"]/text()')
        if len(is_original) == 0:
            dicts['is_original'] = 0  # 不是原创
        else:
            dicts['is_original'] = 1  # 是原创

        # 用xpath取出需要的内容页面部分
        result = selector.xpath('//*[@id="js_content"]')[0]
        # 转为html
        content = etree.tostring(result, method='html')
        # 获取bs4对象
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        new_list = []
        # ls = soup.find_all(["p", "img", 'a', 'section'])
        ls = soup.find_all(["p", "img"])
        for table in ls:
            res = {}
            # print(type(table))
            try:
                target = [item.get('target') for item in table if item and item.get('target')]
                _break = [item.get('style') for item in table if
                          item and item.get('style') and 'break-word' in item.get('style')]
                # print(_break)
                if _break:
                    pass
                elif target and target[0] == '_blank':
                    pass
                elif table.get("style") and "break-word" in table.get("style"):
                    pass
                else:
                    data = table.get_text()
                    if data:
                        # 去除空字符和特殊字符
                        new_data = "".join(data.split())
                        new_data = new_data.replace('\ufeff', '')
                        if new_data != "":
                            res["text"] = new_data
                    link = table.get('data-src')
                    if link:
                        res["img"] = link
                    if res:
                        new_list.append(res)
                    dicts['content'] = new_list

            except Exception as e:
                Logging.logger.error('爬虫中断,进程退出,errmsg:{0}'.format(e))
                return 1

        print("dists", dicts)

        # for table in ls:
        #     res = {}
        #     target = [item.get('target') for item in table if item and item.get('target')]
        #     _break = [item.get('style') for item in table if item and item.get('style') and 'break-word' in item.get('style')]
        #     if 'target="_blank"' in table or "data-copyright" in table or "data-brushtype" in table or "break-word" in table:

        #         # print(table.get('target'))
        #         # print(table.get("data-copyright"))
        #         # print("=====>>>",table.get("data-style-type"))
        #         pass
        #     else:
        #         data = table.get_text()
        #         if data:
        #             # 去除空字符和特殊字符
        #             new_data = "".join(data.split())
        #             new_data = new_data.replace('\ufeff', '')
        #             if new_data != "":
        #                 res["text"] = new_data

        #         link = table.get('data-src')
        #         if link:
        #             res["img"] = link
        #         if res:
        #             new_list.append(res)
        #         dicts['content'] = new_list
        # print("dists",dicts['content'])

