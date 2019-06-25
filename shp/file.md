#爬取手机app-刷屏    四个专题
##列表页
>> https://www.weseepro.com/api/v1/activity/activities/for/pro?pageIndex=1&pageSize=20&type_uuid=289e724e0cf84800876588e2e4e3bf96   区块链列表页
>> https://www.weseepro.com/api/v1/activity/activities/for/pro?pageIndex=1&pageSize=20&type_uuid=22222222222222222222222222222222   财经列表页
>> https://www.weseepro.com/api/v1/activity/activities/for/pro?pageIndex=1&pageSize=20&type_uuid=88888888888888888888888888888888   创投列表页
>> https://www.weseepro.com/api/v1/activity/activities/for/pro?pageIndex=1&pageSize=20&type_uuid=33333333333333333333333333333333  互联网列表页

##详情页
>>    区块链详情页
>> https://www.weseepro.com/api/v1/message/stream/home/3ea9cc65632c4dc7bf8589d77adb9b2b?pageNumber=1&pageSize=10     创投详情页
>> https://www.weseepro.com/api/v1/message/stream/home/a0d270bd7d824334be20bda38f6f6c97?pageNumber=1&pageSize=10     互联网详情页
>> https://www.weseepro.com/api/v1/message/stream/home/b401ce557271458493d6e36f7f668607?pageNumber=1&pageSize=10     财经详情页


  `代码内容--request`

```flow
import requests
import json

headers = {
    'User-Agent': '36kr-Tou-Android/5.3.5 (OD103; Android 7.1.1; Scale/1920x1080; device_id/5eebf0e95e03818c15ff7014a99a4a4d)',
    'Cookie': 'JSESSIONID=F42B1D534D184569C92F2E099A042F84',
    'Host': 'www.weseepro.com',
    'Connection': 'Keep-Alive'
}

response = requests.get(
    "https://www.weseepro.com/api/v1/activity/activities/for/pro?pageIndex=1&pageSize=100&type_uuid=33333333333333333333333333333333",
    headers=headers, verify=False)
response = response.content.decode()
ss = json.loads(response)
print(ss['data'])

&```
