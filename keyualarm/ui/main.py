# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 391, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stuidtxt = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.stuidtxt.setObjectName("stuidtxt")
        self.verticalLayout.addWidget(self.stuidtxt)
        self.psdtxt = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.psdtxt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.psdtxt.setObjectName("psdtxt")
        self.verticalLayout.addWidget(self.psdtxt)
        self.kchtat = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.kchtat.setObjectName("kchtat")
        self.verticalLayout.addWidget(self.kchtat)
        self.kxhtxt = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.kxhtxt.setObjectName("kxhtxt")
        self.verticalLayout.addWidget(self.kxhtxt)
        self.jsmtxt = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.jsmtxt.setObjectName("jsmtxt")
        self.verticalLayout.addWidget(self.jsmtxt)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 500, 148, 46))
        self.pushButton.setObjectName("pushButton")
        self.ans_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.ans_edit.setGeometry(QtCore.QRect(490, 70, 281, 381))
        self.ans_edit.setObjectName("ans_edit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 341, 41))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.start)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stuidtxt.setPlaceholderText(_translate("MainWindow", "学号"))
        self.psdtxt.setPlaceholderText(_translate("MainWindow", "密码"))
        self.kchtat.setPlaceholderText(_translate("MainWindow", "课程号(sd开头)"))
        self.kxhtxt.setPlaceholderText(_translate("MainWindow", "课序号"))
        self.jsmtxt.setPlaceholderText(_translate("MainWindow", "教师名(没有空着)"))
        self.pushButton.setText(_translate("MainWindow", "一键社保"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://github.com/Yuandiaodiaodiao/sdu-get-class\"><span style=\" text-decoration: underline; color:#0000ff;\">项目github地址</span></a></p></body></html>"))

