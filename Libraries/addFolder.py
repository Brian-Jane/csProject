import sys
from PyQt5 import QtWidgets,QtGui
from Tasks import Tasks,taskobject
import time
import GUIFunc as G
import mysql.connector as m
import datetime
import pprint
import json

class addFolderWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Folder")
        self.setGeometry(500, 100, 500,500)
        self.mainLayout=QtWidgets.QGridLayout()
        G.genLabel("Add folder name: ",self.mainLayout,0,0)
        G.genLineEdit(self.mainLayout,0,1)
        G.genLabel("Add Colour",self.mainLayout,1,0)
        G.genComboBox(['None'],self.mainLayout,1,1)
        
        self.setLayout(self.mainLayout)

app = QtWidgets.QApplication(sys.argv)

window = addFolderWindow()

window.show()

sys.exit(app.exec_())

