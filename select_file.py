# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_file.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 363)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(999999, 9999999))
        Form.setStyleSheet("c")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 30, 291, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.datafile_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.datafile_button.sizePolicy().hasHeightForWidth())
        self.datafile_button.setSizePolicy(sizePolicy)
        self.datafile_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.datafile_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.datafile_button.setDefault(False)
        self.datafile_button.setObjectName("datafile_button")
        self.gridLayout.addWidget(self.datafile_button, 0, 0, 1, 1)
        self.indfile_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.indfile_button.setEnabled(False)
        self.indfile_button.setObjectName("indfile_button")
        self.gridLayout.addWidget(self.indfile_button, 2, 0, 1, 1)
        self.output1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.output1.setEnabled(True)
        self.output1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.output1.setText("")
        self.output1.setObjectName("output1")
        self.gridLayout.addWidget(self.output1, 1, 0, 1, 1)
        self.output2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.output2.setEnabled(True)
        self.output2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.output2.setText("")
        self.output2.setObjectName("output2")
        self.gridLayout.addWidget(self.output2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.ok_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Выбор файлов"))
        self.datafile_button.setText(_translate("Form", "Выбрать файл критериев"))
        self.indfile_button.setText(_translate("Form", "Выбрать файл индикаторов"))
        self.cancel_button.setText(_translate("Form", "Отмена"))
        self.ok_button.setText(_translate("Form", "OK"))
