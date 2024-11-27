# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ALI\Downloads\FaceEXP\userhome.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Camera import Ui_Camera
class Ui_userhome(object):

    def __init__(self, Dialog):
        self.dialog = Dialog


    def feedbk(self):

        try:

            name = self.uname.text()
            email = self.uname_2.text()
            phno = self.uname_3.text()

            self.cm = QtWidgets.QDialog()
            self.ui1 = Ui_Camera(self.cm,name,email,phno)
            self.ui1.setupUi(self.cm)
            self.cm.show()
            self.dialog.hide()



        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(762, 514)
        Dialog.setStyleSheet("background-color: rgb(34, 178, 191);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-30, 30, 421, 451))
        self.label.setStyleSheet("image: url(bg.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.uname_3 = QtWidgets.QLineEdit(Dialog)
        self.uname_3.setGeometry(QtCore.QRect(420, 290, 311, 40))
        self.uname_3.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.uname_3.setText("")
        self.uname_3.setObjectName("uname_3")
        self.uname = QtWidgets.QLineEdit(Dialog)
        self.uname.setGeometry(QtCore.QRect(420, 170, 311, 40))
        self.uname.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.uname.setText("")
        self.uname.setObjectName("uname")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(410, 70, 241, 61))
        self.label_6.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.label_6.setObjectName("label_6")
        self.uname_2 = QtWidgets.QLineEdit(Dialog)
        self.uname_2.setGeometry(QtCore.QRect(420, 230, 311, 40))
        self.uname_2.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.uname_2.setText("")
        self.uname_2.setObjectName("uname_2")
        self.next = QtWidgets.QPushButton(Dialog)
        self.next.setGeometry(QtCore.QRect(620, 350, 111, 31))
        self.next.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"background-color: rgb(255, 249, 219);")
        self.next.setObjectName("next")
        self.next.clicked.connect(self.feedbk)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "UserHome"))
        self.uname_3.setPlaceholderText(_translate("Dialog", "Enter Phone Number"))
        self.uname.setPlaceholderText(_translate("Dialog", "Enter Name"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">User Feedback </span></p></body></html>"))
        self.uname_2.setPlaceholderText(_translate("Dialog", "Enter Email"))
        self.next.setText(_translate("Dialog", "Next"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
