from PyQt5 import QtCore
import time
import os
import sys

class Sum(QtCore.QThread):
    sinOut = QtCore.pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.m = 0

    def run(self):
        while self.m < 100:
            self.m+=1
            self.sinOut.emit(self.m)    #反馈信号出去
            time.sleep(1)