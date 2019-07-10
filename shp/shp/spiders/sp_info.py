import scrapy
import json

from shp.items import ShpItem, ShpUserItem


class SpInfoSpider(scrapy.Spider):
    name = 'sp_info'
    allowed_domains = ['weseepro.com']
    url = 'https://www.weseepro.com/api/v1/activity/activities/for/pro?pageIndex={}&pageSize=20&type_uuid=88888888888888888888888888888888'
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
                item = ShpItem()
                # 添加时间
                if mfriend['message']['message_text']['add_time'] is not None:
                    item['add_time'] = mfriend['message']['message_text']['add_time']
                else:
                    item['add_time'] = "2019-06-01 00:00:00"

                # 内容
                if 'content' in mfriend['message']['message_text'].keys():
                    item['content'] = mfriend['message']['message_text']['content'].replace('\n', "")
                else:
                    item['content'] = ""

                # 人物activity_uuid
                item['activity_uuid'] = uu

                # 信息的message_uuid
                item['message_uuid'] = mfriend['message_uuid']

                # 点赞数
                if 'source' in mfriend['message']['message_text']:
                    item['thumb_count'] = mfriend['message']['message_text']['source']
                else:
                    item['thumb_count'] = 0

                # 转发数
                if 'link_type' in mfriend['message']['message_text'].keys():
                    item['forward_count'] = mfriend['message']['message_text']['link_type']
                else:
                    item['forward_count'] = 0

                # 评论数
                if 'comment_count' in mfriend['message']['message_text'].keys():
                    item['comment_count'] = mfriend['message']['message_text']['comment_count']
                else:
                    item['comment_count'] = 0

                # 分享的链接的封面图
                if 'link' not in mfriend['message'].keys():
                    item['pic'] = ""
                else:
                    if mfriend['message']['link'] is None:
                        item['pic'] = ""
                    elif 'pic' not in mfriend['message']['link'].keys():
                        item['pic'] = ""
                    else:
                        item['pic'] = mfriend['message']['link']['pic']

                # 标题
                if 'link' not in mfriend['message'].keys():
                    item['ftitle'] = ""
                elif mfriend['message']['link'] is None:
                    item['ftitle'] = ""
                elif 'title' not in mfriend['message']['link'].keys():
                    item['ftitle'] = ""
                else:
                    item['ftitle'] = mfriend['message']['link']['title']

                # 分享的链接或者图片的地址
                if 'link' not in mfriend['message'].keys():
                    item['url'] = ""
                    item['img_url'] = ""
                    item['link_url'] = ""
                elif mfriend['message']['link'] is None:
                    item['url'] = ""
                    item['img_url'] = ""
                    item['link_url'] = ""
                elif 'url' not in mfriend['message']['link'].keys():
                    item['url'] = ""
                    item['img_url'] = ""
                    item['link_url'] = ""
                else:
                    url = mfriend['message']['link']['url']
                    if ".jpg" in url or ".png" in url:
                        item['img_url'] = url
                        item['link_url'] = ""
                    else:
                        item['img_url'] = ""
                        item['link_url'] = url
                    item['url'] = url

                # print(item)
                yield item
        else:
            return

        self.page += 1
        url = self.detail.format(uu, self.page)
        yield scrapy.Request(url, callback=self.parse_detail)
