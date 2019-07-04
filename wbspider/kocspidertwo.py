# Author:zcc
# -*- coding:utf-8 -*-
import hashlib
import json
import random
import time
from time import sleep
import lxml.etree
from bs4 import BeautifulSoup
from lxml import *
import requests
from lxml import etree
from selenium import webdriver
import re
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
import logging
from logging.handlers import RotatingFileHandler
from selenium.webdriver.chrome.options import Options

logging.basicConfig(level=logging.DEBUG)
name = "./logs/logtwo%s.txt" % (time.strftime("%Y-%m-%d", time.localtime()))
file_log_handler = RotatingFileHandler(name, maxBytes=1024 * 1024 * 100, backupCount=10)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s')

file_log_handler.setFormatter(formatter)

logging.getLogger().addHandler(file_log_handler)


class Spider(object):
    def __init__(self):
        # userAgent=self.get_userAgent(1)
        try:
            userAgent = self.get_userAgent()
            self.chrome_options = Options()
            self.chrome_options.add_argument('--headless')
            self.chrome_options.add_argument('--disable-gpu')
            self.chrome_options.add_argument(userAgent)
            self.chrome_options.add_argument('lang=zh_CN.UTF-8')
            self.chrome_options.add_argument('--no-sandbox')
            self.driver = ''
            #self.driver = webdriver.Chrome()

            # self.driver = webdriver.PhantomJS(
               # executable_path='/usr/local/lib/python3.5/phantomjs-2.1.1-linux-x86_64/bin/phantomjs', port=34388)
            # self.driver = webdriver.PhantomJS()
            # print(type(111,self.driver))
            # self.driver(executable_path='/usr/local/lib/python3.5/phantomjs-2.1.1-linux-x86_64/bin/phantomjs',port=34388)
        except Exception as e:
            print(e)
            logging.info(e)
            #msg = MIMEText('webdriver初始化错误', 'plain', 'utf-8')

            #self.send_email('william.zhang@maxpr.com.cn', msg)

    def get_userAgent(self, ismy=0):
        userlist = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
            'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
            'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
            'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
            'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
            'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
            'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3'
        ]
        if ismy:
            index = 0
        else:
            index = random.randint(0, len(userlist) - 1)
        return userlist[index]

    def get_ip(self):
        url = 'http://www.xicidaili.com/'
        userAgent = self.get_userAgent(1)

        headers = {"User-Agent": userAgent}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
        str1 = ''
        for child in soup.find(id="ip_list").children:
            str1 += str(child)
        iplist = re.findall(r'\d+.\d+.\d+.\d+', str1)
        ip = str(iplist[random.randint(0, len(iplist) - 1)])
        print(ip)
        return ip
    def format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))
    def send_email(self, to_addr, msg):
        from_addr = "william.zhang@maxpr.com.cn"
        password = "xinnet123A"
        smtp_server = "smtp.maxpr.com.cn"
        msg['From'] = self.format_addr('koc正式爬虫<%s>' % from_addr)
        msg['To'] = self.format_addr('管理员<%s>' % to_addr)
        msg['Subject'] = Header('koc正式爬虫运行状态', 'utf-8').encode()

        server = smtplib.SMTP(smtp_server, 25)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

    def get_data(self, urltype):
        html_data = etree.HTML(self.driver.page_source)
        self.driver.quit()
        if urltype == 1:
            data = {}
            try:
                zf_number = html_data.xpath('//*[@id="app"]/div[1]/div/div[3]/div[1]/div[1]/i[2]/text()')
                com_number = html_data.xpath('//*[@id="app"]/div[1]/div/div[3]/div[1]/div[2]/i[2]/text()')
                zan_number = html_data.xpath('//*[@id="app"]/div[1]/div/div[3]/div[1]/div[3]/i[2]/text()')
                data['zf_number'] = self.change_num(zf_number[0])
                data['comment_number'] = self.change_num(com_number[0])
                data['zan_number'] = self.change_num(zan_number[0])
                return data
            except Exception as e:
                print(e)
                logging.info(e)
               # msg = MIMEText('手机页面爬虫失败', 'plain', 'utf-8')
               # self.send_email('william.zhang@maxpr.com.cn', msg)
                logging.info(e)
                return False
        else:
            data = {}
            try:
                zf_number = html_data.xpath(
                    '//*[@id="plc_main"]/div[1]/div/div/div/div/div[2]/div/ul/li[2]/a/span/span/span/em[2]/text()')
                com_number = html_data.xpath(
                    '//*[@id="plc_main"]/div[1]/div/div/div/div/div[2]/div/ul/li[3]/a/span/span/span/em[2]/text()')
                zan_number = html_data.xpath(
                    '//*[@id="plc_main"]/div[1]/div/div/div/div/div[2]/div/ul/li[4]/a/span/span/span/em[2]/text()')
                data['zf_number'] = self.change_num(zf_number[0])
                data['comment_number'] = self.change_num(com_number[0])
                data['zan_number'] = self.change_num(zan_number[0])
                return data
            except Exception as e:
             #   msg = MIMEText('pc页面爬虫失败', 'plain', 'utf-8')

              #  self.send_email('william.zhang@maxpr.com.cn', msg)
                print(e)
                logging.info(e)
                return False

    def change_num(self, number):
        newnumber = str(number)
        if newnumber.find('万') != -1:
            newnumber = newnumber[:-1]
            data = float(newnumber) * 10000
        elif newnumber.find('亿') != -1:
            newnumber = newnumber[:-1]
            data = float(newnumber) * 100000000
        else:
            data = int(newnumber)
        return data

    def craw(self, root_url, urltype):
        '''try:
            driver = webdriver.PhantomJS(executable_path='/usr/local/lib/python3.5/phantomjs-2.1.1-linux-x86_64/bin/phantomjs',port=34388)
        except Exception as e:
            print(e)
            data = {
            "status": "-1",
            "errmsg": e,
            }
            return jsonify(data)'''
        print(type(self.driver))
        self.driver = webdriver.Chrome(chrome_options= self.chrome_options)
        try:
            self.driver.get(root_url)
            sleep(5)
            data = self.get_data(urltype)
            return data
        except Exception as e:
            self.driver.quit()
            print(e)
            return False

    def save_data(self, data):
        print(data)
        logging.info(data)
        res = requests.post(url="https://koc.pg.com.cn/pySaveUrl", data=data)
        print(111, res)
        print(res.json())
        logging.info(res.json())
        print(res.status_code)
        if res.status_code == 200:
            return True
        else:
            return False

    def get_url(self, page=1):
        data = {
            "pagesize": 1,
            "page": page
        }
        res = requests.post(url='https://koc.pg.com.cn/pyWbUrl',
                            data=data)
        data = res.json()
        print(data)
        logging.info(data)
        if data['status'] == 0:
            urldata = data['data']
            print(urldata)
            crawurl = urldata['url']
            print(crawurl)
            logging.info(crawurl)
            iswb1 = str.find(crawurl, 'https://m.weibo.cn/')
            iswb2 = str.find(crawurl, 'https://weibo.com/')
            if iswb1 != -1:
                urltype = 1
            elif iswb2 != -1:
                urltype = 2
            else:
                urltype = 0
            if urltype:
                data = self.craw(crawurl, urltype)
                if data:
                    print("获取点赞数成功")
                    logging.info("获取点赞数成功")
                    data['id'] = urldata['id']
                    data['errno'] = 0
                    res = self.save_data(data)
                    if res:
                        print("修改成功")
                        logging.info("修改成功")
                    else:
                        print("修改失败")
                        logging.info("修改失败")
                else:
                    data = dict()
                    data['id'] = urldata['id']
                    data['errno'] = -1
                    res = self.save_data(data)
                    if res:
                        print("获取失败修改成功")
                        logging.info("获取失败修改成功")
                    else:
                        print("获取失败修改成功")
                        logging.info("获取失败修改成功")
                    print("获取点赞数失败")
                    logging.info("获取点赞数失败")
            else:
                data = dict()
                data['id'] = urldata['id']
                data['errno'] = -1
                res = self.save_data(data)
                if res:
                    print("链接错误修改成功")
                    logging.info("链接错误修改成功")
                else:
                    print("链接错误修改成功")
                    logging.info("链接错误修改成功")
                print("获取点赞数失败")
                #   msg = MIMEText('链接错误失败', 'plain', 'utf-8')
                #    self.send_email('william.zhang@maxpr.com.cn', msg)
                logging.info("获取点赞数失败")
                self.get_url(page=page + 1)



spider = Spider()
spider.get_url()
