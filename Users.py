import os
import Tools
import requests

class Users(object):
    login_url = "http://bkjwxk.sdu.edu.cn/b/ajaxLogin"
    main_url="http://bkjwxk.sdu.edu.cn"
    searchurl = "http://bkjwxk.sdu.edu.cn/b/xk/xs/kcsearch"

    def __init__(self):
        self.response=requests.get(Users.main_url)
        self.login_headers = {
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
        self.sessions = requests.session()  # sessions保持访问的cookie
        self.is_login=0
        self.upload_data=""



    def login(self):
        self.response=self.sessions.post(Users.login_url,data=self.logindata,headers=self.login_headers)
        return self.response

    def changeuser(self,studentid,password):
        self.studentid=studentid
        self.password=password
        self.password_md5 = Tools.md5(password)# 参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误
        self.logindata = "j_username=" + str(studentid) + "&j_password=" + str(self.password_md5)
        self.login_headers["content-length"] = str(len(self.logindata))  # post上去的data长度为contentlength
    def getmonitor(self):
        self.login_headers["content-length"] = str(len(self.upload_data))
        self.response=self.sessions.post(Users.searchurl,data=self.upload_data,headers=self.login_headers)
        return self.response
