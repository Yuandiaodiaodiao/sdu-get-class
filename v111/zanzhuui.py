# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zanzhuui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(972, 1169)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -160, 571, 811))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/zanzhu/images/1516136787129.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(490, 500, 511, 691))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/zanzhu/images/1516136829259.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(-10, 600, 581, 641))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/zanzhu/images/Screenshot_2018-01-17-05-07-47.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(490, -20, 501, 731))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/zanzhu/images/mm_facetoface_collect_qrcode_1516136980196.png"))
        self.label_4.setObjectName("label_4")
        self.label.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

import images_rc
