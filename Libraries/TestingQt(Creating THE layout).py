from PyQt5 import QtWidgets
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Group Box Example')

        # Create a group box
        self.groupBox = QtWidgets.QGroupBox("Personal Information")

        # Create widgets to go inside the group box
        self.nameLabel = QtWidgets.QLabel("Name:")
        self.nameInput = QtWidgets.QLineEdit()
        self.ageLabel = QtWidgets.QLabel("Age:")
        self.ageInput = QtWidgets.QSpinBox()

        # Create a layout for the group box
        self.layout = QtWidgets.QFormLayout()
        self.layout.addRow(self.nameLabel, self.nameInput)
        self.layout.addRow(self.ageLabel, self.ageInput)

        # Set layout to the group box
        self.groupBox.setLayout(self.layout)

        # Create a main layout and add the group box
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.addWidget(self.groupBox)

        # Set the main layout to the window
        self.setLayout(self.mainLayout)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())