
from PyQt5 import QtWidgets,QtGui,QtCore

from Libraries.Tasks import *

FONT= QtGui.QFont()
FONT.setPointSize(10)

HEADINGFONT= QtGui.QFont()
HEADINGFONT.setPointSize(10)
HEADINGFONT.setBold(True)

def generateLighterColor(color):
    Qcolor = QtGui.QColor(color)
    return Qcolor.lighter(30).name()
 
def genCheckbox(task:taskobject,callback, delete_handler, modify_handler, layout:QtWidgets.QBoxLayout,
                row:int,column:int,color=None):
    checkbox=rightClickableBttn(task)
    if color:
        background = generateLighterColor(color)
        checkbox.setStyleSheet(f"background-color:{background};border:5px solid;border-radius:10px;border-color:{color};")
    checkbox.clicked.connect(callback)
    checkbox.setdelete_handler(delete_handler)
    checkbox.setmodify_handler(modify_handler)
    checkbox.setFont(FONT)

    layout.addWidget(checkbox,row,column)

def genLabel(data,layout:QtWidgets.QBoxLayout, row:int=None, column:int=None,color=None):
    Label=QtWidgets.QLabel(data)
    Label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)    
    if color:
        background = generateLighterColor(color)
        Label.setStyleSheet(f"background-color:{background};border:5px solid;border-radius:10px;border-color:{color};")
    if row is None: layout.addWidget(Label)
    else: layout.addWidget(Label,row,column,1,1)
    Label.setFont(FONT)
    return Label

def genLineEdit(layout:QtWidgets.QBoxLayout, row:int=None, column:int=None) ->QtWidgets.QLineEdit:
    """Genrates a LineEdit(Textbox)"""
    LineEdit=QtWidgets.QLineEdit()
    if (row,column)==(None,None): layout.addWidget(LineEdit)
    else: layout.addWidget(LineEdit,row,column)
    LineEdit.setFont(FONT)
    return LineEdit

def invisible(L:list):
    for widget in L:
        widget.hide()

def visible(L:list):
    for widget in L:
        widget.show()

def genRadioBttn(data,layout:QtWidgets.QBoxLayout,row:int=None,column:int=None, bttngrp:QtWidgets.QButtonGroup=None, id:int=None,
                 l:list=None) ->QtWidgets.QRadioButton:
    """Generates a RadioBttn"""
    Radiobttn=QtWidgets.QRadioButton(str(data))
    Radiobttn.setFont(FONT)
    if row is None: layout.addWidget(Radiobttn)
    else: layout.addWidget(Radiobttn,row,column)

    if not id: bttngrp.addButton(Radiobttn)
    if id: bttngrp.addButton(Radiobttn,id=id)
    if l: l.append(Radiobttn)
    return Radiobttn
def genComboBox(Items:list,layout:QtWidgets.QBoxLayout, row:int=None, column:int=None,
                l:list=None) ->QtWidgets.QComboBox:  
    """Generates a ComboBox(DropDown Box)""" 
    combo=QtWidgets.QComboBox()
    for i in Items:
        combo.addItem(str(i))

    if row!=None: layout.addWidget(combo,row,column)
    elif row==None: layout.addWidget(combo)
    combo.setFont(FONT)

    if l: l.append(combo)
    return combo

def genLine(layout:QtWidgets.QBoxLayout,row,column):
    v_line = QtWidgets.QFrame()
    v_line.setFrameShape(QtWidgets.QFrame.VLine)  # Vertical line
    v_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        # Add the lines to the layout
    layout.addWidget(v_line,row,column,1,1)
def genTasksLayout(tasksLayout,callback):
    HEADINGFONT= QtGui.QFont()
    HEADINGFONT.setPointSize(10)
    HEADINGFONT.setBold(True)
    for i in range(1,8,2):genLine(tasksLayout,row=0,column=i)
    
    bttn_group = QtWidgets.QButtonGroup()
    bttn_group.setExclusive(True)
    column_names = {'Slno':"Tasks.slno",'Task':"Tasks.msg",'Priority':"Tasks.priority",'Due Date':"Tasks.dt",
                    "Folder":"Tasks.folder"}
    def checkableBttn(text:str, column):
        bttn=QtWidgets.QRadioButton(text)
        bttn.setCheckable(True)
        #etFlat(True)
        bttn.setFont(HEADINGFONT)
        
        bttn_group.addButton(bttn)
        bttn.clicked.connect(lambda:callback(column_names[text]))
        tasksLayout.addWidget(bttn,0,column)

    for i,text in enumerate(column_names):
        checkableBttn(text,i*2)
    
    spacer=QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    tasksLayout.addItem(spacer,1,0)

