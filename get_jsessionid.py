import requests
import hashlib
url = "http://bkjwxk.sdu.edu.cn/b/ajaxLogin"
url1="http://bkjwxk.sdu.edu.cn/f/common/main"
sessions=requests.session()
response=sessions.post(url1)
print(response.text)
#print(response.text)
passwords=""
headers = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh,zh-CN;q=0.9,en;q=0.8,zh-TW;q=0.7,en-US;q=0.6",
    'connection': "keep-alive",
    'content-length': "67",
    'content-type': "application/x-www-form-urlencoded;charset=UTF-8",
    'host': "bkjwxk.sdu.edu.cn",
    'origin': "http://bkjwxk.sdu.edu.cn",
    'referer': "http://bkjwxk.sdu.edu.cn/f/login",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    'x-requested-with': "XMLHttpRequest"

    }
m2 = hashlib.md5()
m2.update(passwords.encode("utf-8"))#参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误
#print(m2.hexdigest())
payload="j_username=201705130120&j_password="+m2.hexdigest()

response=sessions.post(url,data=payload,headers=headers)
#print(response)
#print(response.text)
# with open('testx.html','w',encoding='utf-8') as f:
#  f.write(response.text)

url2="http://bkjwxk.sdu.edu.cn"
response=sessions.get(url)

