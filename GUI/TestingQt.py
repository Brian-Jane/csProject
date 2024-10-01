import sys
from PyQt5 import QtWidgets
import GUIFunc as G

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mainwindow")
        self.setGeometry(500, 100, 908, 753)
                
                
app = QtWidgets.QApplication(sys.argv)

window = MyWindow()

window.show()
Layout=QtWidgets.QGridLayout()
window.setLayout(Layout)
G.enterRow(Layout,'Task-1',6,folder="Folder-1")
G.enterRow(Layout,'Task-2',9,folder="Folder-2")
sys.exit(app.exec_())