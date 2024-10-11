#from TRIALS.untitled import *
import GUI.Mainwindow as mw

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as connector

from Libraries import Tasks
from Libraries import GUIFunc as Gui

import sys
import json

app = QtWidgets.QApplication(sys.argv)
config = {}
with open('config.json','r') as file:
    config = json.loads(file.read())
print(config)

mycon = connector.connect(user='root',host='localhost',
                          password=config['password'],
                          database=config['database'])

class MyyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mw.Ui_MainWindow()
        self.ui.setupUi(self)
        self.tasks = Tasks.Tasks(mycon)
        self.stackedWidgetIndex = 0
        self.stackedWidgetPages = {"Folders":0,"AllTasks":1}
        self.filter = Tasks.Filter()
        self.filter.completedTask(False)
        
        self.renderTasks(self.ui.AllTasks_GridLayout)

    def on_AllTasksButton_released(self):
        allTasksIndex = self.stackedWidgetPages["AllTasks"]
        self.ui.stackedWidget.setCurrentIndex(allTasksIndex)
        self.refreshTasks(self.ui.AllTasks_GridLayout)

    def on_FoldersButton_released(self):
        foldersIndex = self.stackedWidgetPages["Folders"]
        self.ui.stackedWidget.setCurrentIndex(foldersIndex)
        
    def renderTasks(self,layout):
        """displays all tasks in the given input layout"""
        L = self.tasks.fetchall(filter=self.filter)
        for task in L:
            ID = task.ID
            Gui.enterRow(layout,task,
                         lambda clicked,ID=ID :self.taskCheckboxCallback(layout,ID),
                         spacer=True)
            #spent like... 30 mins trying to figure why this ID argument was
            #"true" every time instead of ID, turns out the signal of a checkbox
            #includes a "clicked" argument which overwrote the ID default arguemnt....so
            #time well spent ig.... 

    def taskCheckboxCallback(self,layout:QtWidgets.QGridLayout,
                            ID):
        self.tasks.completeTask(ID)
        self.refreshTasks(layout)

    def refreshTasks(self,layout):
        self.tasks.refresh()
        for i in range(1,layout.rowCount()-1):
            Gui.deleteRow(layout,i)
        self.renderTasks(layout)
            
MainWindow = MyyMainWindow()


MainWindow.show()
sys.exit(app.exec_())
