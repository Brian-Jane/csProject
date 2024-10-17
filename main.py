#from TRIALS.untitled import *
import GUI.Mainwindow as mw

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette,QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyleFactory
import mysql.connector as connector
from datetime import datetime,timedelta

from Libraries import Tasks
from Libraries import Gui
from addFolder import addFolderWindow
from addFilter import addFilter

from WindowForTasks import TasksWindow
import sys
import json

qApp = QtWidgets.QApplication(sys.argv)
qApp.setStyle("Fusion")

dark_palette = QPalette()
WHITE = QColor(255,255,255)
RED = QColor(255,0,0)
BLACK = QColor(0,0,0)
dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, WHITE)
dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, WHITE)
dark_palette.setColor(QPalette.ToolTipText, WHITE)
dark_palette.setColor(QPalette.Text, WHITE)
dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ButtonText, WHITE)
dark_palette.setColor(QPalette.BrightText, RED)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, BLACK)

qApp.setPalette(dark_palette)

qApp.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
config = {}
with open('config.json','r') as file:
    config = json.loads(file.read())
print(config)

mycon = connector.connect(user='root',host='localhost',
                          password=config['password'],
                          database=config['database'])
class TasksPage:
    def __init__(self,tasksLayout:QtWidgets.QBoxLayout,foldersLayout,filterLayout,folderbttn,completedTasksbttn,filterbttn,
                 searchBar,searchbttn,todaybttn):
        self.tasksLayout = tasksLayout
        self.foldersLayout = foldersLayout
        self.filterLayout = filterLayout
        self.folderbttn = folderbttn
        self.completedTasksbttn = completedTasksbttn
        self.filterbttn = filterbttn
        self.searchBar = searchBar
        self.filter2 = Tasks.Filter()
        self.tasks = Tasks.Tasks(mycon)

        self.filter = Tasks.Filter()
        self.filter.completedTask(False)
        self.order_by = "Tasks.slno"
        def filter_toggled(checked):
            if checked:
                x = addFilter(self.filter2)
                if x.exec_():
                    self.filter2 = x.filter
                    self.refreshTasks()
            else:
                self.filter2 = Tasks.Filter()
                self.refreshTasks()

        self.filterbttn.toggled.connect(filter_toggled)
        def taskButtonClicked(order_by):
            self.order_by=order_by
            self.refreshTasks()
        Gui.genTasksLayout(tasksLayout,taskButtonClicked)
        def addButtonSlot():
            folderList = [i[0] for i in self.tasks.fetchFolders()]
            x = addFolderWindow(folderList)
            a = x.exec_()
            if a:
                print("SJsjsj")
                newFolder = x.newFolder
                self.tasks.addFolder(newFolder[0],newFolder[1])
                self.refreshFolders()

        folderbttn.clicked.connect(addButtonSlot)
        self.folderButtonGroup = QtWidgets.QButtonGroup()
        self.folderButtonGroup.setExclusive(True)
        Nonebttn = QtWidgets.QPushButton("None")
        Nonebttn.setCheckable(True)
        Nonebttn.setChecked(True)
        Nonebttn.clicked.connect(self.on_Nonebttn_clicked)
        foldersLayout.addWidget(Nonebttn)
        self.folderButtonGroup.addButton(Nonebttn)

        def completedTasksCallback(checked):
            self.filter.completedTask(checked)
            self.refreshTasks()
        completedTasksbttn.toggled.connect(completedTasksCallback)
        def searchTask(checked:bool):
            if checked:
                msg = self.searchBar.text()
                self.filter.searchMsg(msg)
            else:
                try:self.filter.undo(self.filter.searchMsg)
                except:pass
            self.refreshTasks()
        def searchTaskByPressingEnter():
            x = bool(searchBar.text())
            searchbttn.setChecked(x)
            searchTask(x)

        searchbttn.toggled.connect(searchTask)
        searchBar.returnPressed.connect(searchTaskByPressingEnter)

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
            if not self.filter.param[self.filter.completedTask]:self.tasks.completeTask(ID)
            else:self.tasks.redoTask(ID)
            self.refreshTasks()
        L = self.tasks.fetchall(order_by=self.order_by,filter=self.filter,filter2=self.filter2)

        def delete_handler(task:Tasks.Tasks,taskobject:Tasks.taskobject):
            if not (taskobject) : raise ValueError
            task.delTask(taskobject.slno)
            self.refreshTasks()

        def modify_handler(task:Tasks.Tasks,taskobject:Tasks.taskobject):
            print("Received taskobject:", taskobject)
            if not (taskobject) : raise TypeError
            self.TW=TasksWindow(task,self.refreshTasks,taskobject,[i[0] for i in self.tasks.fetchFolders()])
            self.TW.show()
            self.refreshTasks()

      
        L = self.tasks.fetchall(order_by=self.order_by,filter=self.filter)
        for task in L:
            ID = task.ID
            Gui.enterRow(self.tasksLayout,task, 
                         lambda clicked,ID=ID :taskCheckboxCallback(ID),        
                         lambda a,b=task: delete_handler(self.tasks, b),  
                         color=task.color,modify_handler=lambda a,b=task:modify_handler(self.tasks,b))
    
             
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
                              self.ui.addFolderbttn,self.ui.CompletedTasks,self.ui.filter,
                              self.ui.SearchBar,self.ui.searchBttn,self.ui.Today)
 

    def on_AllTasksButton_released(self):
        allTasksIndex = self.stackedWidgetPages["AllTasks"]
        self.ui.stackedWidget.setCurrentIndex(allTasksIndex)
        self.refreshTasks(self.ui.AllTasks_GridLayout)

        

    def on_FoldersButton_released(self):
        foldersIndex = self.stackedWidgetPages["Folders"]
        self.ui.stackedWidget.setCurrentIndex(foldersIndex)   

    def connectSlotsByName(self):
        # Automatically connect signals to slots based on naming convention
        super().connectSlotsByName()

    def on_addTasbkttn_released(self):
        folderList = [i[0] for i in self.tasks.fetchFolders()]
        self.TaskWindow=TasksWindow(self.tasks,self.tasksPage.refreshTasks,folderList=folderList)
        self.TaskWindow.show()

    def on_refreshBttn_clicked(self):
        self.tasksPage.refreshAll()


MainWindow = MyyMainWindow()


MainWindow.show()
sys.exit(qApp.exec_())
