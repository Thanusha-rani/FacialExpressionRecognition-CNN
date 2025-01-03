

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import csv
import sys
from review import FERDetect
from Takepicture  import CaptureImage
from Result import Ui_Result
class Ui_Camera(object):

    def __init__(self,Dialog,name,email,phno):
        self.name=name
        self.email=email
        self.phno=phno
        self.dialog = Dialog


    def getCameraImage(self,event):
        try:
            CaptureImage()
            self.showMessageBox("Information", "Picture Captured..!")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def submit(self):
        try:
            emotion_text = FERDetect();
            print(emotion_text)



            self.cm = QtWidgets.QDialog()
            self.res = Ui_Result()
            self.res.setupUi(self.cm)
            self.res.feedback(emotion_text,self.name,self.email,self.phno)
            self.cm.show()
            self.dialog.hide()



        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(631, 493)
        Dialog.setStyleSheet("background-color: rgb(170, 85, 127);")
        self.camera = QtWidgets.QLabel(Dialog)
        self.camera.setGeometry(QtCore.QRect(220, 80, 161, 121))
        self.camera.setStyleSheet("image: url(../FER_CNN/images/camera.png);")
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.camera.mousePressEvent = self.getCameraImage
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(250, 220, 181, 41))
        self.label_5.setStyleSheet("font: 75 12pt \"Vani\";")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 280, 121, 41))
        self.pushButton.setStyleSheet("font: 75 12pt \"Vani\";\n"
"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.submit)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 400, 401, 61))
        self.label_2.setStyleSheet("font: 75 16pt \"Vani\";")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Camera"))
        self.label_5.setText(_translate("Dialog", "Click on Camera"))
        self.pushButton.setText(_translate("Dialog", "Detection"))
        self.label_2.setText(_translate("Dialog", ""))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Camera()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
