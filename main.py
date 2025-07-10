import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import uic
from time import sleep


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.znach1 = ""
        self.znach2 = ""
        self.operation = False
        self.operSign = ""

        self.ce.clicked.connect(lambda: self.ce_clicked(self.line.text()))
        self.sign.clicked.connect(lambda: self.sign_clicked(self.line.text()))
        self.zero.clicked.connect(lambda: self.zero_clicked(self.line.text()))
        self.dote.clicked.connect(lambda: self.dote_clicked(self.line.text()))
        self.equal.clicked.connect(lambda: self.equal_clicked(self.line.text()))
        self.plus.clicked.connect(
            lambda: self.operation_clicked(self.line.text(), "plus")
        )
        self.minus.clicked.connect(
            lambda: self.operation_clicked(self.line.text(), "minus")
        )
        self.mult.clicked.connect(
            lambda: self.operation_clicked(self.line.text(), "mult")
        )
        self.div.clicked.connect(
            lambda: self.operation_clicked(self.line.text(), "div")
        )
        self.off.clicked.connect(
            lambda: self.off_on_clicked(self.line.text(), self.off.text())
        )
        self.on.clicked.connect(
            lambda: self.off_on_clicked(self.line.text(), self.on.text())
        )
        self.one.clicked.connect(
            lambda: self.digit_clicked(self.line.text(), self.one.text())
        )
        self.two.clicked.connect(
            lambda: self.digit_clicked(self.line.text(), self.two.text())
        )
        self.three.clicked.connect(
            lambda: self.digit_clicked(self.line.text(), self.three.text())
        )
        self.four.clicked.connect(
            lambda: self.digit_clicked(self.line.text(), self.four.text())
        )
        self.five.clicked.connect(
            lambda: self.digit_clicked(self.line.text(), self.five.text())
        )
        self.six.clicked.connect(
            lambda: self.digit_clicked(self.line.text(), self.six.text())
        )
        self.seven.clicked.connect(
            lambda: self.digit_clicked(self.line.text(), self.seven.text())
        )
        self.eight.clicked.connect(
            lambda: self.digit_clicked(self.line.text(), self.eight.text())
        )
        self.nine.clicked.connect(
            lambda: self.digit_clicked(self.line.text(), self.nine.text())
        )

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.ce_clicked(self.line.text())
        elif event.key() == Qt.Key.Key_Enter:
            self.equal_clicked(self.line.text())
        elif event.key() == Qt.Key.Key_Return:
            self.equal_clicked(self.line.text())
        elif event.key() == Qt.Key.Key_0:
            self.zero_clicked(self.line.text())
        elif (
            event.key() == Qt.Key.Key_1
            or event.key() == Qt.Key.Key_2
            or event.key() == Qt.Key.Key_3
            or event.key() == Qt.Key.Key_4
            or event.key() == Qt.Key.Key_5
            or event.key() == Qt.Key.Key_6
            or event.key() == Qt.Key.Key_7
            or event.key() == Qt.Key.Key_8
            or event.key() == Qt.Key.Key_9
        ):
            self.digit_clicked(self.line.text(), event.text())
        elif event.text() == ".":
            self.dote_clicked(self.line.text())
        elif event.text() == "+":
            self.operation_clicked(self.line.text(), "plus")
        elif event.text() == "-":
            self.operation_clicked(self.line.text(), "minus")
        elif event.text() == "*":
            self.operation_clicked(self.line.text(), "mult")
        elif event.text() == "/":
            self.operation_clicked(self.line.text(), "div")
        elif event.text() == "q" or event.text() == "Q" or event.text() == "й" or event.text() == "Й":
            self.sign_clicked(self.line.text())
        elif event.key() == Qt.Key.Key_F1:
            self.off_on_clicked(self.line.text(), self.on.text())
        elif event.key() == Qt.Key.Key_F2:
            self.off_on_clicked(self.line.text(), self.off.text())

    def equal_clicked(self, lineText):
        if lineText != "":
            if self.znach1 != "":
                self.znach2 = float(lineText)
                self.calculations(self.operSign)
                self.operSign = ""
                self.operation = False
                self.znach1 = ""

    def operation_clicked(self, lineText, oper):
        if lineText != "":
            if self.znach1 == "":
                self.znach1 = float(lineText)
                self.operSign = oper
            else:
                self.znach2 = float(lineText)
                self.calculations(self.operSign)
                self.operSign = oper

            self.operation = True

    def calculations(self, oper):
        result = 0.0
        if oper == "plus":
            result = self.znach1 + self.znach2
        elif oper == "minus":
            result = self.znach1 - self.znach2
        elif oper == "mult":
            result = self.znach1 * self.znach2
        elif oper == "div":
            result = self.znach1 / self.znach2

        self.znach2 = 0.0
        self.znach1 = result
        if self.znach1 == int(self.znach1):
            self.znach1 = int(self.znach1)
        self.line.setText(str(self.znach1))

    def ce_clicked(self, lineText):
        if lineText != "":
            self.line.setText("0")
            self.operation = False
            self.znach1 = ""
            self.znach2 = ""

    def off_on_clicked(self, lineText, text):
        if text == "Off":
            if lineText != "":
                self.line.setText("")
                self.operation = False
                self.znach1 = ""
                self.znach2 = ""
        else:
            if lineText == "":
                self.line.setText("0")

    def dote_clicked(self, lineText):
        if "." not in lineText and lineText != "":
            if self.operation == True:
                self.line.setText("0.")
                self.operation = False
            else:
                self.line.setText(f"{lineText}.")

    def sign_clicked(self, lineText):
        if lineText != "0" and lineText != "":
            if self.operation == True:
                self.line.setText("0")
                self.operation = False
            else:
                if lineText[0] == "-":
                    self.line.setText(lineText[1:])
                else:
                    self.line.setText(f"-{lineText}")

    def zero_clicked(self, lineText):
        if lineText != "0" and lineText != "":
            if self.operation == True:
                self.line.setText("0")
                self.operation = False
            else:
                self.line.setText(f"{lineText}0")

    def digit_clicked(self, lineText, digit):
        if lineText != "":
            if self.operation == True:
                self.line.setText(digit)
                self.operation = False
            else:
                if lineText == "0":
                    self.line.setText(digit)
                else:
                    self.line.setText(f"{lineText}{digit}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
