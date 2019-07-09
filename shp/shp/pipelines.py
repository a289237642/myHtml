# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings
from datetime import datetime


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
        # print("=====>>", item)

        try:
            self.cursor.execute(
                "insert into pl(content,ctime,head_image_url,message_uuid,name)"
                " values(%s,%s,%s,%s,%s)",
                [item['content'], item['ctime'], item['head_image_url'], item['message_uuid'], item['name']])
            self.connect.commit()
        except Exception as error:
            print(error)
        return item

    def close_spider(self, spider):
        self.connect.close();


"""
 self.cursor.execute(
                "insert into dl(activity_uuid,counts,description,head_image_url,industry,introduction,message_count,name)"
                " values(%s,%s,%s,%s,%s,%s,%s,%s)",
                [item['activity_uuid'], item['counts'], item['description'], item['head_image_url'], item['industry'],
                 item['introduction'], item['message_count'], item['name']])
                 
                 
self.cursor.execute(
                "insert into friends(activity_uuid,add_time,comment_count,content,forward_count,ftitle,message_uuid,pic,thumb_count,url)"
                " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                [item['activity_uuid'], item['add_time'], item['comment_count'], item['content'], item['forward_count'],
                 item['ftitle'], item['message_uuid'], item['pic'], item['thumb_count'], item['url']])
  
self.cursor.execute(
                "insert into dt(activity_uuid,add_time,comment_count,content,forward_count,ftitle,message_uuid,pic,thumb_count,url,img_url,link_url)"
                " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                [item['activity_uuid'], item['add_time'], item['comment_count'], item['content'], item['forward_count'],
                 item['ftitle'], item['message_uuid'], item['pic'], item['thumb_count'], item['url'], item['img_url'],
                 item['link_url']])              
                
 self.cursor.execute(
                "insert into aritcle_info(title,author,soure_time,article,source_url,web_name,tags,unique_timestamp,create_time,is_original,show_time)"
                " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                [item['title'], item['author'], item['soure_time'], item['article'], item['source_url'],
                 item['web_name'], item['tags'], item['unique_timestamp'], item['create_time'], item['is_original'],
                 datetime.now()]) 
                 
                

"""
