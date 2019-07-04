# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmtItem(scrapy.Item):
    title = scrapy.Field()
    thumbnail = scrapy.Field()  # 缩略图
    soure_time = scrapy.Field()  # 原文时间  需要进行转换 2019-07-02 15：05
    author = scrapy.Field()  # 作者
    article = scrapy.Field()  # 文章正文  [{text:""}, {img:""}, {text:""}]
    tags = scrapy.Field()  # 文章分类标签  ['创投']
    unique_timestamp = scrapy.Field()  # 当前时间的时间戳
    show_time = scrapy.Field()  # 爬取时间 需要展示的时间
    create_time = scrapy.Field()  # 创建时间
    web_name = scrapy.Field()  # 网站名称
    source_url = scrapy.Field()  # 详情页的url
