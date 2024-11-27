

from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
from adminhome import Ui_adminhome
from userhome import Ui_userhome
class Ui_Main(object):
    def __init__(self, Dialog):
        self.dialog = Dialog

    def logincheck(self):
        try:
            database = DBConnection.getConnection()
            cursor = database.cursor()
            unm = self.auid.text()
            pwd = self.apwd.text()
            if unm == "" or unm == "null" or pwd == "" or pwd == "null":
                self.showMessageBox("Information", "Please fill out all fields")
            else:
                sql = "select count(*) from adminlogin where userid='" + unm + "' and password='" + pwd + "'"
                cursor.execute(sql)
                res = cursor.fetchone()[0]
                if res > 0:
                    self.home = QtWidgets.QDialog()
                    self.ui = Ui_adminhome()
                    self.ui.setupUi(self.home)
                    self.home.show()
                    self.dialog.hide()
                   
                else:
                    self.showMessageBox("Information", "Invalid Credentials..!")
                
                
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def feedbk(self):
        self.uhome = QtWidgets.QDialog()
        self.ui = Ui_userhome(self.uhome)
        self.ui.setupUi(self.uhome)
        self.uhome.show()
        self.dialog.hide()




    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(990, 641)
        Dialog.setStyleSheet("background-color: rgb(101, 203, 223);")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 80, 991, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(-10, 0, 981, 521))
        self.tableWidget.setStyleSheet("background-image: url(expbanner.jpg);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(750, 110, 191, 61))
        self.label_5.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.label_5.setObjectName("label_5")
        self.alogin = QtWidgets.QPushButton(self.tab_2)
        self.alogin.setGeometry(QtCore.QRect(600, 310, 120, 40))
        self.alogin.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.alogin.setObjectName("alogin")
        self.alogin.clicked.connect(self.logincheck)

        self.apwd = QtWidgets.QLineEdit(self.tab_2)
        self.apwd.setGeometry(QtCore.QRect(600, 250, 330, 40))
        self.apwd.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.apwd.setText("")
        self.apwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.apwd.setObjectName("apwd")
        self.auid = QtWidgets.QLineEdit(self.tab_2)
        self.auid.setGeometry(QtCore.QRect(600, 190, 330, 40))
        self.auid.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.auid.setText("")
        self.auid.setObjectName("auid")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(-270, 0, 771, 541))
        self.tableWidget_2.setStyleSheet("background-image: url(expbanner.jpg);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(-270, 0, 771, 541))
        self.tableWidget_3.setStyleSheet("background-image: url(expbanner.jpg);")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.feedback = QtWidgets.QPushButton(self.tab_3)
        self.feedback.setGeometry(QtCore.QRect(600, 230, 281, 40))
        self.feedback.setStyleSheet("font: 14pt \"Levenim MT\";\n"
"color: rgb(255, 251, 248);")
        self.feedback.setObjectName("feedback")
        self.feedback.clicked.connect(self.feedbk)
        self.tabWidget.addTab(self.tab_3, "")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 901, 51))
        self.label_2.setStyleSheet("\n"
"font: 175 18pt \"Microsoft YaHei UI Light\";\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Home"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Admin Login</span></p></body></html>"))
        self.alogin.setText(_translate("Dialog", "Login"))
        self.apwd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.auid.setPlaceholderText(_translate("Dialog", "Enter User ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Admin"))
        self.feedback.setText(_translate("Dialog", "Feedback"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "User"))
        self.label_2.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI Light\'; font-size:18pt; font-weight:168; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Face Expression Recognition Using CNN</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Main(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
