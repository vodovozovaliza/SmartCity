# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import dirname, abspath

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(dirname(abspath(__file__)) + "/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(0, 1, 800, 600))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap(dirname(abspath(__file__)) + "/imgs/help/Frame 1.png"))
        self.img.setScaledContents(True)
        self.img.setWordWrap(False)
        self.img.setOpenExternalLinks(False)
        self.img.setObjectName("img")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 545, 660, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prev_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.prev_btn.setEnabled(False)
        self.prev_btn.setObjectName("prev_btn")
        self.horizontalLayout.addWidget(self.prev_btn)
        self.next_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout.addWidget(self.next_btn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Help"))
        self.prev_btn.setText(_translate("MainWindow", "Prev"))
        self.next_btn.setText(_translate("MainWindow", "Next"))

