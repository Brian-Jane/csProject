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
def genCheckbox(task:taskobject,layout:QtWidgets.QBoxLayout, row:int,column:int):
    checkbox=QtWidgets.QCheckBox(task.msg)
    checkbox.clicked.connect(lambda:checkbox_clicked(checkbox,task))
    checkbox.setFont(FONT)

    layout.addWidget(checkbox,row,column)

def checkbox_clicked(checkbox:QtWidgets.QCheckBox,task:taskobject):
    print(checkbox.text(),"is clicked!")
    t.completeTask(task.ID)

def genLabel(data,layout:QtWidgets.QBoxLayout, row:int=None, column:int=None):
    Label=QtWidgets.QLabel(data)
    if type(row)==None: layout.addWidget(Label)
    else: layout.addWidget(Label,row,column)
    Label.setFont(FONT)

def enterRow(layout:QtWidgets.QBoxLayout, task:taskobject):

    genLabel(str(task.slno),layout,task.slno,0)
    genCheckbox(task,layout,task.slno,2)
    genLabel(str(task.priority),layout,task.slno,4)
    genLabel(str(task.DueDate),layout,task.slno,6)
    genLabel(task.folder,layout,task.slno,8)

def new_windowbttn(current_window: QtWidgets.QMainWindow, new_window: QtWidgets.QMainWindow):
    if not new_window.isVisible():  # Check if the window is not currently visible
        new_window.show()  # Show the new window
    
def loadUI(main_layout:QtWidgets.QLayout, layout:QtWidgets.QLayout):   
    #Tasks
    Tasks=t.fetchall()
    for i in Tasks:
        enterRow(layout,i[2],i[3],i[4],i[5])
 
"""Have to do the same for folders too"""
