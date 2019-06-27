# -*- coding: utf-8 -*-
import scrapy,time
from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    # allowed_domains = ['weixin.qq.com']
    allowed_domains = ['jandan.net']

    # start_urls = [
    #     'https://mp.weixin.qq.com/s?__biz=MzA3NDI3MzMzMQ==&mid=2247485130&idx=1&sn=fe4ba4175900edfb01463467814d9818&scene=4#rd']
    start_urls=['http://jandan.net/2019/06/27/eye-microbiome.html']

    def parse(self, response):
        author=response.xpath('//*[@id="content"]/div[2]/div[1]/strong/a/text()').extract()[0]
        mtime=response.xpath('//*[@id="content"]/div[2]/div[1]/text()').extract()[0]
        title=response.xpath('//*[@id="content"]/div[2]/div[1]/text()').extract()[0]
        print(author)

        # opt = webdriver.ChromeOptions()
        # opt.set_headless()
        # # chrome_options = Options()
        # # chrome_options.add_argument('--headless')
        # # chrome_options.add_argument('--no-sandbox')
        # # chrome_options.add_argument('--disable-dev-shm-usage')
        # driver = webdriver.Chrome(options=opt)
        # driver.get(response.url)
        # dicts = {}
        # # htmls = etree.HTML(driver.page_source)
        # selector = etree.HTML(driver.page_source)
        # title = selector.xpath('//*[@id="activity-name"]/text()')[0]
        # title = "".join(title.split())
        # name = selector.xpath('//*[@id="js_name"]/text()')[0]
        # name = "".join(name.split())
        # # date = selector.xpath('//*[@id="publish_time"]/text()')[0]
        # spider_time = time.time()
        # date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(spider_time))
        # dicts['title'] = title
        # dicts['name'] = name
        # dicts['date'] = date
        # dicts['web_name'] = name

        # is_original = selector.xpath('//*[@id="copyright_logo"]/text()')
        # if len(is_original) == 0:
        #     dicts['is_original'] = 0  # 不是原创
        # else:
        #     dicts['is_original'] = 1  # 是原创

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
        #     # print("=====>>>",table.get("data-style-type"))
        #     # print(type(table.tostring))
        #     # print('table', table.content)
        #     if 'target="_blank"' in table or "data-copyright" in table or "data-brushtype" in table or "break-word" in table:
        #         # print(table.get('target'))
        #         # print(table.get("data-copyright"))
        #         # print("=====>>>",table.get("data-style-type"))
        #         pass
        #     else:
        #         data = table.get_text()
        #         if data:
        #             # 去除空字符和特殊字符
        #             new_data = "".join(data.split())
        #             new_data = new_data.replace('\ufeff', '')
        #             if new_data != "":
        #                 res["text"] = new_data
                        
        #         link = table.get('data-src')
        #         if link:
        #             res["img"] = link
        #         if res:
        #             new_list.append(res)
        #         dicts['content'] = new_list
        # # print("dists",dicts['content'])
        # content=htmls.xpath('//div[@id="js_content"]/p')

        # print("contebt",content)
        # dicts = {}
        # if len(htmls.xpath('//h2[@id="activity-name"]/text()')) > 0:
        #     dicts['tit'] = htmls.xpath(
        #         '//h2[@id="activity-name"]/text()')[0].strip()
        # else:
        #     dicts['tit'] = ""
        # if len(htmls.xpath('//*[@id="publish_time"]/text()')) > 0:
        #     dicts['mtime'] = htmls.xpath('//*[@id="publish_time"]/text()')[0]
        # else:
        #     dicts['mtime'] = ""
        # if len(htmls.xpath('//span[@id="js_author_name"]/text()')) > 0:
        #     dicts['author'] = htmls.xpath(
        #         '//span[@id="js_author_name"]/text()')[0]
        # else:
        #     dicts['author'] = ""
        # # content=''.join(htmls.xpath('//div[@id="js_content"]/p/span/text()')
        # if len(driver.find_element_by_xpath(
        #         '//div[@id="js_content"]').get_attribute('outerHTML')) > 0:
        #     dicts['content'] = driver.find_element_by_xpath(
        #         '//div[@id="js_content"]').get_attribute('outerHTML')
        # else:
        #     dicts['content'] = ""
        # if len(htmls.xpath('//*[@id="js_content"]/p[5]/img/@data-src')) > 0:
        #     dicts['img_url'] = htmls.xpath(
        #         '//*[@id="js_content"]/p[5]/img/@data-src')[0]
        # else:
        #     dicts['img_url'] = ""

        # print("=====tit=======>>", tit)
        # print("======mtime=======>>", mtime)
        # print("======author=======>>", author)
        # print("======content=======>>", content)
        # print("======img_url=======>>", img_url)
        # print(dicts)
