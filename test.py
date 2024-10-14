from WindowForTasks import TasksWindow
import mysql.connector as m
from Libraries.Tasks import *
from PyQt5 import QtWidgets
import sys
conn=m.connect(user="root",host="LocalHost",database="csp",password="0000")
a=Tasks(conn)



app = QtWidgets.QApplication(sys.argv)

window = TasksWindow(a)

window.show()

sys.exit(app.exec_())