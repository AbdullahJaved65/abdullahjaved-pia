# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'UI.ui'
# Created by: PyQt5 UI code generator 5.13.
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from SecondUI import Ui_second_window

class Ui_dino_run(object):
    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow() 
        self.ui = Ui_second_window()
        self.ui.setupUi(self.window)
        dino_run.hide()
        self.window.show()
    
    def setupUi(self, dino_run):
        dino_run.setObjectName("dino_run")
        dino_run.resize(737, 463)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)

        dino_run.setPalette(palette)
        dino_run.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.centralwidget = QtWidgets.QWidget(dino_run)
        self.centralwidget.setObjectName("centralwidget")

        self.label_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(0, 10, 731, 431))
        self.label_pic.setAutoFillBackground(False)
        self.label_pic.setText("")
        self.label_pic.setPixmap(QtGui.QPixmap("Images/1505257519-trexgame - oblogka.JPG"))
        self.label_pic.setScaledContents(True)
        self.label_pic.setObjectName("label_pic")

        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(300, 270, 151, 51))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.openWindow)

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(280, 40, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Goudy Stout")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label1.setObjectName("label1")
        
        dino_run.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(dino_run)
        self.statusbar.setObjectName("statusbar")
        dino_run.setStatusBar(self.statusbar)

        self.retranslateUi(dino_run)
        QtCore.QMetaObject.connectSlotsByName(dino_run)

    def retranslateUi(self, dino_run):
        _translate = QtCore.QCoreApplication.translate
        dino_run.setWindowTitle(_translate("dino_run", "Dino Run"))
        self.button1.setText(_translate("dino_run", "Go To Menu"))
        self.label1.setText(_translate("dino_run", "Dino Run!"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dino_run = QtWidgets.QMainWindow()
    ui = Ui_dino_run()
    ui.setupUi(dino_run)
    dino_run.show()
    sys.exit(app.exec_())