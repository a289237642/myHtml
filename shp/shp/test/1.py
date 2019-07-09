# -*- coding: utf-8 -*-
import scrapy
import json
from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.options import Options

from shp.items import ShpItem, ShpUserItem


class SpInfoSpider(scrapy.Spider):
    name = 'sp_info'
    allowed_domains = ['weseepro.com']
    url = 'https://www.weseepro.com/api/v1/activity/activities/for/pro?pageIndex={}&pageSize=20&type_uuid=289e724e0cf84800876588e2e4e3bf96'
    page = 1
    start_urls = [url.format(page)]

    detail = "https://www.weseepro.com/api/v1/message/stream/home/{}?pageNumber={}&pageSize=10"

    def parse(self, response):
        python_dict = json.loads(response.text)
        myList = python_dict['data']['activities']
        # 爬虫结束条件
        if myList is None:
            return
        for mlist in myList:
            new_url = self.detail.format(mlist['activity_uuid'], self.page)
            yield scrapy.Request(new_url, callback=self.parse_detail)

        self.page += 1
        url = self.url.format(self.page)
        yield scrapy.Request(url, callback=self.parse)

    def handleJs(self,url):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome()
        driver.get(url)
        htmls = etree.HTML(driver.page_source)

        dicts = {}
        if len(htmls.xpath('//h2[@id="activity-name"]/text()')) > 0:
            dicts['tit'] = htmls.xpath(
                '//h2[@id="activity-name"]/text()')[0].strip()
        else:
            dicts['tit'] = ""
        if len(htmls.xpath('//*[@id="publish_time"]/text()')) > 0:
            dicts['mtime'] = htmls.xpath('//*[@id="publish_time"]/text()')[0]
        else:
            dicts['mtime'] = ""
        if len(htmls.xpath('//span[@id="js_author_name"]/text()')) > 0:
            dicts['author'] = htmls.xpath(
                '//span[@id="js_author_name"]/text()')[0]
        else:
            dicts['author'] = ""
        # content=''.join(htmls.xpath('//div[@id="js_content"]/p/span/text()')
        if len(driver.find_element_by_xpath(
                '//div[@id="js_content"]').get_attribute('outerHTML')) > 0:
            dicts['content'] = driver.find_element_by_xpath(
                '//div[@id="js_content"]').get_attribute('outerHTML')
        else:
            dicts['content'] = ""
        if len(htmls.xpath('//*[@id="js_content"]/p[5]/img/@data-src')) > 0:
            dicts['img_url'] = htmls.xpath(
                '//*[@id="js_content"]/p[5]/img/@data-src')[0]
        else:
            dicts['img_url'] = ""


    def parse_detail(self, response):
        python_dict = json.loads(response.text)
        user = ShpUserItem()
        userInfo = python_dict['data']['activity']
        if userInfo:
            user['name'] = userInfo['name']
            user['head_image_url'] = userInfo['head_image_url']
            user['message_count'] = userInfo['message_count']
            user['description'] = userInfo['description']
            user['introduction'] = userInfo['introduction']
            user['industry'] = userInfo['industry']
            print("=====user===", user)

        # myFriend = python_dict['data']['messages']
        # if len(myFriend) != 0:
        #     uu = python_dict['data']['messages'][0]['message']['account']['activity_uuid']
        #     for i in myFriend:
        #         item = ShpItem()
        #         if i['message'] is None:
        #             return
        #         else:
        #             if i['message']['message_text']['content'] is None:
        #                 item['content'] = ""
        #             item['content'] = i['message']['message_text']['content']
        #             kbool = "link" in i['message'].keys()
        #             if kbool is False:
        #                 item['pic'] = ""
        #                 item['url'] = ""
        #             else:
        #                 picbool = "pic" in i['message']['link'].keys()
        #
        #                 if picbool != False:
        #                     item['pic'] = i['message']['link']['pic']
        #                 else:
        #                     item['pic'] = ""
        #                 bool = "mp.weixin.qq.com" in i['message']['link']['url']
        #                 if bool is True:
        #                     pass
        #                 else:
        #                     item['url'] = ""
        #
        #         print(item)
        #     self.page += 1
        #     url = self.detail.format(uu, self.page)
        #     yield scrapy.Request(url, callback=self.parse_detail)

#https://resource-insight.newrank.cn/insight/android/2019/07/03/262bcfa9f5916f8abad0ace22d2cfda3.jpg?width=1080&height=2338
