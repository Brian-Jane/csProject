from PyQt5 import QtWidgets, QtGui
from Libraries.Tasks import *
import datetime
import mysql.connector as m

FONT= QtGui.QFont()
FONT.setPointSize(10)
conn=m.connect(user='root',host='LocalHost',database='csp', password='0000')

def genCheckbox(data:str,layout:QtWidgets.QBoxLayout, row:int,column):
    checkbox=QtWidgets.QCheckBox(data)
    checkbox.clicked.connect(lambda:checkbox_clicked(checkbox))
    checkbox.setFont(FONT)

    layout.addWidget(checkbox,row,column)
    def checkbox_clicked(checkbox:QtWidgets.QCheckBox):
        print(checkbox.text())

def genLabel(data,layout:QtWidgets.QBoxLayout, row:int=None, column:int=None):
    Label=QtWidgets.QLabel(data)
    if type(row)==None: layout.addWidget(Label)
    else: layout.addWidget(Label,row,column)
    Label.setFont(FONT)

def enterRow(layout:QtWidgets.QBoxLayout, task:str, priority:int=5, DueDate:datetime.datetime=None, folder:str=''):
    t=Tasks(conn)
    t.addTask(msg=task, priority=priority, dt=DueDate, folder=folder)
    i=info(conn,Table="Tasks")
    ID=i.ID(task)
    slno=i.slno(ID)

    genLabel(str(slno),layout,slno-1,0)
    genCheckbox(task,layout,slno-1,1)
    genLabel(str(priority),layout,slno-1,2)
    genLabel(str(DueDate),layout,slno-1,3)
    genLabel(folder,layout,slno-1,4)




    