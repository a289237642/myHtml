# -*- coding: utf-8 -*-
import scrapy
import time, re
import json
from Tmt.items import TmtItem
from datetime import datetime
from bs4 import BeautifulSoup


class MsgInfoSpider(scrapy.Spider):
    name = 'msg_info'
    allowed_domains = ['tmtpost.com']
    url = 'https://www.tmtpost.com/column/3189960/{}'
    page = 1
    start_urls = [url.format(page)]

    def parse(self, response):

        if self.page > 10:
            return
        mlists = response.xpath('//div[@class="mod-article-list clear"]/ul/li')
        for dd in mlists:
            item = TmtItem()
            if len(dd.xpath('./div[1]/h3/a/text()')) > 0:
                item['title'] = dd.xpath('./div/h3/a/text()').extract()[0].replace("\n", "").strip()
            else:
                item['title'] = ""
            item['thumbnail'] = dd.xpath('./div[2]/a/img/@src').extract()[0]

            detail_url = "https://www.tmtpost.com" + dd.xpath('./div[2]/a/@href').extract()[0]
            yield scrapy.Request(detail_url, callback=self.parse_detail, dont_filter=True, meta={"item": item})

        self.page += 1
        url = self.url.format(self.page)
        yield scrapy.Request(url, callback=self.parse)

    def parse_detail(self, response):
        item = response.meta['item']
        item['author'] = response.xpath('//a[@class="color-orange"]/text()').extract()[0].replace("\n", "").strip()
        article = response.xpath('//div[@class="inner"]/p').extract()
        article = self.hanlde_text(article)
        # print(article)
        item['article'] = json.dumps(article, ensure_ascii=False)
        item['soure_time'] = response.xpath('//span[@class="time"]/text()|//span[@class="time "]/text()').extract()[0]
        item['tags'] = '深度解析'
        item['web_name'] = '钛媒体'
        item['source_url'] = response.url
        item['create_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        item['unique_timestamp'] = time.time()
        # print(item)
        yield item

    def hanlde_text(self, article):
        new_l = []
        for p in article:
            item = dict()
            text = BeautifulSoup(p, features="lxml").get_text()
            if text:
                item['text'] = text.replace("\xa0", "")
            ic = "$$".join(re.findall("src=\"(.*?)\"", p))
            if ic:
                item['img'] = ic
            if not item:
                pass
            else:
                new_l.append(item)
        return new_l[:-2]
