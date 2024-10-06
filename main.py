#from TRIALS.untitled import *
from Mainwindow import *
import sys
app = QtWidgets.QApplication(sys.argv)

 
class MyyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.index = 0

    def on_pushButton_5_pressed(self):
        print("ahhh")
        self.index = int(not bool(self.index))
        self.ui.stackedWidget.setCurrentIndex(self.index)

    def slot1(self,b):
        print("Yahallo",b)
MainWindow = MyyMainWindow()


MainWindow.show()
sys.exit(app.exec_())
