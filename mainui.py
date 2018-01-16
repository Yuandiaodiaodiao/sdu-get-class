# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 150, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 0, 135, 30))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 110, 681, 381))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 321, 30))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 30, 187, 57))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 45))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionA = QtWidgets.QAction(MainWindow)
        self.actionA.setObjectName("actionA")
        self.actionA_2 = QtWidgets.QAction(MainWindow)
        self.actionA_2.setCheckable(False)
        self.actionA_2.setObjectName("actionA_2")
        self.actionB = QtWidgets.QAction(MainWindow)
        self.actionB.setObjectName("actionB")
        self.actionA_3 = QtWidgets.QAction(MainWindow)
        self.actionA_3.setObjectName("actionA_3")
        self.menu.addAction(self.actionA)
        self.menu.addAction(self.actionA_3)
        self.menu_2.addAction(self.actionA_2)
        self.menu_2.addAction(self.actionB)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.zanzhu)
        self.pushButton_2.clicked.connect(MainWindow.newversion)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "账户状态:"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "一键赞助吃土的开发者"))
        self.label_3.setText(_translate("MainWindow", "本软件永久免费"))
        self.pushButton_2.setText(_translate("MainWindow", "获取最新版本"))
        self.menu.setTitle(_translate("MainWindow", "功能"))
        self.menu_2.setTitle(_translate("MainWindow", "账户"))
        self.actionA.setText(_translate("MainWindow", "课余量查询"))
        self.actionA_2.setText(_translate("MainWindow", "登陆"))
        self.actionB.setText(_translate("MainWindow", "退出"))
        self.actionA_3.setText(_translate("MainWindow", "成绩查询"))

