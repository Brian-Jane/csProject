import sys
import os
from PyQt5 import QtWidgets,QtGui
import datetime
import mysql.connector as m

from Libraries.Tasks import *

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
    if row is None: layout.addWidget(Label)
    else: layout.addWidget(Label,row,column)
    Label.setFont(FONT)

def genLineEdit(layout:QtWidgets.QBoxLayout, row:int=None, column:int=None):
    LineEdit=QtWidgets.QLineEdit()
    if (row,column)==(None,None): layout.addWidget(LineEdit)
    else: layout.addWidget(LineEdit,row,column)
    LineEdit.setFont(FONT)
    return LineEdit

def newWindow(nWindow:QtWidgets.QMainWindow, cWindow:QtWidgets.QMainWindow=None, close:bool=False):
    #If close is True, this function will close the current window
    n_instance=nWindow()
    if close:
        c_instance=cWindow()
        c_instance.close()
        n_instance.show()
    else:
        n_instance.show()

def enterRow(layout:QtWidgets.QBoxLayout, task:taskobject,
             spacer:QtWidgets.QSpacerItem=None):
    if task==None:
        print("Task contains nothing! Try avoiding repeating tasks")
        return None
    if type(layout)!=QtWidgets.QGridLayout: 
        print("you can use this function only for GridLayout \
              Try again")
        return None
    slno=task.slno
    priority=task.priority
    DueDate=task.dueDate
    folder=task.folder

    if not spacer:
        genLabel(str(slno),layout,slno,0)
        genCheckbox(task,layout,slno,2)
        genLabel(str(priority),layout,slno,4)
        genLabel(str(DueDate),layout,slno,6)
        genLabel(folder,layout,slno,8)
    else:
        layout.removeItem(spacer)
        genLabel(str(slno),layout,slno,0)
        genCheckbox(task,layout,slno,2)
        genLabel(str(priority),layout,slno,4)
        genLabel(str(DueDate),layout,slno,6)
        genLabel(folder,layout,slno,8)
        spacer=QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacer,slno+1,0)
        
    



def loadUI(main_layout:QtWidgets.QLayout, Tlayout:QtWidgets.QLayout, Flayout:QtWidgets.QLayout):   #This function is not yet complete. Kindly ignore
    #Tasks
    Tasks=t.fetchall()
    for i in Tasks:
        enterRow(Tlayout,i[2],i[3],i[4],i[5])
 
"""Have to do the same for folders too"""
