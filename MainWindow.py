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
        MainWindow.resize(999, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 971, 421))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.DircomboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.DircomboBox.setObjectName("DircomboBox")
        self.verticalLayout.addWidget(self.DircomboBox)
        self.FileListWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.FileListWidget.setObjectName("FileListWidget")
        self.verticalLayout.addWidget(self.FileListWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CorrectLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CorrectLabel.setFont(font)
        self.CorrectLabel.setText("")
        self.CorrectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CorrectLabel.setObjectName("CorrectLabel")
        self.verticalLayout_2.addWidget(self.CorrectLabel)
        self.CharacterLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CharacterLabel.setFont(font)
        self.CharacterLabel.setAutoFillBackground(False)
        self.CharacterLabel.setText("")
        self.CharacterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CharacterLabel.setObjectName("CharacterLabel")
        self.verticalLayout_2.addWidget(self.CharacterLabel)
        self.VocabularyLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.VocabularyLineEdit.setFont(font)
        self.VocabularyLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.VocabularyLineEdit.setObjectName("VocabularyLineEdit")
        self.verticalLayout_2.addWidget(self.VocabularyLineEdit)
        self.NextPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.NextPushButton.setObjectName("NextPushButton")
        self.verticalLayout_2.addWidget(self.NextPushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 999, 21))
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
