import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QApplication, QDialog, QLCDNumber, QMainWindow
from PyQt5.uic import loadUi


class PyCalc(QMainWindow, QLCDNumber):
    operation = 0
    Output = QLCDNumber

    def __init__(self):
        super(PyCalc, self).__init__()
        loadUi("Assets/design.ui", self)
        self.setWindowTitle("PyCalc")
        self.zero.clicked.connect(self.zero_btn)

    @pyqtSlot()
    def zero_btn(self):
        QLCDNumber.intValue(self)


app = QApplication(sys.argv)
w = PyCalc()
w.show()
sys.exit(app.exec_())
