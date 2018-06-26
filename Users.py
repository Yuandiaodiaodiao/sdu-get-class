import os
import Tools
import requests
import copy
__all__ = ["Users"]
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



    def login(self):
        self.login_headers["content-length"] = str(len(self.logindata))
        self.response=self.sessions.post(Users.login_url,data=self.logindata,headers=self.login_headers)
        return self.response

    def changeuser(self,studentid,password):
        self.studentid=studentid
        self.password=password
        self.password_md5 = Tools.md5(password)# 参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误
        self.logindata = "j_username=" + str(studentid) + "&j_password=" + str(self.password_md5)
        self.login_headers["content-length"] = str(len(self.logindata))  # post上去的data长度为contentlength
    def do_search(self):
        self.login_headers["content-length"] = str(len(self.searchdata))
        self.response=self.sessions.post(Users.searchurl,data=self.searchdata,headers=self.login_headers)
        return self.response
    def pre_search(self,kch="",jsh="",skxq="",skjc="",kkxsh="",currentPage="1"):
        """课程号 教师号 上课星期 上课节数 开课学院 """
        type="kc"
        self.searchdata="type={}&currentPage={}&kch={}&jsh={}&skxq={}&skjc={}&kkxsh={}"\
            .format(type,currentPage,kch,jsh,skxq,skjc,kkxsh)
        self.login_headers["content-length"] = str(len(self.searchdata))
    def choose(self,kch,kxh):
        """课程号 课序号"""
        url="http://bkjwxk.sdu.edu.cn/b/xk/xs/add/"+kch+"/"+kxh
        self.login_headers["content-length"]="0"
        self.response=self.sessions.post(url,headers=self.login_headers)
        js=self.response.json()
        print(js)
        if js["result"]=="success":
            return True
        else:
            return js["msg"]
    def delclass(self,kch,kxh):
        """删除课"""
        url="http://bkjwxk.sdu.edu.cn/b/xk/xs/delete"
        deldata="aoData=&kchkxh="+kch+"%7C"+kxh
        self.login_headers["content-length"] = str(len(deldata))
        self.response=self.sessions.post(url,data=deldata,headers=self.login_headers)
        js=self.response.json()
        print(js)
        if js["result"]=="success":
            return True
        else:
            return js["msg"]
    def get_rest_num(self,response,kxh):
        result = response["result"] #成功为success
        msg = response["msg"]
        objects = response["object"]  # 课程集合
        currentPage = objects["currentPage"]  # 当前页码
        perPageNum = objects["perPageNum"]  # 单页行数
        totalPages = objects["totalPages"]  # 总页码数
        totalRows = objects["totalRows"]  # 当前页的行数
        resultList = objects["resultList"]  # 结果
        for lesson in resultList:
            if lesson["KXH"] == kxh:
                return lesson["kyl"]
    def search_teacher(self,teachername):
        url="http://bkjwxk.sdu.edu.cn/b/xk/xs/kcapkc/sarchjsm?keyword="+teachername+"&_=1530043816128"
        self.response=self.sessions.get(url)
        js = self.response.json()
        print(js)