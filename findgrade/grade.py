import bkjws.Users


def result_solve(js):
    aad = js["object"]["aaData"]
    # print(aad)
    for x in aad:
        kch = x["kch"]
        kxh = str(x["kxh"])
        kssj = x["kssj"]

        pmdata = "aoData=&dataTableId_length=-1&kch_kxh_kssj=" + kch + "_" + kxh + "_" + kssj
        # print(pmdata)
        rank = User.paiming(pmdata)
        dat = {
            "课程名": x["kcm"],
            "总成绩": x["kscj"],
            "平时成绩": x["pscj"],
            "卷面成绩": x["qmcj"],
            "考试结果": x["kscjView"],
            "五分制绩点": str(x["wfzjd"]) + "  " + str(x["wfzdj"]),
            " ":rank
        }

        for x1 in dat:
            if x1 == "课程名":
                while len(dat[x1]) < 13:
                    dat[x1] += ""
            print(x1 + ":" + str(dat[x1]), end=" ")
        print()


if __name__ == "__main__":
    print("""
    sdu平时成绩查看器
    poweredBy: Yuandiaodiaodiao
    github: https://github.com/Yuandiaodiaodiao
    成绩仅供参考
    """)
    User = bkjws.Users.Users()
    userid = input("输入学号:")
    userpsw = input("输入密码:")
    User.changeuser(userid, userpsw)
    r = User.login()
    r = User.bxqList()
    result_solve(r)
    r = User.lscj()
    result_solve(r)
    r = User.bjgcj()
    result_solve(r)
    print("最后祝您身体健康 ,再见")
    input()
