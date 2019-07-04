# -*- coding: utf-8 -*-
import scrapy, time
from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import logging

loger = logging.getLogger("default_handlers")


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['tmtpost.com']

    start_urls = ['https://www.tmtpost.com/4040455.html']

    def parse(self, response):
        print(response.text)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(response.url)
        dicts = {}
        selector = etree.HTML(driver.page_source)

        zw = driver.find_element_by_xpath('//div[@class="inner"]').get_attribute("outerHTML")
        print(type(zw))
        print("====>>>",zw)

        # title = selector.xpath('//*[@id="activity-name"]/text()')[0]
        # title = "".join(title.split())
        # name = selector.xpath('//*[@id="js_name"]/text()')[0]
        # name = "".join(name.split())
        # spider_time = time.time()
        # date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(spider_time))
        # dicts['title'] = title
        # dicts['name'] = name
        # dicts['date'] = date
        # dicts['web_name'] = name

        # is_original = selector.xpath('//*[@id="copyright_logo"]/text()')
        # if len(is_original) == 0:
        #     dicts['is_original'] = 0  # 不是原创
        # else:
        #     dicts['is_original'] = 1  # 是原创

        # 用xpath取出需要的内容页面部分
        result = selector.xpath('//div[@class="inner"]')
        # 转为html
        content = etree.tostring(result, method='html')
        # 获取bs4对象
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        new_list = []
        # ls = soup.find_all(["p", "img", 'a', 'section'])
        ls = soup.find_all(["p", "img"])
        print(ls)
        # for table in ls:
        #     res = {}
        #     # print(type(table))
        #     try:
        #         target = [item.get('target') for item in table if item and item.get('target')]
        #         _break = [item.get('style') for item in table if
        #                   item and item.get('style') and 'break-word' in item.get('style')]
        #         # print(_break)
        #         if _break:
        #             pass
        #         elif target and target[0] == '_blank':
        #             pass
        #         elif table.get("style") and "break-word" in table.get("style"):
        #             pass
        #         else:
        #             data = table.get_text()
        #             if data:
        #                 # 去除空字符和特殊字符
        #                 new_data = "".join(data.split())
        #                 new_data = new_data.replace('\ufeff', '')
        #                 if new_data != "":
        #                     res["text"] = new_data
        #             link = table.get('data-src')
        #             if link:
        #                 res["img"] = link
        #             if res:
        #                 new_list.append(res)
        #             dicts['content'] = new_list
        #
        #     except Exception as e:
        #         loger.error('爬虫中断,进程退出,errmsg:{0}'.format(e))
        #         return 1
        #
        # print("dists", dicts)
