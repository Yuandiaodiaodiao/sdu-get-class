import Users
import time

Userid: str = "201705130120"  # 用户名
Userpsd: str = ""  # 密码
xk_kxh: list = ["sd07510780", "sd07510770", "sd07510790"]  # 待选列表
kxh: list = ["660", "660", "660"]  # 待选课序号 和xk_kxh一一对应
jsm: list = ["", "", ""]  # 教师名 必须全名 同课序号少于30条时可以置空 一一对应
dkch: str = ""  # 退课课程号 如果不需要退课置空
dkxh: str = ""  # 退课课序号 三位数

if __name__ == "__main__":
    User = Users.Users()
    User.changeuser(Userid, Userpsd)
    r = User.login()
    time.sleep(2.5)

    while "正选结束" in str(r):
        r = User.login()
        print(r)
        time.sleep(2.5)

    while True:
        for x, kx, jshi in zip(xk_kxh, kxh, jsm):
            time.sleep(0.3)
            kyl = User.searc(x, kx, jshi)
            print("课余量=" + str(kyl))
            if int(kyl) > 0:
                print("尝试选课")
                if dkch != "":
                    # 退课
                    User.delclass(dkch, dkxh)
                    time.sleep(2)
                # 选课
                r = User.choose(x, kx)
                print(r)
                time.sleep(2)
