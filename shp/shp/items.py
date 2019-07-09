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
    # link_type = scrapy.Field()
    forward_count = scrapy.Field()
    # 评论数
    comment_count = scrapy.Field()
    # 点赞
    # source = scrapy.Field()
    thumb_count = scrapy.Field()
    # 朋友圈发布时间
    add_time = scrapy.Field()
    # 分享的链接的封面图
    pic = scrapy.Field()
    # 分享的链接或者图片的地址
    url = scrapy.Field()
    # 图片的url
    img_url = scrapy.Field()
    # 文章的url
    link_url = scrapy.Field()
    # 标题
    ftitle = scrapy.Field()
    activity_uuid = scrapy.Field()
    message_uuid = scrapy.Field()

    # 微信链接
    title = scrapy.Field()  # 标题
    soure_time = scrapy.Field()  # 原文时间  需要进行转换 2019-07-02 15：05
    author = scrapy.Field()  # 作者
    article = scrapy.Field()  # 文章正文  [{text:""}, {img:""}, {text:""}]
    tags = scrapy.Field()  # 文章分类标签  ['创投']
    unique_timestamp = scrapy.Field()  # 当前时间的时间戳
    show_time = scrapy.Field()  # 爬取时间 需要展示的时间
    create_time = scrapy.Field()  # 创建时间
    source_url = scrapy.Field()  # 详情页的url
    is_original = scrapy.Field()  # 是否原创
    web_name = scrapy.Field()


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
    message_uuid = scrapy.Field()


class ShpCommentItem(scrapy.Item):
    # 评论人的名字
    name = scrapy.Field()
    # 评论人的头像头像
    head_image_url = scrapy.Field()
    # 评论的内容
    # fcontent = scrapy.Field()
    # 评论的插图
    comment_img = scrapy.Field()
    # 评论时间
    ctime = scrapy.Field()
    # 评论的内容
    content = scrapy.Field()
    # 信息id
    message_uuid = scrapy.Field()
