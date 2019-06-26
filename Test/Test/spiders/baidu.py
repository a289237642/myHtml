# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.options import Options


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['weixin.qq.com']
    start_urls = [
        'https://mp.weixin.qq.com/s?__biz=MzA3NDI3MzMzMQ==&mid=2247485130&idx=1&sn=fe4ba4175900edfb01463467814d9818&scene=4#rd']

    def parse(self, response):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome()
        driver.get(response.url)
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

        # print("=====tit=======>>", tit)
        # print("======mtime=======>>", mtime)
        # print("======author=======>>", author)
        # print("======content=======>>", content)
        # print("======img_url=======>>", img_url)
        print(dicts)
