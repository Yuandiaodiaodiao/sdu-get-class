import os
from loginui import Ui_Dialog
from PyQt5 import QtWidgets, QtGui
import sys
from vars import user

class LoginWindow(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        with open('pass', 'r') as f:
            cookiesx=f.read()
        if len(cookiesx)>7:
            cookiesx=cookiesx.split(",")
            self.lineEdit.setText(cookiesx[0])
            self.lineEdit_2.setText(cookiesx[1])


    def press_ok(self):
        stuid=self.lineEdit.text()
        password=self.lineEdit_2.text()
        user.changeuser(stuid,password)
        response=user.login()
        if "success" in response.text:
            user.is_login=1
            with open('pass', 'w') as f:
                f.write(user.studentid+","+user.password)

            self.accept()
        else:
            self.label_3.setText(response.text)


def startlogin():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    startlogin()