from Tools import md5
import requests

__all__ = ["Users"]


class Users(object):
    login_url = "http://bkjwxk.sdu.edu.cn/b/ajaxLogin"
    main_url = "http://bkjwxk.sdu.edu.cn"
    searchurl = "http://bkjwxk.sdu.edu.cn/b/xk/xs/kcsearch"

    def __init__(self):
        self.response = requests.get(Users.main_url)
        self.login_headers = {
            # 'accept': "*/*",
            # 'accept-encoding': "gzip, deflate",
            # 'accept-language': "zh,zh-CN;q=0.9,en;q=0.8,zh-TW;q=0.7,en-US;q=0.6",
            'connection': "keep-alive",
            'content-length': "",
            'content-type': "application/x-www-form-urlencoded;charset=UTF-8",
            # 'host': "bkjwxk.sdu.edu.cn",
            # 'origin': "http://bkjwxk.sdu.edu.cn",
            # 'referer': "http://bkjwxk.sdu.edu.cn/f/login",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            'x-requested-with': "XMLHttpRequest"

        }
        self.sessions = requests.session()  # sessions保持访问的cookie
        self.is_login = 0

    def login(self):
        self.login_headers["content-length"] = str(len(self.logindata))
        response = self.sessions.post(self.login_url, data=self.logindata, headers=self.login_headers)
        return response.json()

    def debug_changeuser(self, logindata):
        self.logindata = logindata
        self.login_headers["content-length"] = str(len(self.logindata))  # post上去的data长度为contentlength

    def changeuser(self, studentid, password):
        # 设定用户名 密码
        self.studentid = studentid
        self.password = password
        self.password_md5 = md5(password)  # 参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误
        self.logindata = "j_username=" + str(studentid) + "&j_password=" + str(self.password_md5)
        print(self.logindata)
        self.login_headers["content-length"] = str(len(self.logindata))  # post上去的data长度为contentlength

    def do_search(self):
        # 执行查课
        self.login_headers["content-length"] = str(len(self.searchdata))
        response = self.sessions.post(Users.searchurl, data=self.searchdata, headers=self.login_headers)
        return response.json()

    def pre_search(self, kch="", jsh="", skxq="", skjc="", kkxsh="", currentPage="1"):
        """课程号 教师号 上课星期 上课节数 开课学院 """
        # 设置查课参数
        type = "kc"
        self.searchdata = "type={}&currentPage={}&kch={}&jsh={}&skxq={}&skjc={}&kkxsh={}" \
            .format(type, currentPage, kch, jsh, skxq, skjc, kkxsh)
        self.login_headers["content-length"] = str(len(self.searchdata))

    def choose(self, kch, kxh):
        """课程号 课序号"""
        url = "http://bkjwxk.sdu.edu.cn/b/xk/xs/add/" + kch + "/" + kxh
        self.login_headers["content-length"] = "0"
        response = self.sessions.post(url, headers=self.login_headers)
        return response.json()

    def delclass(self, kch, kxh):
        """删除课"""
        url = "http://bkjwxk.sdu.edu.cn/b/xk/xs/delete"
        deldata = "aoData=&kchkxh=" + kch + "%7C" + kxh
        self.login_headers["content-length"] = str(len(deldata))
        response = self.sessions.post(url, data=deldata, headers=self.login_headers)
        return response.json()

    def get_rest_num(self, response, kxh):
        """response do_search的结果 (json对象) kxh 课序号 3位的那个"""
        result = response["result"]  # 成功为success
        msg = response["msg"]
        objects = response["object"]  # 课程集合
        currentPage = objects["currentPage"]  # 当前页码
        perPageNum = objects["perPageNum"]  # 单页行数
        totalPages = objects["totalPages"]  # 总页码数
        totalRows = objects["totalRows"]  # 当前页的行数
        resultList = objects["resultList"]  # 结果
        for lesson in resultList:
            if lesson["KXH"] == kxh:
                return int(lesson["kyl"])
        return False

    def search_teacher(self, teachername):
        """utf8输入教师名(vs有编码问题) 返回json"""
        url = "http://bkjwxk.sdu.edu.cn/b/xk/xs/kcapkc/sarchjsm?keyword=" + teachername + "&_=1530043816128"
        response = self.sessions.get(url)
        js = response.json()
        if js['result'] == 'success':
            return js['object'][0]['JSH']
        else:
            return ""

    def chouqian(self, kch, kxh):
        url = "http://bkjwxk.sdu.edu.cn/b/xk/xs/cq/" + str(kch) + "/" + str(kch)
        self.login_headers["content-length"] = "0"
        response = self.sessions.post(url=url, headers=self.login_headers)
        js = response.json()
        return js

    def searc(self,kch, kxh,jsm):
        if jsm!="":
            jsm=self.search_teacher(jsm)
        self.pre_search(kch=kch,jsh=jsm)
        r = self.do_search()
        #print(r)
        try:
            if "object" in r:
                if "resultList" in r["object"]:
                    if len(r["object"]["resultList"]) > 0:
                        if "KCM" in r["object"]["resultList"][0]:
                            print(r["object"]["resultList"][0]["KCM"], end=" ")
                            kyl = self.get_rest_num(r, str(kxh))
                            return kyl
        except:
            return -999

        return -9999