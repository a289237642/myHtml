# -*- coding: utf-8 -*-
import scrapy, time
from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from scrapy_splash import SplashRequest
import logging
from urllib import request
import json
from urllib import request, parse

loger = logging.getLogger("default_handlers")


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['weixin.qq.com']

    # allowed_domains = ['jandan.net']

    # start_urls = [
    #     'https://mp.weixin.qq.com/s?__biz=MzU5MzU4OTczMA==&mid=2247515475&idx=1&sn=9f492dce7a42993c148ff570a3156c40&chksm=fe0cd9dec97b50c86b68688ac33e3d6d498ef3b796e868872e09b1ff463e8f618dfbada16c68#rd'
    # ]

    def start_requests(self):
        script = '''
        			function main(splash)
        				splash:set_viewport_size(1028, 10000)
        				splash:go(splash.args.url)
        				local scroll_to = splash:jsfunc("window.scrollTo")
        				scroll_to(0, 2000)
        				splash:wait(3)

        				return { 
        					html = splash:html() 
        				}
        			end
        				'''
        url = 'https://mp.weixin.qq.com/s?__biz=MzU5MzU4OTczMA==&mid=2247515475&idx=1&sn=9f492dce7a42993c148ff570a3156c40&chksm=fe0cd9dec97b50c86b68688ac33e3d6d498ef3b796e868872e09b1ff463e8f618dfbada16c68#rd'

        yield SplashRequest(url, callback=self.parse, meta={
            'dont_redirect': True,
            'splash': {
                'args': {
                    'lua_source': script
                },
                'endpoint': 'execute',
            }
        })
        t_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    def handles_fy(self,soure_time):
        # 打开有道在线翻译，输入girl，检查，找到headers,复制里面的网址
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

        # 将网页中的Form Data中的所有数据复制出来
        # 通过调试发现，只需要其中的i对应要翻译的内容和doctype对应的数据格式
        formdata = {
            'i': soure_time,
            'doctype': 'json',
        }

        # formdata中的数据需要转换为bytes格式
        data = parse.urlencode(formdata).encode()

        # 将网页中的请求头Request Headers中的数据复制出来,只需要一个用户代理即可
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71',
        }

        # 请求网页
        req = request.Request(url=url, data=data, headers=headers)

        # 返回网页
        res = request.urlopen(req)

        # 下载导出数据
        result = json.loads(res.read())
        return result["translateResult"][0][0]["tgt"]


    def parse(self, response):
        dicts = {}

        # dicts['title'] = response.xpath('//*[@id="activity-name"]/text()').extract()[0].replace("\n", "").strip()
        # dicts['web_name'] = response.xpath('//*[@id="js_name"]/text()').extract()[0].replace("\n", "").strip()
        # if len(response.xpath('//span[@id="js_author_name"]/text()|//a[@id="js_name"]/text()')) > 0:
        #     dicts['author'] = response.xpath('//span[@id="js_author_name"]/text()|//a[@id="js_name"]/text()').extract()[
        #         0].replace("\n", "").strip()
        # else:
        #     dicts['author'] = ""
        # if response.xpath('//*[@id="copyright_logo"]/text()').extract()[0].replace(":", "") == 'Original':
        #     dicts['is_original'] = 1
        # else:
        #     dicts['is_original'] = 0
        # # dicts['is_original'] = response.xpath('//*[@id="copyright_logo"]/text()').extract()[0].replace(":", "")
        # if len(response.xpath('//em[@id="publish_time"]/text()')) > 0:
        #     dicts['soure_time'] = response.xpath('//em[@id="publish_time"]/text()').extract()[0]
        # else:
        #     dicts['soure_time'] = ""
        # dicts['article'] = response.xpath('//*[@id="js_content"]/p')
        # print(dicts)

        selector = etree.HTML(response.text)
        # 标题
        if len(selector.xpath('//*[@id="activity-name"]/text()')) > 0:
            title = selector.xpath('//*[@id="activity-name"]/text()')[0]
            title = "".join(title.split())
        else:
            title = ""
        # 网站来源
        if len(selector.xpath('//*[@id="js_name"]/text()')) > 0:
            web_name = selector.xpath('//*[@id="js_name"]/text()')[0]
            web_name = "".join(web_name.split())
        else:
            web_name = ""
        # 作者
        if len(selector.xpath(
                '//span[@id="js_author_name"]/text()|//span[@class="rich_media_meta rich_media_meta_text"]/text()')) > 0:
            author = selector.xpath(
                '//span[@id="js_author_name"]/text()|//span[@class="rich_media_meta rich_media_meta_text"]/text()')[
                0].replace("\n", "").strip()
        else:
            author = ""
        is_original = selector.xpath('//*[@id="copyright_logo"]/text()')
        if len(is_original) == 0:
            dicts['is_original'] = 0  # 不是原创
        else:
            dicts['is_original'] = 1  # 是原创

        if len(selector.xpath('//em[@id="publish_time"]/text()')) > 0:
            soure_time = selector.xpath('//em[@id="publish_time"]/text()')[0]
            soure_time=self.handles_fy(soure_time)
        else:
            soure_time = ""




        spider_time = time.time()
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(spider_time))
        dicts['title'] = title
        dicts['author'] = author
        dicts['date'] = date
        dicts['web_name'] = web_name
        dicts['soure_time'] = soure_time

        is_original = selector.xpath('//*[@id="copyright_logo"]/text()')
        if len(is_original) == 0:
            dicts['is_original'] = 0  # 不是原创
        else:
            dicts['is_original'] = 1  # 是原创

        # 用xpath取出需要的内容页面部分
        result = selector.xpath('//*[@id="js_content"]')[0]
        # 转为html
        content = etree.tostring(result, method='html')
        # 获取bs4对象
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        new_list = []
        # ls = soup.find_all(["p", "img", 'a', 'section'])
        ls = soup.find_all(["p", "img"])
        for table in ls:
            res = {}
            try:

                target = [item.get('target') for item in table if item and item.get('target')]
                # if len(target) > 0:
                _break = [item.get('style') for item in table if
                          item and item.get('style') and 'break-word' in item.get('style')]
                if _break:
                    pass
                elif target and target[0] == '_blank':
                    pass
                elif table.get("style") and "break-word" in table.get("style"):
                    pass
                else:
                    data = table.get_text()
                    if data:
                        # 去除空字符和特殊字符
                        new_data = "".join(data.split())
                        new_data = new_data.replace('\ufeff', '')
                        if new_data != "":
                            res["text"] = new_data
                    link = table.get('data-src')
                    if link:
                        res["img"] = link
                    if res:
                        new_list.append(res)
                    dicts['article'] = new_list

            except Exception as e:
                return 1

        print(dicts)

        # dd = self.hanlde_text(dicts['article'])
        # print(dd)

    # def hanlde_text(self, article):
    #     new_l = []
    #     for p in article:
    #         item = dict()
    #         text = BeautifulSoup(p, features="lxml").get_text()
    #         if text:
    #             item['text'] = text.replace("\xa0", "")
    #         ic = "$$".join(re.findall("src=\"(.*?)\"", p))
    #         if ic:
    #             item['img'] = ic
    #         if not item:
    #             pass
    #         else:
    #             new_l.append(item)
    #     return new_l[:-2]

    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver.get(response.url)
    # dicts = {}
    # selector = etree.HTML(driver.page_source)
    # # 标题
    # if len(selector.xpath('//*[@id="activity-name"]/text()')) > 0:
    #     title = selector.xpath('//*[@id="activity-name"]/text()')[0]
    #     title = "".join(title.split())
    # else:
    #     title = ""
    # # 网站来源
    # if len(selector.xpath('//*[@id="js_name"]/text()')) > 0:
    #     web_name = selector.xpath('//*[@id="js_name"]/text()')[0]
    #     web_name = "".join(web_name.split())
    # else:
    #     web_name = ""
    # # 作者
    # if len(selector.xpath('//span[@id="js_author_name"]/text()')) > 0:
    #     author = selector.xpath('//span[@id="js_author_name"]/text()')[0]
    # else:
    #     author = ""
    # is_original = selector.xpath('//*[@id="copyright_logo"]/text()')
    # if len(is_original) == 0:
    #     dicts['is_original'] = 0  # 不是原创
    # else:
    #     dicts['is_original'] = 1  # 是原创
    #
    # if len(selector.xpath('//em[@id="publish_time"]/text()')) > 0:
    #     soure_time = selector.xpath('//em[@id="publish_time"]/text()')[0]
    # else:
    #     soure_time = ""
    #
    # spider_time = time.time()
    # date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(spider_time))
    # dicts['title'] = title
    # dicts['author'] = author
    # dicts['date'] = date
    # dicts['web_name'] = web_name
    # dicts['soure_time'] = soure_time
    #
    # is_original = selector.xpath('//*[@id="copyright_logo"]/text()')
    # if len(is_original) == 0:
    #     dicts['is_original'] = 0  # 不是原创
    # else:
    #     dicts['is_original'] = 1  # 是原创
    #
    # # 用xpath取出需要的内容页面部分
    # result = selector.xpath('//*[@id="js_content"]')[0]
    # # 转为html
    # content = etree.tostring(result, method='html')
    # # 获取bs4对象
    # soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    # new_list = []
    # # ls = soup.find_all(["p", "img", 'a', 'section'])
    # ls = soup.find_all(["p", "img"])
    # for table in ls:
    #     res = {}
    #     try:
    #         target = [item.get('target') for item in table if item and item.get('target')]
    #         _break = [item.get('style') for item in table if
    #                   item and item.get('style') and 'break-word' in item.get('style')]
    #         if _break:
    #             pass
    #         elif target and target[0] == '_blank':
    #             pass
    #         elif table.get("style") and "break-word" in table.get("style"):
    #             pass
    #         else:
    #             data = table.get_text()
    #             if data:
    #                 # 去除空字符和特殊字符
    #                 new_data = "".join(data.split())
    #                 new_data = new_data.replace('\ufeff', '')
    #                 if new_data != "":
    #                     res["text"] = new_data
    #             link = table.get('data-src')
    #             if link:
    #                 res["img"] = link
    #             if res:
    #                 new_list.append(res)
    #             dicts['article'] = new_list
    #
    #     except Exception as e:
    #         return 1
    #
    # print(dicts)
