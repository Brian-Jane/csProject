from PyQt5.QtCore import Qt
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

def genCheckbox(data:str,layout:QtWidgets.QBoxLayout, row:int,column:int):
    checkbox=QtWidgets.QCheckBox(data)
    checkbox.clicked.connect(lambda:checkbox_clicked(checkbox))
    checkbox.setFont(FONT)

    layout.addWidget(checkbox,row,column)

def checkbox_clicked(checkbox:QtWidgets.QCheckBox):
    L=t.fetchall()
    print(checkbox.text(),"is clicked!")
    t.completeTask(L.ID(checkbox.text()))

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

def genLine(layout:QtWidgets.QBoxLayout, orientation:str='v', r:int=None, c:int=None):
    if orientation.lower()=='v':
        Line=QtWidgets.QFrame()
        Line.setFrameShape(QtWidgets.QFrame.VLine)
        if r: layout.addWidget(Line,row=r,column=c,columnspan=4)
        else: layout.addWidget(Line)
    if orientation.lower()=='h':
        Line=QtWidgets.QFrame()
        Line.setFrameShape(QtWidgets.QFrame.HLine)
        layout.addWidget(Line)

def newWindow(nWindow:QtWidgets.QMainWindow, cWindow:QtWidgets.QMainWindow=None, close:bool=False):
    n_instance=nWindow()
    if close:
        c_instance=cWindow()
        c_instance.close()
        n_instance.show()
    else:
        n_instance.show()

def enterRow(layout:QtWidgets.QBoxLayout, task:str, priority:int=5, DueDate:datetime.datetime=None, folder:str='',colorhex:str="#888888",
             spacer:QtWidgets.QSpacerItem=None):
    slno=newSlno()

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
    
def newSlno():
    L=t.fetchall()
    return L[-1].slno +1


def loadUI(main_layout:QtWidgets.QLayout, Tlayout:QtWidgets.QLayout, Flayout:QtWidgets.QLayout):   #This function is not yet complete. Kindly ignore
    #Tasks
    Tasks=t.fetchall()
    for i in Tasks:
        enterRow(Tlayout,i[2],i[3],i[4],i[5])

    """Folders=t.fetchFolders()
    for i in Folders:
        f=i[0]  
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Tasks WHERE Folder=%s",(f,))
            r=cur.fetchall()
            for i in r:
                enterRow(Flayout)"""
 
"""Have to do the same for folders too"""


#This function is ALSO not yet completed. Kindly ignore
'''
def createlayout(Mainwindow:QtWidgets.QMainWindow,widget:QtWidgets.QWidget):
    m=Mainwindow
    Layout=QtWidgets.QGridLayout()
    
    if type(widget)==QtWidgets.QStackedWidget:
        m.page1 = QtWidgets.QWidget()
        
        Headingfont=QtGui.QFont()
        Headingfont.setBold(True)
        Headingfont.setPointSize(10)

        slno=genLabel("slno",Layout,0,0)
        genLine(Layout,r=0,c=1)
        slno.setFont(Headingfont)
        

        Task=genLabel("Task",Layout,0,2)
        genLine(Layout,r=0,c=13)
        Task.setFont(Headingfont)
        

        P=genLabel("Priority",Layout,0,4)
        genLine(Layout,r=0,c=5)
        P.setFont(Headingfont)
       

        dt=genLabel("Due Date",Layout,0,6)
        genLine(Layout,r=0,c=7)
        dt.setFont(Headingfont)
        

        f=genLabel("Folder",Layout,0,8)
        f.setFont(Headingfont)

        addSpacer(Layout,1,0)

        m.page1.setLayout(Layout)

        #Adding page to the stacked widget
        widget.addWidget(m.page1)

        
def addSpacer(Layout:QtWidgets.QBoxLayout,row:int=None,column:int=None):
    spacer= QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    Layout.addItem(spacer)
    if (row,column)==(None,None): Layout.addItem(spacer)
    else: Layout.addItem(spacer,row,column)
'''
