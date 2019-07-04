# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo, pymysql
from scrapy.conf import settings
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine


class TmtPipeline(object):
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
                "insert into aritcle_info(title,thumbnail,soure_time,author,article,tags,unique_timestamp,show_time,create_time,web_name,source_url)"
                " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                [item['title'], item['thumbnail'], item['soure_time'], item['author'], item['article'],
                 item['tags'], item['unique_timestamp'], datetime.now(), item['create_time'], item['web_name'],
                 item['source_url']])
            self.connect.commit()
        except Exception as error:
            print(error)
        return item

    def close_spider(self, spider):
        self.connect.close();

# class TmtPipeline(object):
#     def __init__(self):
#         print("=====start=====")
#         host = settings['MYSQL_HOST'],
#         user = settings['MYSQL_USER'],
#         passwd = settings['MYSQL_PASSWORD'],
#         db = settings['MYSQL_DBNAME'],
#         port = settings['MYSQL_PORT']
#         self.engine = create_engine("mysql+pymysql://%s:%s@%s:%s/%s" % (user, passwd, host, port, db),
#                                     encoding='utf8', echo=True)
#         # host = settings["MONGO_HOST"]
#         # port = settings["MONGO_PORT"]
#         # dbname = settings["MONGO_DBNAME"]
#         # sheetname = settings["MONGO_SHEETNAME"]
#         # # engine =
#         # print("host==", host)
#         # print("port==", port)
#         # print("dbname==", dbname)
#         # print("sheetname==", sheetname)
#
#         # 创建客户端
#         # client = pymongo.MongoClient(host=host, port=port)
#         # # 得到或者创建数据库对象
#         # mydb = client[dbname]
#         # # 得到或者创建表
#         # self.post = mydb[sheetname]
#
#     def process_item(self, item, spider):
#         dict_item = dict(item)
#         try:
#             # print(dict_item)
#             pf = pd.DataFrame(dict_item,  index=[0])
#             pf.to_sql("test", con=self.engine, if_exists='append')
#             # self.post.insert(dict_item)
#         except Exception as e:
#             print('e', e)
#         return item
#     #
#     # def close_spider(self, spider):
#     #     print("======end======")
#     #     self.file.close()
