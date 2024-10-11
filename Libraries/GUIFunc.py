import sys
import os
from PyQt5 import QtWidgets,QtGui
import datetime
import mysql.connector as m
from typing import Union

from Tasks import *

FONT= QtGui.QFont()
FONT.setPointSize(10)

HEADINGFONT= QtGui.QFont()
HEADINGFONT.setPointSize(10)
HEADINGFONT.setBold(True)

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

def genLabel(data,layout:QtWidgets.QBoxLayout, row:int=None, column:int=None,
             l:list=None):
    Label=QtWidgets.QLabel(data)
    if row is None: layout.addWidget(Label)
    else: layout.addWidget(Label,row,column)
    Label.setFont(FONT)
    if l: l.append(Label)
    return Label

def genLineEdit(layout:QtWidgets.QBoxLayout, row:int=None, column:int=None):
    LineEdit=QtWidgets.QLineEdit()
    if (row,column)==(None,None): layout.addWidget(LineEdit)
    else: layout.addWidget(LineEdit,row,column)
    LineEdit.setFont(FONT)
    return LineEdit

def genRadioBttn(data,layout:QtWidgets.QBoxLayout,row:int=None,column:int=None, bttngrp:QtWidgets.QButtonGroup=None,
                 l:list=None):

    Radiobttn=QtWidgets.QRadioButton(str(data))
    Radiobttn.setFont(FONT)
    if row is None: layout.addWidget(Radiobttn)
    else: layout.addWidget(Radiobttn,row,column)
    bttngrp.addButton(Radiobttn)

    if l: l.append(Radiobttn)
    return Radiobttn


def newWindow(nWindow:QtWidgets.QMainWindow, cWindow:QtWidgets.QMainWindow=None, close:bool=False):
    #If close is True, this function will close the current window
    n_instance=nWindow()
    if close:
        c_instance=cWindow()
        c_instance.close()
        n_instance.show()
    else:
        n_instance.show()


def genComboBox(Items:list,layout:QtWidgets.QBoxLayout, row:int=None, column:int=None,
                l:list=None):   
    combo=QtWidgets.QComboBox()
    for i in Items:
        combo.addItem(str(i))

    if row!=None: layout.addWidget(combo,row,column)
    elif row==None: layout.addWidget(combo)
    combo.setFont(FONT)

    if l: l.append(combo)
    return combo

def genLine(Layout:QtWidgets.QBoxLayout, orientation:str='v', row:int=None, column:int=None, rspan:int=None, cspan:int=None):
    if orientation=='v':    #Vertical Line
        vertical_line = QtWidgets.QFrame()
        vertical_line.setFrameShape(QtWidgets.QFrame.VLine)
        if row!=None:
            Layout.addWidget(vertical_line, row, column) 

        return vertical_line

    elif orientation=='h':   #Horizontal Line
        horizontal_line = QtWidgets.QFrame()
        horizontal_line.setFrameShape(QtWidgets.QFrame.HLine)
        if row!=None:
            Layout.addWidget(horizontal_line, row, column) 
    
        return horizontal_line

def hideLayout(Layout:QtWidgets.QBoxLayout):
    for i in range(Layout.count()):
        item=Layout.itemAt(i)
        widget = item.widget()
        if widget is not None:
            widget.setVisible(False)



def enterRow(layout:QtWidgets.QBoxLayout, task:taskobject,
             spacer:QtWidgets.QSpacerItem=None):
    if task==None:
        print("Task contains nothing! Try avoiding repeating tasks")
        return None
    if type(layout)!=QtWidgets.QGridLayout: 
        print("you can use this function only for GridLayout \
              Try again")
        return None
    ID=task.ID
    slno=task.slno
    priority=task.priority
    DueDate=task.dueDate
    folder=task.folder

    if not spacer:
        genLabel(str(slno),layout,ID,0)
        genCheckbox(task,layout,ID,2)
        genLabel(str(priority),layout,ID,4)
        genLabel(str(DueDate),layout,ID,6)
        genLabel(folder,layout,ID,8)
    else:
        layout.removeItem(spacer)
        genLabel(str(slno),layout,ID,0)
        genCheckbox(task,layout,ID,2)
        genLabel(str(priority),layout,ID,4)
        genLabel(str(DueDate),layout,ID,6)
        genLabel(folder,layout,ID,8)
        spacer=QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacer,ID+1,0)
        
    



def re_add(W:QtWidgets.QWidget,Layout:QtWidgets.QGridLayout,row,column,
           cspan:int=None, rspan:int=None):
    Layout.removeWidget(W)
    if cspan is None and rspan is None: Layout.addWidget(W,row,column)
    if cspan is not None and rspan is None: Layout.addWidget(W,row,column,columnSpan=cspan)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

#Generating the mainGridLayout

def genTasksLayout(window:QtWidgets.QMainWindow):
    tasksLayout=QtWidgets.QGridLayout()
    for i in range(8):      #A vertical line is drawn at evry odd column
        if i%2!=0:
            genLine(tasksLayout,orientation='v',row=0,column=i)
    
    def checkableBttn(text:str, column):
        bttn=QtWidgets.QPushButton(text)
        bttn.setCheckable(True)
        bttn.setFlat(True)
        bttn.setFont(HEADINGFONT)
        tasksLayout.addWidget(bttn,0,column)

    checkableBttn('Slno',0)
    checkableBttn('Task',2)
    checkableBttn('Priority',4)
    checkableBttn('Due date', 6)
    checkableBttn('Folder',8)

    spacer=QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    tasksLayout.addItem(spacer,1,0)

    window.setLayout(tasksLayout)

    return tasksLayout






#------------------------------------------------------------------------------------------------------------------------------------------------------------
def produceError(errormsg):
    e=ErrorWindow(errormsg)
    e.show()

class ErrorWindow(QtWidgets.QWidget):
    def __init__(self, error:str):
        super().__init__()
        self.setWindowTitle("Error")
        self.setGeometry(700, 200, 500,200)
        l=QtWidgets.QGridLayout()
        genLabel(error,l,0,0)
        bttn=QtWidgets.QPushButton("OK")
        bttn.setFont(FONT)
        bttn.clicked.connect(lambda: self.close())
        l.addWidget(bttn,1,0)

        self.setLayout(l)