def enterRow(layout:QtWidgets.QBoxLayout, task:taskobject,
             checkBoxCallback, delete_handler, modify_handler, color):
    
    if task==None:
        print("Task contains nothing! Try avoiding repeating tasks")
        return None
    if not isinstance(layout,QtWidgets.QGridLayout): 
        print("you can use this function only for GridLayout \
              Try again")
        return None
    slno=task.slno
    priority=task.priority
    DueDate=task.dueDate
    folder=task.folder

    
    lastrow = layout.rowCount()-1
    spacer = layout.itemAtPosition(lastrow,0)
    
    layout.removeItem(spacer)
    for i in range(1,8,2):
        genLine(layout,lastrow,i)
    genLabel(str(slno),layout,lastrow,0,color)
    genCheckbox(task.msg,checkBoxCallback,delete_handler, modify_handler,layout,lastrow,2,color)
    genLabel(str(priority),layout,lastrow,4,color)
    genLabel(str(DueDate),layout,lastrow,6,color)
    genLabel(folder,layout,lastrow,8,color)
    spacer=QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    layout.addItem(spacer,lastrow+1,0)

def deleteRow(layout:QtWidgets.QGridLayout,row):
    for i in range(layout.columnCount()):
        item = layout.itemAtPosition(row,i)
        if item is not None:
            layout.removeItem(item)
            if item.spacerItem():
                del item
            else:
                widget = item.widget()
                widget.deleteLater()


class Folder(QtWidgets.QWidget):
    def __init__(self,text,color,editCallback,selectCallback,deleteCallback,buttonGroup):
        super().__init__()
        self.color = color
        self.text = text
        self.editCallback = editCallback
        layout = QtWidgets.QHBoxLayout(self)
        layout.setSpacing(0)
        circle = editableButton()
        circle.setFixedSize(20,20)
        circle.doubleClicked.connect(self.circleEdit)
        circle.setStyleSheet(f"background-color:{color};border-radius:10px;")
        layout.addWidget(circle)

        text = editableButton(text)
        text.setCheckable(True)
        buttonGroup.addButton(text)
        text.clicked.connect(selectCallback)
        text.doubleClicked.connect(self.textEdit)
        text.setDeleteCallback(deleteCallback)
        ##buttonGroup.addButton(text)
        layout.addWidget(text)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
    def circleEdit(self):
        new_color = QtWidgets.QColorDialog().getColor(QtGui.QColor(self.color))
        self.editCallback(self.text,new_color.name())

    def textEdit(self):
        text,ok = QtWidgets.QInputDialog.getText(self,"Text Input","Rename Folder")
        if text and ok:
            self.editCallback(text,self.color)

class editableButton(QtWidgets.QPushButton):
    doubleClicked = QtCore.pyqtSignal()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.deleteCallback = 0
    def setDeleteCallback(self,func):
        self.deleteCallback = func
    def mouseDoubleClickEvent(self,event):
        self.doubleClicked.emit()
        super().mouseDoubleClickEvent(event)
    def contextMenuEvent(self, event):
        if self.deleteCallback:
            context_menu = QtWidgets.QMenu(self)

            info_action = QtWidgets.QAction("delete", self)
            info_action.triggered.connect(self.deleteCallback)

            context_menu.addAction(info_action)
            context_menu.exec_(event.globalPos())
        else:
            super().contextMenuEvent(event)
    
class rightClickableBttn(QtWidgets.QCheckBox):
    rightClicked = QtCore.pyqtSignal()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.delete_handler=None
        self.modify_handler=None
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.rightClicked.emit()
            event.accept()  # Stop event propagation
        else:
            super().mousePressEvent(event)
    def setdelete_handler(self,func):
        self.delete_handler=func
    def setmodify_handler(self,func):
        self.modify_handler=func
    def contextMenuEvent(self, event):
        context_menu = QtWidgets.QMenu(self)
        delete = context_menu.addAction("Delete Task")
        modify = context_menu.addAction("Modify Task")

        # Connect the actions to handlers only if they are set
        if self.delete_handler:
            delete.triggered.connect(self.delete_handler)
        else:
            delete.triggered.connect(lambda: print("Delete handler not set"))

        if self.modify_handler:
            modify.triggered.connect(self.modify_handler)
        else:
            modify.triggered.connect(lambda: print("Modify handler not set"))

        context_menu.exec_(event.globalPos())  # Show the context menu