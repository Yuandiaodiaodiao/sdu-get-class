import v111.Users
import time
User=v111.Users.Users()
userid = input("输入学号:")
userpsw = input("输入密码:")
User.changeuser(userid, userpsw)
r = User.login()
time.sleep(2)
# r=User.choose("sd00111790","600")
r=User.chouqian("sd00111790","600")
print(r)
