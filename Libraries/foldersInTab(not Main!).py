from PyQt5 import QtWidgets
import GUIFunc as G
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mainwindow")
        self.setGeometry(500, 100, 1000, 500)
        self.layout_to_store_tabWidget=QtWidgets.QGridLayout()

        self.TW=G.genTabWidget(self.layout_to_store_tabWidget)

        gf=G.guiFolders(self.TW)
        
        gf.addTab('Folder-1')
        gf.addTab('Folder-5')

        


        self.setLayout(self.layout_to_store_tabWidget)


    
app = QtWidgets.QApplication(sys.argv)

window = MyWindow()

window.show()

sys.exit(app.exec_())