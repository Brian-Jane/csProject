import sys
import os
from PyQt5 import QtWidgets,QtGui
import datetime
import mysql.connector as m

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

def genLabel(data,layout:QtWidgets.QBoxLayout, row:int=None, column:int=None):
    Label=QtWidgets.QLabel(data)
    if row is None: layout.addWidget(Label)
    else: layout.addWidget(Label,row,column)
    Label.setFont(FONT)
    return Label

def genLineEdit(layout:QtWidgets.QBoxLayout, row:int=None, column:int=None):
    LineEdit=QtWidgets.QLineEdit()
    if (row,column)==(None,None): layout.addWidget(LineEdit)
    else: layout.addWidget(LineEdit,row,column)
    LineEdit.setFont(FONT)
    return LineEdit

def genRadioBttn(data,layout:QtWidgets.QBoxLayout,row:int=None,column:int=None):
    global What_is_clicked
    What_is_clicked=None
    Radiobttn=QtWidgets.QRadioButton(str(data))
    Radiobttn.setFont(FONT)
    Radiobttn.clicked.connect(lambda: radioBttn_clicked(Radiobttn))
    if row is None: layout.addWidget(Radiobttn)
    else: layout.addWidget(Radiobttn,row,column)

    return (Radiobttn,What_is_clicked)

def radioBttn_clicked(RadioBttn:QtWidgets.QRadioButton):
    global What_is_clicked
    What_is_clicked=RadioBttn


def newWindow(nWindow:QtWidgets.QMainWindow, cWindow:QtWidgets.QMainWindow=None, close:bool=False):
    #If close is True, this function will close the current window
    n_instance=nWindow()
    if close:
        c_instance=cWindow()
        c_instance.close()
        n_instance.show()
    else:
        n_instance.show()


def genComboBox(List:list,layout:QtWidgets.QBoxLayout, row:int=None, column:int=None):
    combo=QtWidgets.QComboBox()
    for i in List:
        combo.addItem(str(i))

    if row!=None: layout.addWidget(combo,row,column)
    elif row==None: layout.addWidget(combo)
    combo.setFont(FONT)

    return combo



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




def produceError(errormsg):
    e=ErrorWindow(errormsg)
    e.show()

class ErrorWindow(QtWidgets.QWidget):
    def __init__(self, error:str):
        super().__init__()
        self.setWindowTitle("Error")
        self.setGeometry(700, 200, 380,200)
        l=QtWidgets.QGridLayout()
        genLabel(error,l,0,0)
        bttn=QtWidgets.QPushButton("OK")
        bttn.clicked.connect(lambda: self.close())
        l.addWidget(bttn,1,0)

        self.setLayout(l)