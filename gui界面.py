from PyQt5 import QtWidgets, QtGui
import sys
from untitled import Ui_MainWindow
import time, threading
import os
from Users import Users
import  monitor
def loop():
    class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
        def __init__(self):
            super(mywindow,self).__init__()
            self.setupUi(self)

        #定义槽函数
        def hello(self):
            t = threading.Thread(target=monitor.starmonint, name='LoopThread')
            t.start()
            self.textEdit.setText("hello world")

    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()

    app.exec_()
    print("结束")
loop()
t = threading.Thread(target=monitor.starmonint, name='LoopThread2')
t.start()

n=100
sys.exit(0)
