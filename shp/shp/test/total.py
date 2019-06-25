# -*- coding: utf-8 -*-
import scrapy
import json
from selenium import webdriver
from lxml import etree

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

    def handleJs(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        htmls = etree.HTML(driver.page_source)

        dicts = {}
        if len(htmls.xpath('//h2[@id="activity-name"]/text()')) > 0:
            dicts['title'] = htmls.xpath(
                '//h2[@id="activity-name"]/text()')[0].strip()
        else:
            dicts['title'] = ""
        if len(htmls.xpath('//*[@id="publish_time"]/text()')) > 0:
            dicts['atime'] = htmls.xpath('//*[@id="publish_time"]/text()')[0]
        else:
            dicts['atime'] = ""
        if len(htmls.xpath('//span[@id="js_author_name"]/text()')) > 0:
            dicts['author'] = htmls.xpath(
                '//span[@id="js_author_name"]/text()')[0]
        else:
            dicts['author'] = ""
        # content=''.join(htmls.xpath('//div[@id="js_content"]/p/span/text()')
        if len(driver.find_element_by_xpath(
                '//div[@id="js_content"]').get_attribute('outerHTML')) > 0:
            dicts['content'] = driver.find_element_by_xpath(
                '//div[@id="js_content"]').get_attribute('outerHTML').replace('\n', '').replace('data-src', 'src')
        else:
            dicts['content'] = ""
        if len(htmls.xpath('//*[@id="js_content"]/p[5]/img/@data-src')) > 0:
            dicts['tUrl'] = htmls.xpath(
                '//*[@id="js_content"]/p[5]/img/@data-src')[0]
        else:
            dicts['tUrl'] = ""
        return dicts

    def parse_detail(self, response):
        python_dict = json.loads(response.text)
        myFriend = python_dict['data']['messages']
        if len(myFriend) == 0:
            return
        else:
            uu = python_dict['data']['messages'][0]['message']['account']['activity_uuid']
            for i in myFriend:
                item = ShpItem()
                if i['message'] is None:
                    return
                else:
                    item['url'] = i['message']['link']['url']
                    if "mp.weixin.qq.com" in i['message']['link']['url']:
                        dicts = self.handleJs(i['message']['link']['url'])
                        item['title'] = dicts['title']
                        item['author'] = dicts['author']
                        item['atime'] = dicts['atime']
                        item['content'] = dicts['content']
                        item['tUrl'] = dicts['tUrl']
                        item['activity_uuid'] = uu

                # print(item)
                yield item
            self.page += 1
            url = self.detail.format(uu, self.page)
            yield scrapy.Request(url, callback=self.parse_detail)
