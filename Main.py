# -*- coding: UTF-8 -*-
'''
Created on 2020年6月22日

@author: Kuan
'''
import os
import sys

from PyQt5 import QtWidgets, QtCore
import Config
import Helpers.LoadFile as LoadFileHelper
from MainWindow import Ui_MainWindow


class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__content_index = 0
        self.score = 0
        self.__dir_path = LoadFileHelper.get_dir_path(Config.Dagdai_Dir_NAME)
        self.__text_list = []
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.setWindowTitle("LearningBPM")
        self.initialize()
        self.__ui.DircomboBox.currentIndexChanged.connect(self.select_level)
        self.__ui.FileListWidget.itemClicked.connect(self.load_ppt_file)
        self.__ui.NextPushButton.clicked.connect(self.next_pushbutton_clicked)
        self.__ui.NextPushButton.setShortcut(QtCore.Qt.Key_Return)

    # ========================================================================
    def initialize(self):
        selected_dir = ""
        self.__ui.FileListWidget.clear()
        self.add_dir_list()
        self.add_file_list()

    def next_pushbutton_clicked(self):
        self.__ui.CorrectLabel.setAutoFillBackground(True)
        label_text = self.__ui.VocabularyLineEdit.text()
        line_edit_text = self.__ui.CharacterLabel.text()
        if label_text.strip() == line_edit_text.strip():
            self.__ui.CorrectLabel.setStyleSheet("background-color: lightgreen")
            self.__ui.CorrectLabel.setText("Correct!!")
            self.score = self.score + 1
        else:
            self.__ui.CorrectLabel.setStyleSheet("background-color: red")
            self.__ui.CorrectLabel.setText("Ooops!!")

        self.__content_index = self.__content_index + 1
        if self.__content_index < len(self.__text_list):
            self.__ui.CharacterLabel.setText(self.__text_list[self.__content_index])
        else:
            self.__ui.CharacterLabel.setText("Finish!!")
            self.__ui.CorrectLabel.setAutoFillBackground(False)
            self.__ui.VocabularyLineEdit.setEnabled(False)
            self.__ui.ScoreLabel.setText("SCORE: " + str(round(self.score / len(self.__text_list) * 100, 1)))

    def load_ppt_file(self):
        self.__text_list = []
        self.__content_index = 0
        self.__ui.VocabularyLineEdit.setEnabled(True)
        ppt_dir = self.get_ppt_dir()
        file_list = LoadFileHelper.get_file_list(ppt_dir)
        file_index = self.__ui.FileListWidget.currentRow()
        file_path = ppt_dir + "\\" + file_list[file_index]
        self.__text_list = LoadFileHelper.load_powerpoint_file(file_path)
        self.__ui.CharacterLabel.setText(self.__text_list[self.__content_index])

    def select_level(self):
        selected_dir = ""
        self.__ui.FileListWidget.clear()
        self.add_file_list()

    def add_dir_list(self):
        dir_list = LoadFileHelper.get_file_list(Config.Dagdai_Dir_NAME)
        for DIR in dir_list:
            self.__ui.DircomboBox.addItem(DIR)

    def add_file_list(self):
        ppt_dir = self.get_ppt_dir()
        file_list = LoadFileHelper.get_file_list(ppt_dir)
        for PPT in file_list:
            self.__ui.FileListWidget.addItem(PPT)

    def get_ppt_dir(self):
        dir_path = self.__dir_path + "\\" + self.__ui.DircomboBox.currentText()
        sub_dir_list = os.listdir(dir_path)
        selected_dir = dir_path + "\\" + sub_dir_list[1]
        return selected_dir


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = AppWindow()
    MainWindow.show()
    sys.exit(app.exec_())
