import Users
User=Users.Users()
userid="201705130120"
userpsw="Wangzixi"

User.changeuser(userid, userpsw)

# 登陆 获取返回数据
login_rsp = User.login()
User.search_teacher("照明")