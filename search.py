# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 431, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_inp = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.search_inp.setObjectName("search_inp")
        self.horizontalLayout.addWidget(self.search_inp)
        self.search_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.search_btn.setDefault(True)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 100, 431, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.label_place = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_place.setFont(font)
        self.label_place.setFrameShape(QtWidgets.QFrame.Box)
        self.label_place.setText("")
        self.label_place.setAlignment(QtCore.Qt.AlignCenter)
        self.label_place.setWordWrap(True)
        self.label_place.setObjectName("label_place")
        self.gridLayout.addWidget(self.label_place, 1, 1, 1, 1)
        self.label_v1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_v1.setFont(font)
        self.label_v1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_v1.setText("")
        self.label_v1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_v1.setWordWrap(True)
        self.label_v1.setObjectName("label_v1")
        self.gridLayout.addWidget(self.label_v1, 2, 1, 1, 1)
        self.label_v3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_v3.setFont(font)
        self.label_v3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_v3.setText("")
        self.label_v3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_v3.setWordWrap(True)
        self.label_v3.setObjectName("label_v3")
        self.gridLayout.addWidget(self.label_v3, 4, 1, 1, 1)
        self.label_v4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_v4.setFont(font)
        self.label_v4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_v4.setText("")
        self.label_v4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_v4.setWordWrap(True)
        self.label_v4.setObjectName("label_v4")
        self.gridLayout.addWidget(self.label_v4, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_v5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_v5.setFont(font)
        self.label_v5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_v5.setText("")
        self.label_v5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_v5.setWordWrap(True)
        self.label_v5.setObjectName("label_v5")
        self.gridLayout.addWidget(self.label_v5, 6, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_v2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_v2.setFont(font)
        self.label_v2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_v2.setText("")
        self.label_v2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_v2.setWordWrap(True)
        self.label_v2.setObjectName("label_v2")
        self.gridLayout.addWidget(self.label_v2, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_13.setFont(font)
        self.label_13.setFrameShape(QtWidgets.QFrame.Box)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 1)
        self.label_name = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_name.setFont(font)
        self.label_name.setFrameShape(QtWidgets.QFrame.Box)
        self.label_name.setText("")
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setWordWrap(True)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 1, 1, 1)
        self.label_v6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_v6.setFont(font)
        self.label_v6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_v6.setText("")
        self.label_v6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_v6.setWordWrap(True)
        self.label_v6.setObjectName("label_v6")
        self.gridLayout.addWidget(self.label_v6, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtWidgets.QFrame.Box)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_17.setFont(font)
        self.label_17.setFrameShape(QtWidgets.QFrame.Box)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 8, 0, 1, 1)
        self.label_sum = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_sum.setFont(font)
        self.label_sum.setFrameShape(QtWidgets.QFrame.Box)
        self.label_sum.setText("")
        self.label_sum.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sum.setWordWrap(True)
        self.label_sum.setObjectName("label_sum")
        self.gridLayout.addWidget(self.label_sum, 8, 1, 1, 1)
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(46, 80, 421, 20))
        self.error_label.setStyleSheet("color: #E61F0F;")
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Поиск по городу"))
        self.search_btn.setText(_translate("MainWindow", "Поиск"))
        self.label_9.setText(_translate("MainWindow", "3"))
        self.label_12.setText(_translate("MainWindow", "5"))
        self.label_3.setText(_translate("MainWindow", "Place"))
        self.label_7.setText(_translate("MainWindow", "2"))
        self.label_13.setText(_translate("MainWindow", "6"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_11.setText(_translate("MainWindow", "4"))
        self.label_5.setText(_translate("MainWindow", "1"))
        self.label_17.setText(_translate("MainWindow", "Sum"))

