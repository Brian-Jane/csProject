import sys
import os
from PyQt5 import QtWidgets,QtGui,QtCore
import datetime
import mysql.connector as m
from typing import Union

from Libraries.Tasks import *

FONT= QtGui.QFont()
FONT.setPointSize(10)

HEADINGFONT= QtGui.QFont()
HEADINGFONT.setPointSize(10)
HEADINGFONT.setBold(True)

'''conn=m.connect(user='root',host='LocalHost',database='csp', password='0000')

t=Tasks(conn)'''

def genCheckbox(task:taskobject,layout:QtWidgets.QBoxLayout, row:int,column:int, T:Tasks):
    checkbox=QtWidgets.QCheckBox(task.msg)
    checkbox.clicked.connect(lambda:checkbox_clicked(checkbox,task,T))
    checkbox.setFont(FONT)

    layout.addWidget(checkbox,row,column)
    return checkbox

def checkbox_clicked(checkbox:QtWidgets.QCheckBox,task:taskobject, T:Tasks):
    print(checkbox.text(),"is clicked!")
    T.completeTask(task.ID)

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


def newWindow(nWindow_instance:QtWidgets.QMainWindow, cWindow_instance:QtWidgets.QMainWindow=None, close:bool=False):
    #If close is True, this function will close the current window
    if close:
        cWindow_instance.close()
        nWindow_instance.show()
    else:
        nWindow_instance.show()


    '''if __name__=='__main__':
        app = QtWidgets.QApplication(sys.argv)

        window = nWindow()

        window.show()

        sys.exit(app.exec_())'''


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
    frameShape = QtWidgets.QFrame.VLine if orientation=='v' else QtWidgets.QFrame.HLine
    vertical_line = QtWidgets.QFrame()
    vertical_line.setFrameShape(QtWidgets.QFrame.VLine)
    if row!=None:
        Layout.addWidget(vertical_line, row, column) 
    return vertical_line

def genSpacer(layout:QtWidgets.QBoxLayout,row:int=None,column:int=None,Orientation='v'):
    if Orientation=='v':
        spacer=QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacer)
        if row!=None: layout.addItem(spacer,row,column)
        elif row==None: layout.addItem(spacer)
    if Orientation=='h':
        spacer=QtWidgets.QSpacerItem(40,20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacer)
        if row!=None: layout.addItem(spacer,row,column)
        elif row==None: layout.addItem(spacer)

    return spacer

def invisible(L:list):
    for widget in L:
        widget.hide()


def widgets_in_layout(Layout:QtWidgets.QBoxLayout,widget_type):
    L=[]
    for i in Layout.findChildren(widget_type):
        L.append(i)

    return L



def hideLayout(Layout:QtWidgets.QBoxLayout):
    for i in range(Layout.count()):
        item=Layout.itemAt(i)
        widget = item.widget()
        if widget is not None:
            widget.setVisible(False)



def enterRow(layout:QtWidgets.QBoxLayout, task:taskobject,
             spacer:bool=True,T:Tasks=None):
    if T is None:
        print("Enter Tasks instance (T)     GUIFunc\Line-141")

    if task==None:
        print("Task contains nothing! Try avoiding repeating tasks      GUIFunc\Line-144")
        return None
    if type(layout)!=QtWidgets.QGridLayout: 
        print("you can use EnterRow function only for GridLayout \
              Try again")
        return None
    ID=task.ID
    slno=task.slno
    priority=task.priority
    DueDate=task.dueDate
    folder=task.folder

    for i in range(8):      #A vertical line is drawn at evry odd column
        if i%2!=0:
            genLine(layout,orientation='v',row=ID,column=i)

    if not spacer:
        for i in range(1,8,2):
            genLine(layout,slno,i)
        genLabel(str(slno),layout,slno,0)

        genCheckbox(task,layout,slno,2,T)
        genLabel(str(priority),layout,slno,4)
        genLabel(str(DueDate),layout,slno,6)
        genLabel(folder,layout,slno,8)
    else:
        lastrow = layout.rowCount()-1
        spacer = layout.itemAtPosition(lastrow,0)
        
        layout.removeItem(spacer)
        for i in range(1,8,2):
            genLine(layout,lastrow,i)
        color = QtGui.QColor(task.color)

        genLabel(str(slno),layout,lastrow,0)
        genCheckbox(task,layout,lastrow,2,T)
        genLabel(str(priority),layout,lastrow,4)
        genLabel(str(DueDate),layout,lastrow,6)
        genLabel(folder,layout,lastrow,8)
        spacer=QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacer,ID+1,0)



