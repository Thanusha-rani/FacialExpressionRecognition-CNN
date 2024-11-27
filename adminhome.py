

from PyQt5 import QtCore, QtGui, QtWidgets
from Training import build_cnnmodel
from Ratings import Ui_Ratings
from Graph import view
from DBConnection import DBConnection
from PerformanceEvaluation import calculate_cnn_accuracy
class Ui_adminhome(object):
    
    def build_model(self):
        build_cnnmodel()
        self.showMessageBox("Information", "CNN Model is build successfully..!")


    def accuracy(self):
        calculate_cnn_accuracy()
        self.showMessageBox("Information", "Model Evaluation is completed successfully..!")

    def performance(self):
        database = DBConnection.getConnection()
        cursor = database.cursor()
        cursor.execute("select accuracy_sc,pre_sc,rec_sc,f1_sc from metrics_data")
        row = cursor.fetchall()
        for r in row:
            accuracy_cnn = r[0]
            pr_score = r[1]
            rcl_score = r[2]
            f1_score = r[3]

        list = []
        list.append(accuracy_cnn)
        list.append(pr_score)
        list.append(rcl_score)
        list.append(f1_score)
        view(list)

    def feedbk(self):
        try:
            self.fb = QtWidgets.QDialog()
            self.ui2 = Ui_Ratings()
            self.ui2.setupUi(self.fb)
            self.ui2.score()
            self.fb.show()

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
        Dialog.resize(762, 514)
        Dialog.setStyleSheet("background-color: rgb(34, 178, 191);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-30, 30, 421, 451))
        self.label.setStyleSheet("image: url(bg.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.evaluation_2 = QtWidgets.QPushButton(Dialog)
        self.evaluation_2.setGeometry(QtCore.QRect(430, 230, 241, 40))
        self.evaluation_2.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"background-color: rgb(255, 249, 219);")
        self.evaluation_2.setObjectName("evaluation_2")
        self.evaluation_2.clicked.connect(self.performance)
        self.evaluation = QtWidgets.QPushButton(Dialog)
        self.evaluation.setGeometry(QtCore.QRect(430, 160, 241, 40))
        self.evaluation.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"background-color: rgb(255, 249, 219);")
        self.evaluation.setObjectName("evaluation")
        self.evaluation.clicked.connect(self.accuracy)
        self.build = QtWidgets.QPushButton(Dialog)
        self.build.setGeometry(QtCore.QRect(430, 90, 241, 40))
        self.build.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"background-color: rgb(255, 249, 219);")
        self.build.setObjectName("build")
        self.evaluation_3 = QtWidgets.QPushButton(Dialog)
        self.evaluation_3.setGeometry(QtCore.QRect(430, 300, 241, 40))
        self.evaluation_3.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"background-color: rgb(255, 249, 219);")
        self.evaluation_3.setObjectName("evaluation_3")
        self.evaluation_3.clicked.connect(self.feedbk)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.evaluation_2.setText(_translate("Dialog", "View Performances"))
        self.evaluation.setText(_translate("Dialog", "Model Evaluation"))
        self.build.setText(_translate("Dialog", "Build Model"))
        self.evaluation_3.setText(_translate("Dialog", "View Feedback"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
