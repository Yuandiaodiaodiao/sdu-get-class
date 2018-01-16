import requests
import os
import time
import threading
from vars import user
from PyQt5 import QtWidgets, QtGui
from mainui import Ui_MainWindow
import sys
import loginmodule
import monitorchoose

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.label_2.setText("离线")
        self.actionA_2.triggered.connect(self.login)
        self.actionA.triggered.connect(self.to_search)
    def to_search(self):
        searchx=monitorchoose.MonitorchooseWin()
        searchx.show()
        searchx.exec_()
    # 定义槽函数
    def login(self):

        dialx=loginmodule.LoginWindow()
        dialx.show()
        dialx.exec_()
        if user.is_login==1:
            print("登录成功")
            self.label_2.setText("已登录")

        else:
            self.label_2.setText("登录失败")




if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()

    sys.exit(app.exec_())






    #
    # studentid=input("输入学号:")
    # password=input("输入密码:")
    # user=Users()
    # #print(user.login_headers)
    # response = user.login()
    # #print(response.text)
    # while not "success" in response.text:
    #     print(response.text)
    #     studentid = input("输入学号:")
    #     password = input("输入密码:")
    #     user.changeuser(studentid,password)
    #     response = user.login()
    #
    # print("登陆成功")
