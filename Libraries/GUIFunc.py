import sys
import os
from PyQt5 import QtWidgets,QtGui
import datetime
import mysql.connector as m

from Tasks import *

FONT= QtGui.QFont()
FONT.setPointSize(10)
conn=m.connect(user='root',host='LocalHost',database='csp', password='0000')

t=Tasks(conn)
iT=info(conn,Table="Tasks")
iF=info(conn,Table='Folders')

def genCheckbox(data:str,layout:QtWidgets.QBoxLayout, row:int,column:int):
    checkbox=QtWidgets.QCheckBox(data)
    checkbox.clicked.connect(lambda:checkbox_clicked(checkbox))
    checkbox.setFont(FONT)

    layout.addWidget(checkbox,row,column)

def checkbox_clicked(checkbox:QtWidgets.QCheckBox):
    print(checkbox.text(),"is clicked!")
    t.completeTask(iT.ID(checkbox.text()))

def genLabel(data,layout:QtWidgets.QBoxLayout, row:int=None, column:int=None):
    Label=QtWidgets.QLabel(data)
    if type(row)==None: layout.addWidget(Label)
    else: layout.addWidget(Label,row,column)
    Label.setFont(FONT)

def enterRow(layout:QtWidgets.QBoxLayout, task:str, priority:int=5, DueDate:datetime.datetime=None, folder:str='',colorhex:str="#888888"):
    t.addTask(msg=task, priority=priority, dt=DueDate, folder=folder)
    if folder:
        folders=t.fetchFolders()
        if (folder,colorhex) not in folders: t.addFolder(folder)
    ID=iT.ID(task)
    slno=iT.slno(ID)

    genLabel(str(slno),layout,slno,0)
    genCheckbox(task,layout,slno,2)
    genLabel(str(priority),layout,slno,4)
    genLabel(str(DueDate),layout,slno,6)
    genLabel(folder,layout,slno,8)

def new_windowbttn(current_window: QtWidgets.QMainWindow, new_window: QtWidgets.QMainWindow):
    if not new_window.isVisible():  # Check if the window is not currently visible
        new_window.show()  # Show the new window
    
def loadUI(main_layout:QtWidgets.QLayout, layout:QtWidgets.QLayout):   
    #Tasks
    Tasks=t.fetchall()
    for i in Tasks:
        enterRow(layout,i[2],i[3],i[4],i[5])
 
"""Have to do the same for folders too"""
