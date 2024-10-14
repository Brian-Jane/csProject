#from TRIALS.untitled import *
import GUI.Mainwindow as mw

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as connector
from datetime import datetime,timedelta

from Libraries import Tasks
from Libraries import Gui

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
class TasksPage:
    def __init__(self,tasksLayout,foldersLayout,filterLayout,folderbttn,filterbttn,taskbttns,
                 searchBar,searchbttn,todaybttn):
        self.tasksLayout = tasksLayout
        self.foldersLayout = foldersLayout
        self.filterLayout = filterLayout
        self.folderbttn = folderbttn
        self.filterbttn = filterbttn
        self.taskbttns = taskbttns
        self.searchBar = searchBar

        self.tasks = Tasks.Tasks(mycon)

        self.filter = Tasks.Filter()
        self.filter.completedTask(False)
        self.order_by = "Tasks.slno"
        def taskButtonClicked(order_by):
            self.order_by=order_by
            self.refreshTasks()
        Gui.genTasksLayout(tasksLayout,taskButtonClicked)

        self.folderButtonGroup = QtWidgets.QButtonGroup()
        self.folderButtonGroup.setExclusive(True)
        Nonebttn = QtWidgets.QPushButton("None")
        Nonebttn.setCheckable(True)
        Nonebttn.setChecked(True)
        Nonebttn.clicked.connect(self.on_Nonebttn_clicked)
        foldersLayout.addWidget(Nonebttn)
        self.folderButtonGroup.addButton(Nonebttn)
        
        taskButtonGroup = QtWidgets.QButtonGroup()
        taskButtonGroup.setExclusive(True)
        
        def searchTask(checked:bool):
            if searchbttn.isChecked() ^ checked:
                searchbttn.setChecked(checked)
            if checked:
                msg = self.searchBar.text()
                self.filter.searchMsg(msg)
            else:
                try:self.filter.undo(self.filter.searchMsg)
                except:pass
            self.refreshTasks()
        searchbttn.toggled.connect(searchTask)
        searchBar.returnPressed.connect(lambda:searchTask(True))

        def today(checked:bool):
            if checked:self.filter.dateBefore(datetime.now()+timedelta(days=1))
            else:
                try:self.filter.undo(self.filter.dateBefore)
                except:pass
            self.refreshTasks()

        todaybttn.toggled.connect(today)
        self.renderFolders()
        self.renderTasks()
    
    def on_Nonebttn_clicked(self):
        try:
            self.filter.undo(self.filter.folder)
        except:pass
        self.refreshTasks()

    def renderTasks(self):
        """displays all tasks in the given input layout"""
        layout = self.tasksLayout
        def taskCheckboxCallback(ID):
            self.tasks.completeTask(ID)
            self.refreshTasks()

        L = self.tasks.fetchall(order_by=self.order_by,filter=self.filter)
        for task in L:
            ID = task.ID
            Gui.enterRow(layout,task,
                         lambda clicked,ID=ID :taskCheckboxCallback(ID),
                         color=task.color)
    def refreshTasks(self):
        layout = self.tasksLayout
        self.tasks.refresh()
        for i in range(1,layout.rowCount()-1):
            Gui.deleteRow(layout,i)
        self.renderTasks()

    def renderFolders(self):
        L = self.tasks.fetchFolders()
        layout = self.foldersLayout
        buttonGroup = self.folderButtonGroup
        def editCallback(old_name,text,color):
            self.tasks.updateFolder(old_name,text,color)
            self.refreshFolders()
            self.refreshTasks()
        def selectCallback(name):
            self.filter.folder(name)
            self.refreshTasks()
        def deleteCallback(name):
            self.on_Nonebttn_clicked()
            self.tasks.delFolder(name)
            self.refreshFolders()
            self.refreshTasks()
        for i in L:
            x = Gui.Folder(i[0],i[1],lambda text,color,n=i[0]:editCallback(n,text,color),
                       lambda a,n=i[0]:selectCallback(n),lambda a,n=i[0]:deleteCallback(n),buttonGroup)
            layout.addWidget(x)

    def refreshFolders(self):
        layout = self.foldersLayout
        for i in range(layout.count()-1,0,-1):
            item = layout.takeAt(i)
            widget = item.widget()
            if widget: 
                widget.deleteLater()
        self.renderFolders()
    
    def refreshAll(self):
        self.refreshFolders()
        self.refreshTasks()
    
class MyyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mw.Ui_MainWindow()
        self.ui.setupUi(self)
        self.tasks = Tasks.Tasks(mycon)
        self.stackedWidgetIndex = 0
        self.stackedWidgetPages = {"Folders":0,"AllTasks":1}
        """taskButtonDict = {self.ui.Slno:"Tasks.slno",
                          self.ui.Priority:"Tasks.priority",self.ui.DueDate:"Tasks.dt",
                          self.ui.Folder:"Tasks.folder"}"""
        self.tasksPage = TasksPage(self.ui.AllTasks_GridLayout,
                              self.ui.scrollAreaWidgetContents.layout(),
                              self.ui.scrollAreaWidgetContents_2.layout(),
                              self.ui.addFolderbttn,None,None,
                              self.ui.SearchBar,self.ui.searchBttn,self.ui.Today)

    def on_AllTasksButton_released(self):
        allTasksIndex = self.stackedWidgetPages["AllTasks"]
        self.ui.stackedWidget.setCurrentIndex(allTasksIndex)
        self.refreshTasks(self.ui.AllTasks_GridLayout)

    def on_FoldersButton_released(self):
        foldersIndex = self.stackedWidgetPages["Folders"]
        self.ui.stackedWidget.setCurrentIndex(foldersIndex)    

MainWindow = MyyMainWindow()


MainWindow.show()
sys.exit(app.exec_())
