from PyQt5 import QtWidgets
import Libraries.GUIFunc as G
from Libraries.Tasks import Tasks
import sys
import mysql.connector as m
import json

with open('config.json','r') as file:
    config = json.loads(file.read())
print(config)
conn = m.connect(user='root',host='localhost',
                          password=config['password'],
                          database=config['database'])
T=Tasks(conn)



class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folder Window")
        self.setGeometry(500, 100, 1000, 500)
        self.layout_to_store_tabWidget=QtWidgets.QGridLayout()

        self.TW=G.genTabWidget(self.layout_to_store_tabWidget)

        gf=G.guiFolders(self.TW,T,conn=conn)
        
        gf.addTab('Folder-1')
        gf.addTab('Folder-2')
        


        self.setLayout(self.layout_to_store_tabWidget)


    
app = QtWidgets.QApplication(sys.argv)

window = MyWindow()

window.show()

sys.exit(app.exec_())