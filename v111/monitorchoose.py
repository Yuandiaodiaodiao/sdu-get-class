from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
import sys
from moniterui import Ui_Form
import time, threading
import os
from vars import user
from monitor import MonitorWin


class MonitorchooseWin(QtWidgets.QDialog, Ui_Form):


    def __init__(self):
        super(MonitorchooseWin, self).__init__()
        self.setupUi(self)
        # self.threads = Monitorthread()
        # self.threads.update_text_singal.connect(self.uptext)
        # self.threads.start()


    def startmonitor(self):
        payload = "type=kc&currentPage=1&kch=sd02910640&jsh=&skxq=2&skjc=3&kkxsh="  # data数据 筛选
        kch=self.lineEdit_2.text()
        skxq=self.comboBox.currentText()
        skjc=self.comboBox_2.currentText()
        type="kc"
        currentPage=1
        kkxsh=""
        jsh=""
        up_data="type={}&currentPage={}&kch={}&jsh={}&skxq={}&skjc={}&kkxsh={}"\
            .format(type,currentPage,kch,jsh,skxq,skjc,kkxsh)
        user.upload_data=up_data
        print(up_data)
        print(kch)
        user.schoolarea=self.comboBox_3.currentText()
        monitorx =MonitorWin()
        monitorx.show()
        monitorx.exec_()


    # 定义槽函数




