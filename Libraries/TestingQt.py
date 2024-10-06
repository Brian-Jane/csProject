import sys
from PyQt5 import QtWidgets
import GUIFunc as G
import mysql.connector as m
from Tasks import *
conn=m.connect(user="root",host="LocalHost",database="csp",password="0000")
a=Tasks(conn)

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mainwindow")
        self.setGeometry(500, 100, 908, 753)
        self.Layout=QtWidgets.QGridLayout()
        G.enterRow(self.Layout,"Task-3",1,datetime.datetime(2024,10,2), folder="Folder-4")
        self.bttn=QtWidgets.QPushButton(text="press")
        self.bttn.clicked.connect(lambda: G.newWindow(newWindow))
        self.Layout.addWidget(self.bttn)
        self.setLayout(self.Layout)

        self.new_window_instance = None



class newWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mainwindow")
        self.setGeometry(500, 100, 908, 753)
        self.Layout=QtWidgets.QHBoxLayout()
        G.genLabel("Add Task ",self.Layout)
        self.textbox=G.genLineEdit(self.Layout)
        
        self.bttn=QtWidgets.QPushButton(text="Submit")
        self.bttn.clicked.connect(lambda: self.submit_task(self.textbox))
        self.Layout.addWidget(self.bttn)
        self.setLayout(self.Layout)

    def submit_task(self,LineEdit:QtWidgets.QLineEdit):
        a.addTask(LineEdit.text())
        print("submit clicked")



app = QtWidgets.QApplication(sys.argv)

window = MyWindow()

window.show()

sys.exit(app.exec_())