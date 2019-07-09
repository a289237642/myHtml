# -*- coding: utf-8 -*-
import scrapy
import json

from shp.items import ShpItem, ShpUserItem


class SpInfoSpider(scrapy.Spider):
    name = 'sp_info'
    allowed_domains = ['weseepro.com']
    url = 'https://www.weseepro.com/api/v1/activity/activities/for/pro?pageIndex={}&pageSize=20&type_uuid=33333333333333333333333333333333'
    page = 1
    start_urls = [url.format(page)]

    def parse(self, response):
        python_dict = json.loads(response.text)
        myList = python_dict['data']['activities']

        if myList is None:
            return
        for mlist in myList:
            user = ShpUserItem()
            user['name'] = mlist['name']
            user['head_image_url'] = mlist['head_image_url']
            user['message_count'] = ""
            user['description'] = mlist['description']
            user['counts'] = mlist['counts']
            user['introduction'] = mlist['introduction']
            user['industry'] = mlist['industry']
            if mlist['industry'] == '区块链':
                user['industry'] = 2
            elif mlist['industry'] == '创投':
                user['industry'] = 0
            elif mlist['industry'] == '互联网':
                user['industry'] = 1
            elif mlist['industry'] == '财经':
                user['industry'] = 3
            user['activity_uuid'] = mlist['activity_uuid']
            # print(user)
            yield user

        self.page += 1
        url = self.url.format(self.page)
        yield scrapy.Request(url, callback=self.parse)
