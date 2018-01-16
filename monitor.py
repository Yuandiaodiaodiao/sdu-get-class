from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
import sys
from untitled import Ui_Form
import time, threading
import os
from vars import user
from monitorthread import Monitorthread


class MonitorWin(QtWidgets.QDialog, Ui_Form):


    def __init__(self):
        super(MonitorWin, self).__init__()
        self.setupUi(self)
        self.threads = Monitorthread()
        # self.textEdit.append("22222")
        # self.textEdit.append("6666")
        self.threads.update_text_singal.connect(self.uptext)
        self.threads.clear_text_singal.connect(self.cleartext)
        self.threads.start()
    def __del__(self):
        self.threads.requestInterruption()
        self.threads.wait()
        self.close()




    # 定义槽函数
    def end(self):
        self.threads.requestInterruption()
        self.threads.wait()
        self.close()
        # self.threads.
        #self.ui.textEdit_info.clear()

    def cleartext(self):
        self.textEdit.clear()
    def uptext(self,text):
        #print(1)
        self.textEdit.setText(text)

