# -*- coding: utf-8 -*-
import scrapy
import json
from datetime import datetime

from shp.items import ShpItem, ShpUserItem, ShpCommentItem


class SpInfoSpider(scrapy.Spider):
    name = 'sp_info'
    allowed_domains = ['weseepro.com']
    url = 'https://www.weseepro.com/api/v1/activity/activities/for/pro?pageIndex={}&pageSize=20&type_uuid=33333333333333333333333333333333'
    page = 1
    start_urls = [url.format(page)]

    detail = "https://www.weseepro.com/api/v1/message/stream/home/{}?pageNumber={}&pageSize=10"

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
            yield scrapy.Request(new_url, callback=self.parse_detail)

        self.page += 1
        url = self.url.format(self.page)
        yield scrapy.Request(url, callback=self.parse)

    def parse_detail(self, response):
        uu = self.handlesUrl(response.url)

        python_dict = json.loads(response.text)
        myFriend = python_dict['data']['messages']
        if len(myFriend) > 0:
            for mfriend in myFriend:
                muuid = mfriend['message_uuid']
                pls = mfriend['follow_messages']
                if len(pls) > 0:
                    for pl in pls:
                        item = ShpCommentItem()
                        # 评论人的名字
                        item['name'] = pl['account']['name']
                        # 评论人的头像头像
                        item['head_image_url'] = pl['account']['head_image_url']
                        # 评论的内容
                        item['content'] = pl['message_text']['content']
                        # 评论图片
                        # item['comment_img'] = pl['message_text']['comment_img']
                        # 信息的ID
                        item['message_uuid'] = muuid
                        # 评论时间
                        item['ctime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        yield item
                else:
                    pass
        else:
            return
        self.page += 1
        url = self.detail.format(uu, self.page)
        yield scrapy.Request(url, callback=self.parse_detail)
