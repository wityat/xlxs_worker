# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 122)
        MainWindow.setMinimumSize(QtCore.QSize(581, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.browse_file = QtWidgets.QPushButton(self.centralwidget)
        self.browse_file.setObjectName("browse_file")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.browse_file)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.start)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.statusBar.setFont(font)
        self.statusBar.setToolTipDuration(-1)
        self.statusBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browse_file.setText(_translate("MainWindow", "Выбрать файл"))
        self.start.setText(_translate("MainWindow", "Начать преобразование"))
