import Users
import json
import time
"""
登录
监视课号
课余量>1
选课
"""

if __name__=="__main__":
    # 创建用户对象
    User=Users.Users()

    userid=input("输入学号:")
    userpsw=input("输入密码:")
    kch=input("输入课程号(sd开头):")
    jsh=input("输入教师号(选课网站获取):")
    kxh=input("输入课序号(是1号而不是001):")
    dkch = input("输入退课程号(sd开头):")
    dkxh = input("输入退课序号(是1号而不是001):")

    # userid="201705130120"
    # userpsw=""
    # # 课程名
    # kch = "sd02910650"
    # # 教师号
    # jsh = "200799015592"
    # kxh = "368"  # 课序号
    # 设置用户名密码
    User.changeuser(userid,userpsw)

    # 登陆 获取返回数据
    login_rsp=User.login()

    User.pre_search(kch=kch, jsh=jsh)


    # 初始化搜索
    while True:
        # 执行搜索
        search_rsp=User.do_search().json()
        # 查询课余量
        kyl=User.get_rest_num(search_rsp,kxh)

        print("课余量"+str(kyl))

        if int(kyl)>0:
            time.sleep(2.1)
            User.delclass(dkch,dkxh) #退课
            time.sleep(2.1)
            User.choose(kch,kxh) #选课


