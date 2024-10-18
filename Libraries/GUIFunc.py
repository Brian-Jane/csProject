from PyQt5 import QtWidgets,QtGui,QtCore
import mysql.connector as m
from typing import Union

from Libraries.Tasks import *

FONT= QtGui.QFont()
FONT.setPointSize(10)

HEADINGFONT= QtGui.QFont()
HEADINGFONT.setPointSize(10)
HEADINGFONT.setBold(True)

def genLabel(data,layout:QtWidgets.QBoxLayout, row:int=None, column:int=None,
             l:list=None) ->QtWidgets.QLabel:
    """Generates a Label"""
    Label=QtWidgets.QLabel(data)
    if row is None: layout.addWidget(Label)
    else: layout.addWidget(Label,row,column)
    Label.setFont(FONT)
    if l: l.append(Label)
    return Label

def genLineEdit(layout:QtWidgets.QBoxLayout, row:int=None, column:int=None) ->QtWidgets.QLineEdit:
    """Genrates a LineEdit(Textbox)"""
    LineEdit=QtWidgets.QLineEdit()
    if (row,column)==(None,None): layout.addWidget(LineEdit)
    else: layout.addWidget(LineEdit,row,column)
    LineEdit.setFont(FONT)
    return LineEdit

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

def invisible(L:list):
    for widget in L:
        widget.hide()

def visible(L:list):
    for widget in L:
        widget.show()


