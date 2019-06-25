# -*- coding: utf-8 -*-
import scrapy
import json
from selenium import webdriver
from lxml import etree

from shp.items import ShpItem, ShpUserItem


class SpInfoSpider(scrapy.Spider):
    name = 'sp_info'
    allowed_domains = ['weseepro.com']
    url = 'https://www.weseepro.com/api/v1/activity/activities/for/pro?pageIndex={}&pageSize=20&type_uuid=22222222222222222222222222222222'
    page = 1
    start_urls = [url.format(page)]

    detail = "https://www.weseepro.com/api/v1/message/stream/home/{}?pageNumber={}&pageSize=10"

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

        # 寻找activity_uuid

    def handlesUrl(self, url):
        return url.split("/")[-1].split("?")[0]

    def parse(self, response):
        python_dict = json.loads(response.text)
        myList = python_dict['data']['activities']
        # 爬虫结束条件
        if myList is None:
            return
        for mlist in myList:
            new_url = self.detail.format(mlist['activity_uuid'], self.page)
            yield scrapy.Request(new_url, callback=self.parse_detail, )

        self.page += 1
        url = self.url.format(self.page)
        yield scrapy.Request(url, callback=self.parse)

    def parse_detail(self, response):
        uu = self.handlesUrl(response.url)

        python_dict = json.loads(response.text)
        myFriend = python_dict['data']['messages']
        null = 0  # myself
        if len(myFriend) == 0:
            return
        else:
            for i in myFriend:
                item = ShpItem()
                if i['message'] is None:
                    return
                else:
                    item['add_time'] = i['message']['message_text']['add_time']
                    item['content'] = i['message']['message_text']['content'].replace('\n', "")
                    item['activity_uuid'] = uu

                    if i['message']['message_text']['add_time'] is null:
                        item['add_time'] = ""
                    else:
                        item['add_time'] = i['message']['message_text']['add_time']
                    if 'source' not in i['message']['message_text'].keys():
                        item['source'] = ""
                    else:
                        item['source'] = i['message']['message_text']['source']

                    if 'link_type' not in i['message']['message_text'].keys():
                        item['link_type'] = ""
                    else:
                        item['link_type'] = i['message']['message_text']['link_type']

                    if 'comment_count' not in i['message']['message_text'].keys():
                        item['comment_count'] = ""
                    else:
                        item['comment_count'] = i['message']['message_text']['comment_count']

                    if i['message']['link'] is not null or 'link' in i['message'].keys():
                        picList = list(i.keys())
                        for j in picList:
                            if 'pic' != j or 'link' not in i.keys():
                                item['pic'] = ""
                            else:
                                item['pic'] = i['message']['link']['pic']

                        if i['message']['link'] is null or 'title' not in i['message']['link'].keys():
                            item['ftitle'] = ""
                        elif i['message']['link'] is not null or 'title' in i['message']['link'].keys():
                            item['ftitle'] = i['message']['link']['title']
                        if 'url' not in i['message']['link'].keys():
                            item['url'] = ""
                        else:
                            item['url'] = i['message']['link']['url']
                    elif i['message']['link'] is null or 'link' not in i['message'].keys():
                        item['pic'] = ""
                        item['ftitle'] = ""
                        item['url'] = ""

                print(item)
                # yield item
        self.page += 1
        url = self.detail.format(uu, self.page)
        yield scrapy.Request(url, callback=self.parse_detail)


# //img[@data-ratio][not(@data-copyright)]//@src
