import sys
from PyQt5 import QtWidgets
import GUIFunc as G
import mysql.connector as m
from Tasks import *

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mainwindow")
        self.setGeometry(800, 200, 300, 800)
        self.stacked_widget=QtWidgets.QStackedWidget(self)
        G.createlayout(self,self.stacked_widget)
        
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())