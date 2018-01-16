#_*_coding:utf-8_*_
from PyQt5.QtCore import QThread,Qt,pyqtSignal
from PyQt5.QtWidgets import QWidget,QLabel,QApplication
import sys
import time
from text2 import  Sum
class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("demo")
        self.resize(400,200)
        self.lable =QLabel("这是一个标签",self)
        self.lable.move(150,100)
        self.sum = Sum()    #实例化Sum类
        self.sum.sinOut.connect(self.printNum)  #将信号连接至printNum函数
        self.sum.start()    #开启线程
        self.show()
    def printNum(self,num):
        print(num)


if __name__ == '__main__':
    app =QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec())