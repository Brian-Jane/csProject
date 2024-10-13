
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as connector

from Libraries import GUIFunc as G
from Libraries.Tasks import *
import WindowForTasks 
import sys
import json


class MyyMainWindow(QtWidgets.QWidget):
    def __init__(self, T:Tasks, conn:MySQLConnection):
        super().__init__()
        self.T=T
        self.conn=conn
        self.setWindowTitle("mainwindow")
        self.setGeometry(500, 100, 1000,900)
        self.Vlayout=QtWidgets.QVBoxLayout()
        
        self.mainLayout=QtWidgets.QGridLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)


        spacer1=QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Vlayout.addItem(spacer1)

        self.tasks=QtWidgets.QPushButton('Tasks')
        self.tasks.setFont(G.FONT)
        self.tasks.clicked.connect(self.tasks_clicked)
        self.Vlayout.addWidget(self.tasks)


        self.folders=QtWidgets.QPushButton('Folders')
        self.folders.setFont(G.FONT)
        self.folders.clicked.connect(self.folders_clicked)
        self.Vlayout.addWidget(self.folders)

        spacer2=QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Vlayout.addItem(spacer2)

        self.mainLayout.addLayout(self.Vlayout,0,0,3,1)

    

        vertical_line = QtWidgets.QFrame()
        vertical_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.mainLayout.addWidget(vertical_line, 0,1,2,1 )

        self.stackedWidget=QtWidgets.QStackedWidget()

        #Page-1
        self.page_1 = self.create_page(self.stackedWidget)      #Index 0
        outer_layout= QtWidgets.QGridLayout()
        self.LE=G.genLineEdit(outer_layout,0,0)
        self.LE.setPlaceholderText('Search')
        srchbttn=QtWidgets.QPushButton('🔍')
        outer_layout.addWidget(srchbttn,0,1)

        G.genSpacer(outer_layout,0,2,'h')

        addTaskBttn=QtWidgets.QPushButton("+ Add Task")
        addTaskBttn.clicked.connect(self.addTasksBttn_clicked)
        
        outer_layout.addWidget(addTaskBttn,0,3)

        W_toStoretl=QtWidgets.QWidget()
        tl1=G.genTasksLayout(W_toStoretl)[0]
        for i in self.T.fetchall():
            G.enterRow(tl1,i,True,self.T)
        
        outer_layout.addWidget(W_toStoretl,3,0, 1,3)
        self.page_1.setLayout(outer_layout)
        print("bttn Parent:", srchbttn.parent())



        #Page-2
        self.page_2 = self.create_page(self.stackedWidget)      #Index 1
        self.layout_to_store_tabWidget=QtWidgets.QGridLayout()

        self.TW=G.genTabWidget(self.layout_to_store_tabWidget)

        gf=G.guiFolders(self.TW,self.T,self.conn)
        for (i,colour) in self.T.fetchFolders():
            gf.addTab(i)



        self.page_2.setLayout(self.layout_to_store_tabWidget)
        




        self.mainLayout.addWidget(self.stackedWidget,1,2)
        self.setLayout(self.mainLayout)

    def create_page(self, stackedWidget:QtWidgets.QStackedWidget):
        page=QtWidgets.QWidget()
        stackedWidget.addWidget(page)
        return page


    def tasks_clicked(self):
        """Switch to Page-1 (index 0)."""
        self.stackedWidget.setCurrentIndex(0)

    def folders_clicked(self):
        """Switch to Page-2 (index 1)."""
        self.stackedWidget.setCurrentIndex(1)

    def addTasksBttn_clicked(self):
        self.taskWindow=WindowForTasks.TasksWindow(self.T)        #I am Initialising the TasksWindow as a part of self (To avoid garbage collection)
        G.newWindow(self.taskWindow)

    '''def srchBttn_clicked(self,task:str, tasklayout:QtWidgets.QGridLayout):
        if task=='':
            if G.isAllTasks(tasklayout):
               pass
            else:
                G.deleteRow(tasklayout,row=1)
                G.enterAllTasks(tasklayout) 
            
        else:   
            if self.T.searchTask(task):     
                row=self.T.searchTask(task)[0].ID
                for i in range(tasklayout.rowCount()):
                    if i!=row:
                        G.deleteRow(tasklayout,i)   
                G.genSpacer(tasklayout,2,0,'v')
            else:
                G.produceError("Task Not found")'''





with open('config.json','r') as file:
    config = json.loads(file.read())
print(config)

mycon = connector.connect(user='root',host='localhost',
                          password=config['password'],
                          database=config['database'])
T=Tasks(mycon)


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MyyMainWindow(T,mycon)


    window.show()

    sys.exit(app.exec_())

    

    
