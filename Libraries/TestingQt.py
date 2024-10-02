import sys
from PyQt5 import QtWidgets
import GUIFunc as G
import mysql.connector as m
from Tasks import *
conn=m.connect(user="root",host="LocalHost",database="csp",password="0000")
a=Tasks(conn)
i=info(conn,"Folders")
class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mainwindow")
        self.setGeometry(500, 100, 908, 753)
        self.Layout=QtWidgets.QGridLayout()
        G.enterRow(self.Layout,"Task-3",1,datetime.datetime(2024,10,2), folder="Folder-1")
        self.bttn=QtWidgets.QPushButton(text="press")
        self.bttn.clicked.connect(lambda: self.press_clicked(self.Layout))
        self.Layout.addWidget(self.bttn)
        self.setLayout(self.Layout)

    def press_clicked(self,Layout):
        G.enterRow(Layout,"Task-5",folder="Folder-5")

app = QtWidgets.QApplication(sys.argv)

window = MyWindow()

window.show()

sys.exit(app.exec_())