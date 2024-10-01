import sys
from PyQt5 import QtWidgets
import GUIFunc as G

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mainwindow")
        self.setGeometry(500, 100, 908, 753)
        """checkboxes=self.findChildren(QtWidgets.QCheckBox)
        D={}
        #{task:Checkbox}    Automatically the name of the checkbox is the text it stores
        for i in checkboxes:
            D[i.text()]=i
        v_layout=QtWidgets.QVBoxLayout()
        G.genCheckbox(task="hi", layout=v_layout, Window=self,Dcheck=D)     
        G.genCheckbox(task="hello",layout=v_layout, Window=self,Dcheck=D)  
        self.setLayout(v_layout)
        for key, checkbox in D.items():
            print(f"Checkbox name: {key} - Text: {checkbox.text()}")"""
        Layout=QtWidgets.QGridLayout()
        self.setLayout(Layout)
        G.enterRow(Layout,'Task-1',6,folder="Folder-1")
        G.enterRow(Layout,'Task-2',9,folder="Folder-2")
        
app = QtWidgets.QApplication(sys.argv)

window = MyWindow()

window.show()

sys.exit(app.exec_())