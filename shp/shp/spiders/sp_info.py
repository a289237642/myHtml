# -*- coding: utf-8 -*-
import scrapy


class SpInfoSpider(scrapy.Spider):
    name = 'sp_info'
    allowed_domains = ['weseepro.com']
    start_urls = ['http://weseepro.com/']

    def parse(self, response):
        pass
