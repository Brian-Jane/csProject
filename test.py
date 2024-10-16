#from TRIALS.untitled import *
import GUI.Mainwindow as mw

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette,QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyleFactory
import mysql.connector as connector
from datetime import datetime,timedelta

from Libraries import Tasks
from Libraries import Gui

from WindowForTasks import TasksWindow

import sys
import json


class TestApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)
        checkbox = Gui.right_ClickTask("Right Click Me")
        layout.addWidget(checkbox)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TestApp()
    window.show()
    sys.exit(app.exec_())