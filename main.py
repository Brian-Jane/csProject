#from TRIALS.untitled import *
import Mainwindow as mw

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as connector

from Libraries import Tasks
from Libraries import GUIFunc as Gui

import sys
import json

app = QtWidgets.QApplication(sys.argv)
with open('config.json','r') as file:
    config = json.load(file)
mycon = connector.connect(user='root',host='localhost',
                          password=config['password'],
                          database=config['database'])

class MyyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mw.MainUi_MainWindow()
        self.ui.setupUi(self)
        self.renderTasks(self,filter)
        self.tasks = Tasks.Tasks(mycon)
        self.stackedWidgetPage = 0

    def renderTasks(self,layout,filter=Tasks.Filter()):
        """displays all tasks in the given input layout"""
        L = self.tasks.fetchall(filter)
        for task in L:
            Gui.enterRow(layout,task)
        
    
MainWindow = MyyMainWindow()


MainWindow.show()
sys.exit(app.exec_())