def count_spacers(layout):
        spacer_count = 0
        pos=[]
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if isinstance(item, QtWidgets.QSpacerItem):
                spacer_count += 1
                pos.append(i)
        return spacer_count, f"at pos: {pos}"


def re_add(W:QtWidgets.QWidget,Layout:QtWidgets.QGridLayout,row,column,
           cspan:int=None, rspan:int=None):
    Layout.removeWidget(W)
    if cspan is None and rspan is None: Layout.addWidget(W,row,column)
    if cspan is not None and rspan is None: Layout.addWidget(W,row,column,columnSpan=cspan)





#------------------------------------------------------------------------------------------------------------------------------------------------------------

#Generating the mainGridLayout

def genTasksLayout(outer_Layout:Union[QtWidgets.QWidget,QtWidgets.QMainWindow]):
    tasksLayout=QtWidgets.QGridLayout()
    for i in range(8):      #A vertical line is drawn at evry odd column
        if i%2!=0:
            genLine(tasksLayout,orientation='v',row=0,column=i)
    
    bttn_group = QtWidgets.QButtonGroup()

    def checkableBttn(text:str, column):
        bttn=QtWidgets.QPushButton(text)
        bttn.setCheckable(True)
        bttn.setFlat(True)
        bttn.setFont(HEADINGFONT)
        tasksLayout.addWidget(bttn,0,column)
        bttn_group.addButton(bttn)


    checkableBttn('Slno',0)
    checkableBttn('Task',2)
    checkableBttn('Priority',4)
    checkableBttn('Due date', 6)
    checkableBttn('Folder',8)

    spacer=QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    tasksLayout.addItem(spacer,1,0)

    outer_Layout.setLayout(tasksLayout)

    
    print(count_spacers(tasksLayout),"space(s) are there")
    return tasksLayout, spacer


def deleteRow(tasksLayout:QtWidgets.QGridLayout,row:int):
    for column in range(tasksLayout.columnCount()):
            item = tasksLayout.itemAtPosition(row, column)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()  # Delete the widget
                tasksLayout.removeItem(item)


def enterAllTasks(tasklayout:QtWidgets.QGridLayout,T:Tasks):
    for i in T.fetchall():
        enterRow(tasklayout,i,True)

def isAllTasks(tasklayout:QtWidgets.QGridLayout, T:Tasks):
    IDs=[]
    for i in range(1,tasklayout.rowCount()):
        widget=tasklayout.itemAtPosition(i,0).widget()
        if widget is not None:
            print(type(tasklayout.itemAtPosition(i,0)), i)
            IDs.append(int(tasklayout.itemAtPosition(i,0).widget().text()))

    for i in T.fetchall():
        if i.ID not in IDs:
            return False
    else:
        return True





def genTabWidget(Layout_to_store_tabWidget:QtWidgets.QBoxLayout):
    tab_Widget=QtWidgets.QTabWidget()
    tab_Widget.tabBar().setFont(FONT)
    Layout_to_store_tabWidget.addWidget(tab_Widget)
    return tab_Widget


class guiFolders():
    def __init__(self,tabWidget:QtWidgets.QTabWidget,T:Tasks, conn:MySQLConnection):
        self.tabWidget=tabWidget
        self.T=T
        self.conn=conn
    
    def addTab(self, folder_name:str):
        tab=QtWidgets.QWidget()
        Lyt,S=genTasksLayout(tab)
        self.tabWidget.addTab(tab,folder_name)
        l=self.T.fetchall()
        for i in l:
            if i.folder==folder_name:
                enterRow(Lyt,i,True,self.T)

        with self.conn.cursor() as cur:
            cur.execute("SELECT Color FROM Folders WHERE Folder_name=%s",(folder_name,))
            c=cur.fetchone()[0]
            tab.setStyleSheet(f"background-color: {c};")








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