# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings


class ShpPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            db=settings['MYSQL_DBNAME'],
            port=settings['MYSQL_PORT']
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        try:
            self.cursor.execute(
                "insert into user_base(name,head_image_url,description,message_count,introduction,industry,activity_uuid,counts)"
                " values(%s,%s,%s,%s,%s,%s,%s,%s)",
                [item['name'], item['head_image_url'], item['description'], item['message_count'],
                 item['introduction'], item['industry'], item['activity_uuid'],item['counts']])
            self.connect.commit()
        except Exception as error:
            print(error)
        return item

    def close_spider(self, spider):
        self.connect.close();


"""
 self.cursor.execute(
                "insert into user_base(name,head_image_url,description,message_count,introduction,industry,activity_uuid)"
                " values(%s,%s,%s,%s,%s,%s,%s)",
                [item['name'], item['head_image_url'], item['description'], item['message_count'],
                 item['introduction'], item['industry'], item['activity_uuid']])
                 
                 
self.cursor.execute(
                "insert into friends(content,url,activity_uuid,pic,link_type,comment_count,source,add_time)"
                " values(%s,%s,%s,%s,%s,%s,%s,%s)",
                [item['content'], item['url'], item['activity_uuid'], item['pic'], item['link_type'],
                 item['comment_count'], item['source'], item['add_time']])
                
                
self.cursor.execute(
                "insert into aritcle(title,author,atime,tUrl,content,activity_uuid)"
                " values(%s,%s,%s,%s,%s,%s)",
                [item['title'], item['author'], item['atime'], item['tUrl'], item['content'], item['activity_uuid']])
"""
