# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\MyQUIForCalc.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets
from App import App

class Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("Dialog")
        self.setEnabled(True)
        self.resize(1122, 851)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 55, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(30, 280, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 55, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(800, 320, 161, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_4 = QtWidgets.QTextEdit(self)
        self.textEdit_4.setGeometry(QtCore.QRect(130, 270, 181, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self)
        self.textEdit_5.setGeometry(QtCore.QRect(580, 70, 501, 131))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(110, 80, 181, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_3 = QtWidgets.QTextEdit(self)
        self.textEdit_3.setGeometry(QtCore.QRect(110, 210, 181, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 90, 55, 16))
        self.label.setObjectName("label")
        self.CalcButton = QtWidgets.QPushButton(self)
        self.CalcButton.setGeometry(QtCore.QRect(520, 320, 161, 81))
        self.CalcButton.setObjectName("CalcButton")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(490, 80, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 55, 16))
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 140, 181, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.app = App()
        self.CalcButton.clicked.connect(self.button_send_macceleroc_result)
        self.pushButton_2.clicked.connect(self.get_result)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "num_payments"))
        self.label_2.setText(_translate("Dialog", "Balance"))
        self.pushButton_2.setText(_translate("Dialog", "get result"))
        self.label.setText(_translate("Dialog", "Rate"))
        self.CalcButton.setText(_translate("Dialog", "Caculate result"))
        self.label_6.setText(_translate("Dialog", "Answers"))
        self.label_4.setText(_translate("Dialog", "term"))
    def button_send_macceleroc_result(self):
        rate=self.textEdit.toPlainText()
        balance=self.textEdit_2.toPlainText()
        term = self.textEdit_3.toPlainText()
        num_payments=self.textEdit_4.toPlainText()
        try:
            rate=int(rate)
            balance=int(balance)
            term=int(term)
            num_payments=int(num_payments)
        except:
            self.textEdit_5.setText("TypeError")
            return TypeError
        try:
            result = self.app.calc.mac_calculate(balance, rate, term, num_payments)
            self.textEdit_5.setText(result)
            self.app.db.save_result(rate,balance,term,num_payments,result)
        except:
            self.textEdit_5.setText("ValueError")
            return ValueError
    def get_result(self):
        rate = self.textEdit.toPlainText()
        balance = self.textEdit_2.toPlainText()
        term = self.textEdit_3.toPlainText()
        num_payments = self.textEdit_4.toPlainText()
        try:
            rate = int(rate)
            balance = int(balance)
            term = int(term)
            num_payments = int(num_payments)
        except:
            self.textEdit_5.setText("TypeError")
            return TypeError
        try:
            result = self.app.db.get_one_example(rate, balance, term, num_payments)
            self.textEdit_5.setText(str(result[0][0]))
        except:
            self.textEdit_5.setText("None")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())