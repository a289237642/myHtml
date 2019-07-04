import requests
import re
from lxml import etree
from bs4 import BeautifulSoup


url = "https://www.tmtpost.com/4040455.html"

headers = {
    'User-Agent': '36kr-Tou-Android/5.3.5 (OD103; Android 7.1.1; Scale/1920x1080; device_id/5eebf0e95e03818c15ff7014a99a4a4d)'
}

response = requests.get(url, headers=headers).text
selector = etree.HTML(response)

tit = selector.xpath('//div[@class="pro_icon"]/img/@src')[0]
print(tit)

text1 = BeautifulSoup(response, features="lxml").get_text()

ic = "$$".join(re.findall("src=\"(.*?)\"", response))

print(ic,text1)