import sys
from PyQt5 import QtWidgets,QtGui
from Tasks import Tasks,taskobject
import time
import GUIFunc as G
import mysql.connector as m
import datetime
import pprint
conn=m.connect(user='root',host='LocalHost',database='csp',password='0000')



class TasksWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mainwindow")
        self.setGeometry(500, 100, 1000,900)
        self.mainLayout=QtWidgets.QGridLayout()

        #Row-0
        W1=G.genLabel("Enter Task",self.mainLayout,0,0)
        W1.setFont(G.HEADINGFONT)
        self.task=G.genLineEdit(self.mainLayout,0,1)
        self.task.setPlaceholderText('Enter Task')

        #Row-1
        vertical_spacer_1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(vertical_spacer_1, 1, 0)


        #Row-2
        W2=G.genLabel("Folder",self.mainLayout,2,0)
        W2.setFont(G.HEADINGFONT)

        T=Tasks(conn)
        folders=[None]
        for i in T.fetchFolders():
            folders.append(i[0])

        self.folder=G.genComboBox(folders,self.mainLayout,2,1)


        #Row-3
        vertical_spacer_2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(vertical_spacer_1, 3, 0)


        #Row-4
        W3=QtWidgets.QPushButton("DueDate")
        W3.setFlat(True)
        W3.setCheckable(True)
        W3.setFont(G.HEADINGFONT)


        #Row-5
        self.layout1=QtWidgets.QGridLayout()   
        current_year=datetime.datetime.now().year

        G.genLabel("Year", self.layout1,0,0)    
        G.genLabel("Month",self.layout1,0,1)
        G.genLabel("Day",self.layout1,0,2)
        G.genLabel("Time    (hrs:min)",self.layout1,0,3)
        #year
        self.year=G.genComboBox(list(range(current_year,current_year+10)),self.layout1,1,0)
        #Month
        self.month=G.genComboBox(['','January','February','March','April','May','June','July','August','September','October','November','December'],
                      self.layout1, 1,1)
        #Day
        self.day=G.genComboBox(['']+list(range(1,32)),self.layout1, 1,2)
        #Time
        self.timeEdit=QtWidgets.QTimeEdit()
        self.timeEdit.setFont(G.FONT)
        self.layout1.addWidget(self.timeEdit,1,3)

        self.mainLayout.addLayout(self.layout1,5,0,1,2)


        #Row-6
        vertical_spacer_2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(vertical_spacer_2, 6, 0)

        #Row-7
        W4=G.genLabel("Priority",self.mainLayout,7,0)
        W4.setFont(G.HEADINGFONT)

        #Row-8
        self.layout2=QtWidgets.QHBoxLayout()
        for i in range(1,11):
            G.genRadioBttn(i,self.layout2)

        self.mainLayout.addItem(self.layout2,8,0,1,2)
        
        #Row-9
        vertical_spacer_3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(vertical_spacer_3, 9, 0)


        #Row-10
        self.submitBttn=QtWidgets.QPushButton('Submit')
        self.submitBttn.setFont(G.FONT)
        self.mainLayout.addWidget(self.submitBttn,10,0)
        
        self.submitBttn.clicked.connect(self.Submit_clicked)


        ##
        self.setLayout(self.mainLayout)


    def Submit_clicked(self):
        month_map = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}
        
        year=int(self.year.currentText())
        month=self.month.currentText().lower()
        day=self.day.currentText().lower()      #If Day or month is not provided, day=month=''

        hr=self.timeEdit.time().hour()
        min=self.timeEdit.time().minute()
        sec=self.timeEdit.time().second()

        #What_is_clicked tells us which radiobutton is clicked

        try:
            priority=G.What_is_clicked.text()
        except AttributeError:
            priority=5


        c=1
        if not self.task.text():
            G.produceError("Please enter the task")
            c=0
        else:
            if self.is_valid_date(day,month):
                c=1
            else:
                G.produceError("Invalid Date")
                c=0

        if day=='' and month=='':
            date=None
        else:
            day=int(self.day.currentText().lower())
            month=month_map[self.month.currentText().lower()]
            date=datetime.datetime(year,month,day,hr,min,sec)
        

        if c==1:
            d={
                'task': self.task.text(), 
                 'priority': int(priority), 
                 'date' : date,
                 'folder':self.folder.currentText()
                    }
        
            pprint.pprint(d)

            self.close()
            T=Tasks(conn)

            T.addTask(d['task'], d['priority'], date, d['folder'], Revivaldt=None)
                  


    def is_valid_date(self, day: int, month: str):
        run = True

        # Check if the month is empty or None
        if not month:
            if day:
                run = False
            return run

        # If the month is provided but day is not, it's invalid
        if month and not day:
            return False

        # Dictionary with the maximum number of days in each month
        month_days = {
            "january": 31,
            "february": 29,  # Considering leap years
            "march": 31,
            "april": 30,
            "may": 31,
            "june": 30,
            "july": 31,
            "august": 31,
            "september": 30,
            "october": 31,
            "november": 30,
            "december": 31
        }

        day=int(day)
        # Normalize month input to lowercase
        month = month.lower()

        # Validate month existence in the dictionary
        if month not in month_days:
            return False

        # Check if the provided day exceeds the maximum number of days in the month
        if day > month_days[month]:
            run = False

        # Get the current year
        current_date = datetime.datetime.now()
        year = current_date.year

        # Handle February and leap years
        if month == 'february' and day == 29:
            # Check if it's a leap year
            if year % 4 == 0:
                if year % 100 == 0 and year % 400 != 0:
                    run = False  # Not a leap year if divisible by 100 but not 400
            else:
                run = False  # Not a leap year if not divisible by 4

        return run
        

app = QtWidgets.QApplication(sys.argv)

window = TasksWindow()

window.show()

sys.exit(app.exec_())

