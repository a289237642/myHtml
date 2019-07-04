#Author:zcc
# -*- coding:utf-8 -*-
import json
import random
import re
from time import sleep
import datetime
from pymysql import connect
import lxml.etree
import soup as soup
from bs4 import BeautifulSoup
from lxml import *
import requests
from lxml import etree
from pymongo import MongoClient
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver




class Spider(object):
    def __init__(self):
        userAgent=self.get_userAgent(1)
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        self.cookie={
            'value':'oid%3D4269031915999301%26lfid%3D102803%26luicode%3D20000174%26uicode%3D20000174',
            'name':'',
            'path':'/',
            'domain':'.weibo.cn',
            'expires':None
        }
        '''
        {'domain': '.weibo.cn', 'expires': '周日, 09 9月 2018 01:38:01 GMT', 'expiry': 1536457081, 'httponly': False, 'name': '_T_WM', 'path': '/', 'secure': False, 'value': '3f2a5b8f09e19eecaf9fee130dc4e90c'}]
        '''
        dcap["phantomjs.page.settings.userAgent"] = (userAgent)
        self.driver = webdriver.PhantomJS(executable_path='/usr/local/lib/python3.5/phantomjs-2.1.1-linux-x86_64/bin/phantomjs',port=34388)  # desired_capabilities=dcap
        # self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')  # desired_capabilities=dcap
        # self.driver = webdriver.Firefox() # desired_capabilities=dcap

    def get_userAgent(self,ismy=0):
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
            index=0
        else:
            index=random.randint(0,len(userlist)-1)
        return userlist[index]

    def get_ip(self):
        url = 'http://www.xicidaili.com/'
        userAgent = self.get_userAgent(1)

        headers = {"User-Agent":userAgent}
        r= requests.get(url,headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
        str1=''
        for child in soup.find(id="ip_list").children:
            str1+=str(child)
        iplist = re.findall(r'\d+.\d+.\d+.\d+',str1)
        ip = str(iplist[random.randint(0,len(iplist)-1)])
        print(ip)
        return ip


    def craw(self,root_url):


        self.driver.set_window_size(1240, 900)
        self.driver.get(root_url)
        sleep(2)

        # self.driver.execute_script("")
        # self.driver.execute_script("")
        # self.driver.execute_script("")
        # self.driver.execute_script("")
        # self.driver.execute_script("")
        # self.driver.execute_script("")

        # js = "var currentPosition,timer;function GoTop(){timer=setInterval("+"runToTop()"+",1);}function runToTop(){currentPosition=document.documentElement.scrollTop || document.body.scrollTop; currentPosition-=10;if(currentPosition>0){window.scrollTo(0,currentPosition);}else{window.scrollTo(0,0);clearInterval(timer);}}"

        # lastHeight = self.driver.execute_script("return document.body.scrollHeight")
        # self.driver.execute_script("var q=document.documentElement.scrollTop=%s" %lastHeight)
        self.driver.execute_script("""   
                (function () {   
                    var y = document.body.scrollTop;   
                    var step = 200;   
                    window.scroll(0, y);   


                    function f() {   
                        if (y < document.body.scrollHeight) {   
                            y += step;   
                            window.scroll(0, y);   
                            setTimeout(f, 700);   
                        }  
                        else {   
                            window.scroll(0, y);   
                            document.title += "scroll-done";   
                        }   
                    }   


                    setTimeout(f, 1000);   
                })();   
                """)

        # self.driver.execute_script(js)
        # print(lastHeight)
        # return False
        sleep(20)
        # sleep(15)

        # 获取数据
        data = self.get_div()
        return True


    def get_div(self):
        html_data = etree.HTML(self.driver.page_source)
        divs = html_data.xpath('//*[@id="app"]/div/div/div/div/div[1]/div/div/div[3]/div[2]/div/div/div[1]/div/ul/li/div[@class="am-cf inner_li"]')
        list=[]
        i=0
        for div in divs:
            data,title,name,min_pic,summary,date,url = self.get_data(div)

            if data:
                i = i + 1
                print(i)
                # 存储数据
                res = self.save_data(data,title,name,min_pic,summary,date,url)
                if res:
                    list.append(data)
                else:
                    break
            else:
                data=[]


        # print("一共爬取了%s篇文章" % i)
        # print(list)
        self.driver.quit()
        return data
    def save_data(self,data,title,name,min_pic,summary,date,url):
        myclient = MongoClient("mongodb://47.100.63.158:27017/")

        # myclient = MongoClient("mongodb://localhost:27017/")
        mydb = myclient["wechat"]
        # mydb = myclient["will"]
        mycol = mydb["articles"]

        datalist = myclient.wechat.articles.find_one({'name': name, 'title': title})
        if datalist:
            print(99999999)
            return False
        else:
            mydict = data
            x = mycol.insert_one(mydict)
            print(x)

            conn = connect(host="rm-uf6gw23j409s5ui7qmoo.mysql.rds.aliyuncs.com",port=3306,user= "maxpr_mysql",
                                 password="COFdjwD*$*m8bd!HtMLP4+Az0eE9m", database="zjlivenew", charset='utf8')
            cs1 = conn.cursor()
            now = datetime.datetime.now()
            headimg='https://cdn.max-digital.cn/gander_goose/dev/test2/15368084853514.jpg'
            sql1 = "insert into zj_article_info(title,summary,author,min_pic,web_name,wechat_art_date,is_show,is_big,link,round_head_img,create_time) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (title,summary,name,min_pic,"36氪",date,0,0,url,headimg,now)
            cs1.execute(sql1)
            # 获取最新插入的文章的ID
            new_article_id = int(conn.insert_id())

            # 修改分类--24小时下文章的自定义排序值
            # sql2 = 'update zj_article_group set sort_num = sort_num + 1 where group_id=1'
            # cs1.execute(sql2)

            # 上线到24小时分类
            sql3 = 'insert into zj_article_group (article_id,group_id,sort_num,create_time) values ("%s", "%s", "%s", "%s")' % (new_article_id, 1, 1, now)
            cs1.execute(sql3)

            # 修改上线文章状态
            sql4 = "update zj_article_info set is_show=1, zj_art_date='%s' where id='%s'" % (now, new_article_id)
            cs1.execute(sql4)

            conn.commit()
            cs1.close()
            db.close()
            return x



    def get_data(self,div):
        try:
            title = div.xpath('./a/div[2]/h3/text()')
            desc = div.xpath('./a/div[2]/div/text()')
            author = div.xpath('./div/div[1]/div[1]/a/text()')
            date = div.xpath('./div/div[1]/div[2]/span[1]/@title')
            main_img = div.xpath('./a/div[1]/div/img/@src')
            url = div.xpath('./a/@href')
            data = {}
            # print(title[0])
            # print(desc[0])
            # print(author[0])
            # print(date[0])

            data['title'] = title[0]
            data['web_name'] = '36氪'
            data['summary'] = desc[0]
            data['name'] = author[0]
            data['date'] = date[0]
            # print(1111,title[0])
            # print(2222,desc[0])
            # print(3333,author[0])
            # print(4444,date[0])
            # print(5555,main_img[0])
            data['min_pic']=self.upload(main_img[0])

            # data['main_img']=main_img[0]

            # print(data)

            url = "https://36kr.com" + url[0]
            data['url'] = url
            content = self.getarticle_content(url)
            # return data
            if content:
                data['content'] = content
                print('66666666666')
                # print(data)
                return data,title[0],author[0],data['min_pic'],data['summary'],data['date'],url
            else:
                return False,False,False,False,False,False,False
        except Exception as e:
            print(e)
            return False, False, False,False,False,False,False

        # with open('36ke.html', 'r') as f:
        #     html_data=f.read()
        # # f.write(self.driver.page_source)
        # html_data = etree.HTML(html_data)
        # divs = html_data.xpath('//*[@id="app"]/div/div/div/div/div[1]/div/div/div[3]/div[2]/div/div/div[1]/div/ul/li/div[@class="am-cf inner_li"]')
        # for div in divs:


    def getarticle_content(self,url):
        print(url)
        self.driver.get(url)
        sleep(5)
        page = self.driver.page_source
        # html = open('77.html', 'r')
        # data = pq(html)
        print(11111)

        soup = BeautifulSoup(page, 'html.parser', from_encoding='utf-8')
        # print("文章详情页面获取成功")
        # print(soup)
        # html_data = etree.HTML(self.driver.page_source)
        # div = html_data.xpath('//*[@id="J_post_wrapper_5149034"]/div[1]/div/div[2]/section[1]')
        arrlist = []
        print(22222)

        for child in soup.find(class_="textblock").children:
            if child.string == None:
                try:
                    str2=''
                    for child in child.children:
                        if child.name == 'img':
                            arrlist.append({'img': child.attrs['src']})
                            # arrlist.append({'image': child.attrs['src']})
                        else:
                            if child.string != None:
                                str2+=child.string
                                # print('1111'+child.string)
                                # arrlist.append({'text': child.string})
                            elif child.name == 'img':
                                arrlist.append({'img': child.attrs['src']})
                                # arrlist.append({'image': child.attrs['src']})
                            else:
                                str1 = ''
                                for child in child.children:
                                    if child.string != None:
                                        # print('2222' + child.string)
                                        str1 += child.string
                                    elif child.name == 'img':
                                        arrlist.append({'img': child.attrs['src']})
                                        # arrlist.append({'image': child.attrs['src']})
                                    else:
                                        for child in child.children:
                                            if child.string != None:
                                                str1+=child.string
                                                # print("+++++++" + child.string)
                                                # list.append({'text': child.string})
                                            elif child.name == 'img':
                                                arrlist.append({'img': child.attrs['src']})
                                                # arrlist.append({'image': child.attrs['src']})
                                            else:
                                                for child in child.children:
                                                    if child.string != None:
                                                        arrlist.append({'text': child.string})
                                                    elif child.name == 'img':
                                                        arrlist.append({'img': child.attrs['src']})
                                                        # arrlist.append({'image': child.attrs['src']})
                                if str1 != '' or str1 != '\n':
                                    arrlist.append({'text': str1})
                    if str2 != '' or str2 != '\n':
                        arrlist.append({'text': str2})
                except Exception as e:
                    # print('该元素没有子节点')
                    print(11)
                    # print(child.string)
                    # print(child)

            else:
                print(33333)
                if child.name=='img':
                    arrlist.append({'img': child.attrs['data-src']})
                elif child.string != '' or child.string != '\n':
                    # print('3333'+child.string)
                    arrlist.append({'text': child.string})


        newlist = []
        for item in arrlist:
            if list(item.keys())[0] == 'img':
                item['img']=self.upload(item['img'])
                newlist.append(item)
            else:

                data = item.get('text')
                if data!='':
                    newlist.append(item)

                # pattern = re.compile(r'&(.*?);|\s|  ')
                # new_data = pattern.sub("", data)
                # new_data = new_data.replace(u'\ufeff', '')
                # item['text'] = new_data
                #
                #
                # if list(item.values())[0] != '':
                #     newlist.append(item)

        return newlist






    def upload(self,file_url):
        url = 'http://api.max-digital.cn/Api/oss/uploadByUrl'

        file_path = 'miniprogram/zjlive/download/image'
        params = {
            'fileurl': file_url,
            'filepath': file_path,
        }
        data = requests.post(url=url, data=params)

        data = data.json()
        print(123, json.dumps(data, ensure_ascii=False))

        if data.get('code') == 'OK':
            url=data.get('oss_file_url')
            oss_url = url.replace('maxpr.oss-cn-shanghai.aliyuncs.com', 'cdn.max-digital.cn')
            new = oss_url.replace('http','https')
            return new
            # return data.get('oss_file_url')
        else:
            # 表示上传失败
            return False
            raise Exception("上传失败")





#spider =Spider()
#url = 'http://36kr.com/'
#spider.craw(url)


# myclient = MongoClient("mongodb://47.100.63.158:27017/")
# # dblist = myclient.database_names()
# mydb = myclient["william"]
# mycol = mydb["articles"]
# if "william" in dblist:
#     print("数据库已存在！")
