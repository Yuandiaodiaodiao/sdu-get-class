
import hashlib
import requests
import os





url = "http://bkjwxk.sdu.edu.cn/b/xk/xs/kcsearch"
"""
qxrxk 任选  kc全部课程
kch 课序号
jsh 教师序号(支持模糊搜索)
skxq 上课星期
skjc 上课节数
开课学院序号 kkxsh
"""
#             选课类型   当前页码
payload = "type=kc&currentPage=1&kch=sd02910640&jsh=&skxq=2&skjc=3&kkxsh=" # data数据 筛选
headers = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh,zh-CN;q=0.9,en;q=0.8,zh-TW;q=0.7,en-US;q=0.6",
    'connection': "keep-alive",
    'content-length': "62",
    'content-type': "application/x-www-form-urlencoded",
    'host': "bkjwxk.sdu.edu.cn",
    'origin': "http://bkjwxk.sdu.edu.cn",
    'referer': "http://bkjwxk.sdu.edu.cn/f/common/main",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
      'cache-control': "no-cache",
    'postman-token': "d04249ff-223e-1bc1-53d8-518b38522362"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

