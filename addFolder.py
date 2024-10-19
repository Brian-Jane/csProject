import sys
from PyQt5 import QtWidgets,QtGui
from Libraries.Tasks import Tasks,taskobject
import time
import Libraries.Gui as G
import mysql.connector as m
import datetime
import pprint
import json


class addFolderWindow(QtWidgets.QDialog):
    def __init__(self,folderList):
        super().__init__()
        self.folderList = folderList
        self.setWindowTitle("Add Folder")
        self.setGeometry(500, 100, 500,500)
        self.mainLayout=QtWidgets.QGridLayout()
        G.genLabel("Add folder name: ",self.mainLayout,0,0)
        self.folder=G.genLineEdit(self.mainLayout,0,1)
        G.genLabel("Add Colour",self.mainLayout,1,0)
        
        self.color_button = QtWidgets.QPushButton()
        self.color_button.setFixedSize(50,50)
        self.color= '#87CEEB'
        self.color_button.setStyleSheet(f'background-color: {self.color} ; border: none; border-radius: 25px;')
        self.mainLayout.addWidget(self.color_button,1,1) 
        self.color_button.clicked.connect(self.colour_button_clicked)

        self.submitbttn=QtWidgets.QPushButton('Submit')
        self.submitbttn.setFont(G.FONT)
        self.submitbttn.clicked.connect(self.submitbttn_clicked)

        self.mainLayout.addWidget(self.submitbttn)

        self.setLayout(self.mainLayout)

    def colour_button_clicked(self):
        color_dialog=QtWidgets.QColorDialog()
        color_dialog.setStyleSheet('background-color: white;')
        color = color_dialog.getColor()
        self.color = color.name()
        self.color_button.setStyleSheet(f'background-color: {self.color};  border: none; border-radius: 25px;')

    def submitbttn_clicked(self):
        if self.folder.text() in self.folderList:
            QtWidgets.QMessageBox.warning(self,"Warning","Folder already exists")
        else:
            self.newFolder = (self.folder.text(),self.color)
            self.accept()
     