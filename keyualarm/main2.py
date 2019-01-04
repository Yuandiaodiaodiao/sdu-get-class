import rubbish.v111.Users
import sys
import time
import winsound
import rubbish.v111.Tools
from keyualarm.ui.main import  Ui_MainWindow
from PyQt5 import QtWidgets,QtCore
class searchThread(QtCore.QThread):
    update_text_singal = QtCore.pyqtSignal(str)
    def __init__(self,user):
        super(searchThread,self).__init__()
        self.user=user



    def run(self):
        times=0
        while not self.isInterruptionRequested():
            time.sleep(0.8)
            print("xuan")
            r = self.user.do_search()
            kyl = self.user.get_rest_num(r, self.user.kxh)
            if (kyl>0):
                print("beep")
                self.update_text_singal.emit("课余量>0 \n !!!!!!!")
                winsound.PlaySound('alarm_01.wav', winsound.SND_ASYNC)
                time.sleep(5)

            times+=1
            self.update_text_singal.emit("课余量="+str(kyl)+"尝试次数"+str(times))


class mainwindow(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(mainwindow, self).__init__()
        self.setupUi(self)
        js= rubbish.v111.Tools.read_cache()
        self.label.setOpenExternalLinks(True)
        self.user = rubbish.v111.Users.Users()
        self.stuidtxt.setText(js["usrid"])
        self.psdtxt.setText(js["usrpsd"])
        self.kchtat.setText(js["kch"])
        self.jsmtxt.setText(js["jsm"])
        self.kxhtxt.setText(js["kxh"])
        self.thrstart = False
        self.thr = searchThread(self.user)
        self.thr.update_text_singal.connect(self.updatex)



    def updatex(self,strs):
        self.ans_edit.setText(str(strs))
    def start(self):
        if self.thrstart==True:
            self.thrstart=False
            self.thr.requestInterruption()
            self.thr.wait()
        userid = self.stuidtxt.text()
        userpsd = self.psdtxt.text()
        kch = self.kchtat.text()
        jsm = self.jsmtxt.text()
        kxh = self.kxhtxt.text()
        rubbish.v111.Tools.save_cache(userid, userpsd, kch, jsm, kxh)

        self.user.kxh=kxh
        self.user.changeuser(userid, userpsd)
        self.user.login()
        r = self.user.search_teacher(jsm)
        print(r)
        self.user.pre_search(kch=kch, jsh=r["object"][0]["JSH"])

        self.thrstart=True
        self.thr.start()






if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())
    #
    # User=v111.Users.Users()
    # User.debug_changeuser("j_username=201705130120&j_password=58c253b4ed3f16dd37f1506b9b156b7b")
    # r=User.login()


