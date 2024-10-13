import sys
from PyQt5 import QtWidgets,QtGui
from Libraries.Tasks import Tasks,taskobject
import time
import Libraries.GUIFunc as G
import mysql.connector as m
import datetime
import pprint
import json


'''class ColorDotButton(QtWidgets.QPushButton):
    def __init__(self, initial_color="#FF0000", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = initial_color
        self.setFixedSize(50, 50)  # Set a fixed size for the button
        self.update_style()

        # Connect the button click event to the color selection method
        self.clicked.connect(self.open_color_dialog)

    def update_style(self):
        # Set the background color of the button using the hex code and make it circular
        self.setStyleSheet(f"""
            background-color: {self.color};  /* Use hex code for color */
            border: none;
            border-radius: 25px;  /* Half of the width/height to make it circular */
        """)

    def open_color_dialog(self):
        global COLOUR
        # Open the color dialog and get the selected color
        color_dialog = QtWidgets.QColorDialog()
        color_dialog.setStyleSheet('background-color: white;')
        color_dialog.setFont(G.FONT)
        color = color_dialog.getColor()
        COLOUR=color

        # If a color was selected, update the button color
        if color.isValid():
            self.color = color.name()  # Get the hex color code
            self.update_style()
            COLOUR=self.color'''


class addFolderWindow(QtWidgets.QWidget):
    def __init__(self,T:Tasks):
        super().__init__()
        self.T=T
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
        print(self.folder.text(),self.color)
        if not self.T.addFolder(self.folder.text(),self.color):
            G.produceError("Folder already there")


    

with open('config.json','r') as file:
    config = json.loads(file.read())
print(config)
mycon = m.connect(user='root',host='localhost',
                          password=config['password'],
                          database=config['database'])
t=Tasks(mycon)
app = QtWidgets.QApplication(sys.argv)

window = addFolderWindow(t)

window.show()

sys.exit(app.exec_())

