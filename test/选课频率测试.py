import v111.Users
import time
User=v111.Users.Users()
User.changeuser("201705130120","Wangzixi")
User.login()
def searc(kch):
    User.pre_search(kch=kch)
    r=User.do_search()
    # print(r)
    print(r["object"]["resultList"][0]["KCM"],end=" ")
    kyl=User.get_rest_num(r,"600")
    return kyl
def tuixuan(kch,kxh,kchx,kxhx):
    r=User.delclass(kch,kxh)
    print(r["msg"])
    time.sleep(2)
    r=User.choose(kchx,kxhx)
    print(r["msg"])
while True:
    searc("sd07517120")
    tuixuan("sd00221142","0","sd00221142","0")
