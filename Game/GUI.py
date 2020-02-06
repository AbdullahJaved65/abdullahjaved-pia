import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("This Is My First Window!")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World")
        self.label.move(100,100)
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Click Me!")
        self.button1.clicked.connect(self.trigger)

    def trigger(self):
        self.label.setText("You Pressed The Button!")
        self.update()

    def update(self):
        self.label.adjustSize()

def trigger():
    print("Clicked")

def window():
    app = QApplication([])
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()