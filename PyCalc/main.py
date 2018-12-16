#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QShortcut
from PyQt5.uic import loadUi


class PyCalc(QMainWindow):
    operation = ""
    full_operation = []
    operator_type = ""
    operator_display_char = ""

    def __init__(self):
        super(PyCalc, self).__init__()
        loadUi(os.path.dirname(__file__)+"/Assets/design.ui", self)
        self.setWindowTitle("PyCalc")
        self.init_shortcuts()
        self.zero.clicked.connect(self.btn0)
        self.one.clicked.connect(lambda: self.num(1))
        self.two.clicked.connect(lambda: self.num(2))
        self.three.clicked.connect(lambda: self.num(3))
        self.four.clicked.connect(lambda: self.num(4))
        self.five.clicked.connect(lambda: self.num(5))
        self.six.clicked.connect(lambda: self.num(6))
        self.seven.clicked.connect(lambda: self.num(7))
        self.eight.clicked.connect(lambda: self.num(8))
        self.nine.clicked.connect(lambda: self.num(9))
        self.point.clicked.connect(self.btn_point)
        self.equal.clicked.connect(self.btn_equal)
        self.plus.clicked.connect(lambda: self.set_operator('+'))
        self.minus.clicked.connect(lambda: self.set_operator("-"))
        self.multiply.clicked.connect(lambda: self.set_operator("*"))
        self.divide.clicked.connect(lambda: self.set_operator("/"))
        self.undo.clicked.connect(self.btn_undo)
        self.clear.clicked.connect(self.btn_clear)
        self.about.triggered.connect(self.btn_about)

    @pyqtSlot()
    def init_shortcuts(self):
        self.shortcut = QShortcut(QKeySequence("F1"), self)
        self.shortcut.activated.connect(self.btn_about)
        self.shortcut = QShortcut(QKeySequence("0"), self)
        self.shortcut.activated.connect(lambda: self.btn0())
        self.shortcut = QShortcut(QKeySequence("1"), self)
        self.shortcut.activated.connect(lambda: self.num(1))
        self.shortcut = QShortcut(QKeySequence("2"), self)
        self.shortcut.activated.connect(lambda: self.num(2))
        self.shortcut = QShortcut(QKeySequence("3"), self)
        self.shortcut.activated.connect(lambda: self.num(3))
        self.shortcut = QShortcut(QKeySequence("4"), self)
        self.shortcut.activated.connect(lambda: self.num(4))
        self.shortcut = QShortcut(QKeySequence("5"), self)
        self.shortcut.activated.connect(lambda: self.num(5))
        self.shortcut = QShortcut(QKeySequence("6"), self)
        self.shortcut.activated.connect(lambda: self.num(6))
        self.shortcut = QShortcut(QKeySequence("7"), self)
        self.shortcut.activated.connect(lambda: self.num(7))
        self.shortcut = QShortcut(QKeySequence("8"), self)
        self.shortcut.activated.connect(lambda: self.num(8))
        self.shortcut = QShortcut(QKeySequence("9"), self)
        self.shortcut.activated.connect(lambda: self.num(9))
        self.shortcut = QShortcut(QKeySequence("."), self)
        self.shortcut.activated.connect(lambda: self.btn_point())
        self.shortcut = QShortcut(QKeySequence("+"), self)
        self.shortcut.activated.connect(lambda: self.set_operator("+"))
        self.shortcut = QShortcut(QKeySequence("-"), self)
        self.shortcut.activated.connect(lambda: self.set_operator("-"))
        self.shortcut = QShortcut(QKeySequence("*"), self)
        self.shortcut.activated.connect(lambda: self.set_operator("*"))
        self.shortcut = QShortcut(QKeySequence("/"), self)
        self.shortcut.activated.connect(lambda: self.set_operator("/"))
        self.shortcut = QShortcut(QKeySequence("="), self)
        self.shortcut.activated.connect(lambda: self.btn_equal())
        self.shortcut = QShortcut(QKeySequence("Enter"), self)
        self.shortcut.activated.connect(lambda: self.btn_equal())
        self.shortcut = QShortcut(QKeySequence("Esc"), self)
        self.shortcut.activated.connect(lambda: self.btn_clear())
        self.shortcut = QShortcut(QKeySequence("Backspace"), self)
        self.shortcut.activated.connect(lambda: self.btn_undo())

    def btn0(self):
        if self.operation:
            if self.operation[0] != "0":
                self.operation += "0"
                self.output.setText("".join(str(i) for i in self.full_operation) + self.operation)

    def num(self, number):
        self.operation += str(number)
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
            self.output.setText("<h2><b>" + self.operation + "</b></h2>")
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

    @staticmethod
    def btn_about():
        msg = QMessageBox()
        msg.setMinimumWidth(2000)
        msg.setWindowTitle("About")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Created by @416d72")
        msg.setInformativeText('This is a Simple desktop calculator app made with PyQT5 <a '
                               'href="https://github.com/@416d72/PyCalc">View source</a>')
        msg.setDetailedText(" ")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec_()
        return


app = QApplication(sys.argv)
w = PyCalc()
w.show()
sys.exit(app.exec_())
