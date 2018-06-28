import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi


class PyCalc(QMainWindow):
    operation = ""
    full_operation = []
    operator_type = ""

    def __init__(self):
        super(PyCalc, self).__init__()
        loadUi("Assets/design.ui", self)
        self.setWindowTitle("PyCalc")
        self.zero.clicked.connect(self.btn0)
        self.one.clicked.connect(self.btn1)
        self.two.clicked.connect(self.btn2)
        # self.three.clicked.connect(self.btn3)
        # self.four.clicked.connect(self.btn4)
        # self.five.clicked.connect(self.btn5)
        # self.six.clicked.connect(self.btn6)
        # self.seven.clicked.connect(self.btn7)
        # self.eight.clicked.connect(self.btn8)
        # self.nine.clicked.connect(self.btn9)
        self.point.clicked.connect(self.btn_point)
        self.equal.clicked.connect(self.btn_equal)
        self.plus.clicked.connect(self.set_operator("+"))
        self.minus.clicked.connect(self.set_operator("-"))
        self.multiply.clicked.connect(self.set_operator("*"))
        self.divide.clicked.connect(self.set_operator("/"))
        self.undo.clicked.connect(self.btn_undo)
        self.clear.clicked.connect(self.btn_clear)
        # self.about.clicked.connect(self.btn_about)

    @pyqtSlot()
    def btn0(self):
        if self.operation:
            if self.operation[0] != "0":
                self.operation += "0"
                self.output.setText("".join(str(i) for i in self.full_operation) + self.operation)

    def btn1(self):
        self.operation += "1"
        self.output.setText("".join(str(i) for i in self.full_operation) + self.operation)

    def btn2(self):
        self.operation += "2"
        self.output.setText("".join(str(i) for i in self.full_operation) + self.operation)

    def btn_point(self):
        if "." not in self.operation:
            if not self.operation:
                self.operation += "0"
            self.operation += "."
            self.output.setText("".join(str(i) for i in self.full_operation) + self.operation)

    def btn_equal(self):
        if len(self.operation) > 0 or len(self.full_operation) > 0:
            self.full_operation.append(self.operation)
            self.operation = str(eval("".join(self.full_operation)))
            self.output.setText(self.operation)
            self.full_operation.clear()

    def set_operator(self, type_of_operator):
        self.operator_type = type_of_operator
        self.operator()

    def operator(self):
        if self.operation:
            if self.operation[-1] not in "-+*/":
                self.full_operation.append(self.operation + self.operator_type)
                self.operation = ""
        self.output.setText("".join(str(i) for i in self.full_operation))

    def btn_undo(self):
        if len(self.operation) > 0:
            self.operation = self.operation[:-1]
            if len(self.full_operation) == 0:
                self.output.setText(self.operation)
            else:
                self.output.setText("".join(str(i) for i in self.full_operation) + self.operation)
        else:
            if len(self.full_operation) > 0:
                if not self.full_operation[-1]:
                    self.full_operation.pop()
                self.full_operation[-1] = self.full_operation[-1][:-1]
                if self.full_operation[-1][-1] not in "/*-+":
                    self.operation = self.full_operation[-1]
                    self.full_operation.pop()
                self.output.setText("".join(str(i) for i in self.full_operation) + self.operation)

    def btn_clear(self):
        self.operation = ""
        self.full_operation.clear()
        self.output.setText("")


app = QApplication(sys.argv)
w = PyCalc()
w.show()
sys.exit(app.exec_())
