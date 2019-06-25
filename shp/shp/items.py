# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShpItem(scrapy.Item):
    # 朋友圈
    # #内容
    content = scrapy.Field()
    # 转发数
    link_type = scrapy.Field()
    # 评论数
    comment_count = scrapy.Field()
    # 点赞
    source = scrapy.Field()
    # 朋友圈发布时间
    add_time = scrapy.Field()
    # 分享的链接的封面图
    pic = scrapy.Field()
    # 分享的链接或者图片的地址
    url = scrapy.Field()
    # 标题
    ftitle = scrapy.Field()

    # 微信链接
    # 标题
    title = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 成稿时间
    atime = scrapy.Field()
    # 图片的链接
    tUrl = scrapy.Field()
    # 文章内容
    tcontent = scrapy.Field()
    # activity_uuid
    activity_uuid = scrapy.Field()


class ShpUserItem(scrapy.Item):
    # 姓名
    name = scrapy.Field()
    # 头像
    head_image_url = scrapy.Field()
    # 朋友圈数
    message_count = scrapy.Field()
    # 用户描述
    description = scrapy.Field()
    # 介绍
    introduction = scrapy.Field()
    # 标签
    industry = scrapy.Field()
    # 粉丝
    counts = scrapy.Field()

    # activity_uuid
    activity_uuid = scrapy.Field()
