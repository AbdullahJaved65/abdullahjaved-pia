# -*- coding: utf-8 -*
# Form implementation generated from reading ui file 'SecondUI.ui'
# Created by: PyQt5 UI code generator 5.13.0
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import cv2
import numpy as np
import pyautogui
from mss import mss

class Ui_second_window(object):
    def ai_game(self):
         mon = {'top': 422, 'left': 163, 'width': 100, 'height': 40}  # area of interest on the screen
         k = 1
         while 1:
            img = mss().grab(mon)
            img = np.array(img)

            cv2.imshow('test', img)
            p_cac = img[22, :, 0]   
            p_bird = img[1, :, 0]

            p_cac_sum = np.sum(p_cac)
            print(p_cac_sum)
            p_bird_sum = np.sum(p_bird)

            if p_cac_sum < 23911:
                pyautogui.press('up')

            if p_bird_sum == 22241 and k == 1:
                pyautogui.keyUp('down')
                k = 0
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
   
    def open_webpage(self):
        new = 1
        url = "http://www.trex-game.skipser.com"
        webbrowser.open(url,new=new)

    def setupUi(self, second_window):
        second_window.setObjectName("second_window")
        second_window.resize(728, 335)

        self.centralwidget = QtWidgets.QWidget(second_window)
        self.centralwidget.setObjectName("centralwidget")

        self.label_picture = QtWidgets.QLabel(self.centralwidget)
        self.label_picture.setGeometry(QtCore.QRect(0, 0, 721, 311))
        self.label_picture.setText("")
        self.label_picture.setPixmap(QtGui.QPixmap("Images/1505257519-trexgame - oblogka.JPG"))
        self.label_picture.setScaledContents(True)
        self.label_picture.setObjectName("label_picture")

        self.button_AI = QtWidgets.QPushButton(self.centralwidget)
        self.button_AI.setGeometry(QtCore.QRect(320, 200, 75, 23))
        self.button_AI.setObjectName("button_AI")
        self.button_AI.clicked.connect(self.ai_game)

        self.button_Start = QtWidgets.QPushButton(self.centralwidget)
        self.button_Start.setGeometry(QtCore.QRect(290, 70, 151, 61))
        self.button_Start.setObjectName("button_Start")
        self.button_Start.clicked.connect(self.open_webpage)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Goudy Stout")
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_message = QtWidgets.QLabel(self.centralwidget)
        self.label_message.setGeometry(QtCore.QRect(200, 170, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Goudy Stout")
        self.label_message.setFont(font)
        self.label_message.setObjectName("label_message")

        second_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(second_window)
        self.statusbar.setObjectName("statusbar")
        second_window.setStatusBar(self.statusbar)

        self.retranslateUi(second_window)
        QtCore.QMetaObject.connectSlotsByName(second_window)

    def retranslateUi(self, second_window):
        _translate = QtCore.QCoreApplication.translate
        second_window.setWindowTitle(_translate("second_window", "Dino Run"))
        self.button_AI.setText(_translate("second_window", "Yes, Please!"))
        self.button_Start.setText(_translate("second_window", "Start The Game!"))
        self.label.setText(_translate("second_window", "Start The Game By Pressing The Button Below"))
        self.label_message.setText(_translate("second_window", "Do You Want To Use The AI?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    second_window = QtWidgets.QMainWindow()
    ui = Ui_second_window()
    ui.setupUi(second_window)
    second_window.show()
    sys.exit(app.exec_())