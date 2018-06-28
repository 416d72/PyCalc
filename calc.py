import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi


class PyCalc(QMainWindow):
    def __init__(self):
        super(PyCalc, self).__init__()
        loadUi("Assets/design.ui", self)
        self.setWindowTitle("PyCalc")

    @pyqtSlot()
    def on_push_button(self):
        pass


app = QApplication(sys.argv)
w = PyCalc()
w.show()
sys.exit(app.exec_())
