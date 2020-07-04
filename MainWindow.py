# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(329, 228)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CharacterLabel = QtWidgets.QLabel(self.centralwidget)
        self.CharacterLabel.setGeometry(QtCore.QRect(160, 50, 150, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.CharacterLabel.setFont(font)
        self.CharacterLabel.setAutoFillBackground(False)
        self.CharacterLabel.setText("")
        self.CharacterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CharacterLabel.setObjectName("CharacterLabel")
        self.FileListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.FileListWidget.setGeometry(QtCore.QRect(10, 50, 141, 131))
        self.FileListWidget.setObjectName("FileListWidget")
        self.DircomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.DircomboBox.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.DircomboBox.setObjectName("DircomboBox")
        self.NextPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextPushButton.setGeometry(QtCore.QRect(160, 150, 150, 31))
        self.NextPushButton.setObjectName("NextPushButton")
        self.VocabularyLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.VocabularyLineEdit.setGeometry(QtCore.QRect(160, 110, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VocabularyLineEdit.setFont(font)
        self.VocabularyLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.VocabularyLineEdit.setObjectName("VocabularyLineEdit")
        self.CorrectLabel = QtWidgets.QLabel(self.centralwidget)
        self.CorrectLabel.setGeometry(QtCore.QRect(160, 10, 150, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CorrectLabel.setFont(font)
        self.CorrectLabel.setText("")
        self.CorrectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CorrectLabel.setObjectName("CorrectLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 329, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NextPushButton.setText(_translate("MainWindow", "Next"))
