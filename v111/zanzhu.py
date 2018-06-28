from PyQt5 import QtWidgets, QtGui
from zanzhuui import Ui_Form


class ZanzhuWin(QtWidgets.QDialog, Ui_Form):


    def __init__(self):
        super(ZanzhuWin, self).__init__()
        self.setupUi(self)