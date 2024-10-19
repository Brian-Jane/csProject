from PyQt5 import QtWidgets
from Libraries.Tasks import Filter
import datetime

class addFilter(QtWidgets.QDialog):
    def __init__(self,filter:Filter=None):
        self.filter = filter
        super().__init__()
        self.setGeometry(50,50,500,500)
        layout = QtWidgets.QVBoxLayout(self)

        p1 = Priority(1,self.filter)
        p2 = Priority(0,self.filter)

        duedate = dueDate(self.filter)

        submit_bttn = QtWidgets.QPushButton("Submit")
        submit_bttn.clicked.connect(self.submit)
        layout.addLayout(p1)
        layout.addLayout(p2)
        layout.addLayout(duedate)
        layout.addWidget(submit_bttn)

        self.setLayout(layout)
    def submit(self):
        self.accept()

class Priority(QtWidgets.QVBoxLayout):
    def __init__(self,b,filter:Filter):
        super().__init__()
        if b:
            button = QtWidgets.QPushButton("Priority Higher than")
        else:
            button = QtWidgets.QPushButton("Priority Lower than")
        self.addWidget(button)
        Hbox = QtWidgets.QHBoxLayout()
        self.bttngrp = QtWidgets.QButtonGroup()
        for i in range(1,11):
            self.bu = QtWidgets.QRadioButton(str(i),None)
            self.bttngrp.addButton(self.bu)
            Hbox.addWidget(self.bu)
        def setpriority(bttn:QtWidgets.QRadioButton):
            if b:
                filter.priorityHigherThan(int(bttn.text()))
            else:filter.priorityLowerThan(int(bttn.text()))
        self.bttngrp.buttonClicked.connect(setpriority)
        self.addLayout(Hbox)

class dueDate(QtWidgets.QHBoxLayout):
    def __init__(self,filter):
        super().__init__()
        self.filter = filter
        self.button = QtWidgets.QPushButton("Due Date Before:")
        self.button.setCheckable(True)
        self.button.toggled.connect(self.toggled)
        self.addWidget(self.button)

    def toggled(self,checked):
        if checked:
            dueDateBefore = QtWidgets.QDateTimeEdit(datetime.datetime.now())
            def setdt(dt):
                self.filter.dateBefore(dt.toPyDateTime())
            dueDateBefore.dateTimeChanged.connect(setdt)
            self.addWidget(dueDateBefore)
        else:
            try:self.filter.undo(self.filter.dateBefore)
            except:pass
            item = self.takeAt(1)
            item.widget().deleteLater()