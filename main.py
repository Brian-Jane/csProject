#from TRIALS.untitled import *
from TRIALS.TRial import *
import sys
app = QtWidgets.QApplication(sys.argv)

 
class MyyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
    def slot1(self,b):
        print("Yahallo",b)
MainWindow = MyyMainWindow()
ui = Ui_MainWindow()

ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
