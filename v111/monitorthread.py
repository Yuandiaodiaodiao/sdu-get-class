from PyQt5 import QtCore
import time
import os
import sys
from vars import user
import json

class Monitorthread(QtCore.QThread):
    update_text_singal = QtCore.pyqtSignal(str)
    clear_text_singal = QtCore.pyqtSignal()
    def __init__(self):
        super(Monitorthread,self).__init__()


    def run(self):
        asq=1
        while not self.isInterruptionRequested():
            time.sleep(5)
            #self.clear_text_singal.emit()
            responsx=user.getmonitor()
            # print(responsx.text)
            if len(str(responsx))<10:
                continue
            response=json.loads(responsx.text)
            objects=response["object"]
            currentPage=objects["currentPage"]
            perPageNum=objects["perPageNum"]
            totalPages=objects["totalPages"]
            totalRows=objects["totalRows"]
            resultList=objects["resultList"]
            ans=""
            for c in resultList:
                print(c["SJDD"])
                if not user.schoolarea in c["SJDD"]:
                    continue
                strings="课余量{:<4} 课程:{:<15} 教师:{:<10}"\
                    .format(c["kyl"],c["KCM"],c["JSM"])
                strings=str(strings)
                #strings=strings.replace("("," (")
                strings=strings.replace(")",") ")
                print(strings)
                ans+=strings+"\n"
            self.update_text_singal.emit(ans)