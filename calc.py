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
        self.zero.clicked.connect(self.btn0)
        self.one.clicked.connect(self.btn1)
        self.two.clicked.connect(self.btn2)
        self.three.clicked.connect(self.btn3)
        self.four.clicked.connect(self.btn4)
        self.five.clicked.connect(self.btn5)
        self.six.clicked.connect(self.btn6)
        self.seven.clicked.connect(self.btn7)
        self.eight.clicked.connect(self.btn8)
        self.nine.clicked.connect(self.btn9)
        self.point.clicked.connect(self.btn_point)
        self.equal.clicked.connect(self.btn_equal)
        self.plus.clicked.connect(self.btn_plus)
        self.minus.clicked.connect(self.btn_minus)
        self.multiply.clicked.connect(self.btn_multiply)
        self.divide.clicked.connect(self.btn_divide)
        self.undo.clicked.connect(self.btn_undo)
        self.clear.clicked.connect(self.btn_clear)
        self.about.clicked.connect(self.about)

    @pyqtSlot()
    def btn0(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(0)
        self.output.display("".join(str(i) for i in self.operation))

    def btn1(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(1)
        self.output.display("".join(str(i) for i in self.operation))

    def btn2(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn3(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn4(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn5(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn6(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn7(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn8(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn9(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn_point(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn_equal(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn_plus(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn_minus(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn_multiply(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn_divide(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn_undo(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def btn_clear(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))

    def about(self):
        if self.operation[0] == 0:
            del (self.operation[0])
        self.operation.append(2)
        self.output.display("".join(str(i) for i in self.operation))



app = QApplication(sys.argv)
w = PyCalc()
w.show()
sys.exit(app.exec_())
