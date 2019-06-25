# import requests
#
# headers = {
#     "Host": "mp.weixin.qq.com",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
# }
# response = requests.get(
#     'https://mp.weixin.qq.com/s?__biz=MzA3NDI3MzMzMQ==&mid=2247485130&idx=1&sn=fe4ba4175900edfb01463467814d9818&scene=4#rd',
#     headers=headers)
#
# print(response.content)
ss = "https://www.weseepro.com/api/v1/message/stream/home/d23aaf8649864dd586d346cc708bdaf8?pageNumber=5&pageSize=10"

print(ss.split("/")[-1].split("?")[0])
