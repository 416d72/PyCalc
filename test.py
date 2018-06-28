import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLCDNumber
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.lcd = QLCDNumber(self)

        button = QPushButton('Generate', self)
        button.resize(button.sizeHint())

        layout = QVBoxLayout()
        layout.addWidget(self.lcd)
        layout.addWidget(button)

        self.setLayout(layout)
        button.clicked.connect(self.handleButton)

        self.setGeometry(300, 500, 250, 150)
        self.setWindowTitle('Rand Integer')
        self.show()

    def handleButton(self):
        self.lcd.display(self.randomint())

    def randomint(self):
        random = randint(2, 99)
        return random


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
