import scrapy
import json, logging, time
from shp.items import ShpItem, ShpUserItem
from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

loger = logging.getLogger("default_handlers")


class SpInfoSpider(scrapy.Spider):
    name = 'sp_info'
    allowed_domains = ['weseepro.com']
    url = 'https://www.weseepro.com/api/v1/activity/activities/for/pro?pageIndex={}&pageSize=20&type_uuid=88888888888888888888888888888888'
    page = 1
    start_urls = [url.format(page)]

    detail = "https://www.weseepro.com/api/v1/message/stream/home/{}?pageNumber={}&pageSize=10"

    def handlesUrl(self, url):
        return url.split("/")[-1].split("?")[0]

    def handlerWx(self, url):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        dicts = {}
        selector = etree.HTML(driver.page_source)
        title = selector.xpath('//*[@id="activity-name"]/text()')[0]
        title = "".join(title.split())
        author = selector.xpath('//*[@id="js_name"]/text()')[0]
        author = "".join(author.split())
        spider_time = time.time()
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(spider_time))
        dicts['title'] = title
        dicts['author'] = author
        dicts['date'] = date
        dicts['web_name'] = "微信文章"
        dicts['source_url'] = url

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
            # print(type(table))
            try:
                target = [item.get('target') for item in table if item and item.get('target')]
                _break = [item.get('style') for item in table if
                          item and item.get('style') and 'break-word' in item.get('style')]
                # print(_break)
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
                    dicts['content'] = new_list

            except Exception as e:
                loger.error('爬虫中断,进程退出,errmsg:{0}'.format(e))
        return dicts

    def parse(self, response):
        python_dict = json.loads(response.text)
        myList = python_dict['data']['activities']
        # 爬虫结束条件
        if myList is None:
            return
        for mlist in myList:
            new_url = self.detail.format(mlist['activity_uuid'], self.page)
            yield scrapy.Request(new_url, callback=self.parse_detail)

        self.page += 1
        url = self.url.format(self.page)
        yield scrapy.Request(url, callback=self.parse)

    def parse_detail(self, response):
        uu = self.handlesUrl(response.url)

        python_dict = json.loads(response.text)
        myFriend = python_dict['data']['messages']
        if len(myFriend) > 0:
            for mfriend in myFriend:
                item = ShpItem()
                # 分享的链接或者图片的地址
                if 'link' not in mfriend['message'].keys():
                    item['url'] = ""
                elif mfriend['message']['link'] is None:
                    item['url'] = ""
                elif 'url' not in mfriend['message']['link'].keys():
                    item['url'] = ""
                else:
                    url = mfriend['message']['link']['url']
                    if "mp.weixin.qq.com" in url:
                        dicts = self.handlerWx(url)
                        item['title'] = dicts['title']
                        item['author'] = dicts['author']
                        item['is_original'] = dicts['is_original']
                        item['content'] = dicts['content']
                        item['tUrl'] = dicts['tUrl']
                        item['activity_uuid'] = uu
                        # pass
                        print(item)
                        # yield item
                    else:
                        pass

                # print(item)
                yield item
        else:
            return

        self.page += 1
        url = self.detail.format(uu, self.page)
        yield scrapy.Request(url, callback=self.parse_detail)
