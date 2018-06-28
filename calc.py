import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi


class PyCalc(QMainWindow):
    operation = [0]

    def __init__(self):
        super(PyCalc, self).__init__()
        loadUi("Assets/design.ui", self)
        self.setWindowTitle("PyCalc")
        self.zero.clicked.connect(self.zero_btn)
        self.one.clicked.connect(self.one_btn)

    @pyqtSlot()
    def zero_btn(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(0)
        self.output.display("".join(str(i) for i in self.operation))

    def one_btn(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(1)
        self.output.display("".join(str(i) for i in self.operation))


app = QApplication(sys.argv)
w = PyCalc()
w.show()
sys.exit(app.exec_())
