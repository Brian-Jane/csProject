# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI\Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(1200, 900)
        font = QtGui.QFont()
        font.setPointSize(4)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 100, 1000, 800))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.MainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setObjectName("MainLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.line_14 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout.addWidget(self.line_14)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(72, 237, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.MainLayout.addLayout(self.verticalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.page)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 661, 511))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gridLayoutWidget_4.setFont(font)
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.Taskslayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.Taskslayout_3.setContentsMargins(0, 0, 0, 0)
        self.Taskslayout_3.setObjectName("Taskslayout_3")
        self.line_13 = QtWidgets.QFrame(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_13.setFont(font)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.Taskslayout_3.addWidget(self.line_13, 0, 3, 3, 1)
        self.line_15 = QtWidgets.QFrame(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_15.setFont(font)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.Taskslayout_3.addWidget(self.line_15, 0, 1, 3, 1)
        self.DueDate_2 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DueDate_2.setFont(font)
        self.DueDate_2.setStyleSheet("")
        self.DueDate_2.setCheckable(True)
        self.DueDate_2.setChecked(False)
        self.DueDate_2.setFlat(True)
        self.DueDate_2.setObjectName("DueDate_2")
        self.Taskslayout_3.addWidget(self.DueDate_2, 0, 6, 1, 1)
        self.line_16 = QtWidgets.QFrame(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_16.setFont(font)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.Taskslayout_3.addWidget(self.line_16, 0, 5, 3, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.checkBox_4.setObjectName("checkBox_4")
        self.Taskslayout_3.addWidget(self.checkBox_4, 1, 2, 1, 1)
        self.msg_4 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.msg_4.setFont(font)
        self.msg_4.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_4.setObjectName("msg_4")
        self.Taskslayout_3.addWidget(self.msg_4, 0, 2, 1, 1)
        self.Folder_2 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Folder_2.setFont(font)
        self.Folder_2.setStyleSheet("")
        self.Folder_2.setCheckable(True)
        self.Folder_2.setChecked(False)
        self.Folder_2.setFlat(True)
        self.Folder_2.setObjectName("Folder_2")
        self.Taskslayout_3.addWidget(self.Folder_2, 0, 8, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.Taskslayout_3.addWidget(self.label_5, 1, 8, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.Taskslayout_3.addWidget(self.label_14, 1, 0, 1, 1)
        self.line_17 = QtWidgets.QFrame(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_17.setFont(font)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.Taskslayout_3.addWidget(self.line_17, 0, 7, 3, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.Taskslayout_3.addWidget(self.label_15, 1, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(78, 308, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Taskslayout_3.addItem(spacerItem3, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.Taskslayout_3.addWidget(self.label_16, 1, 4, 1, 1)
        self.Slno_2 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Slno_2.setFont(font)
        self.Slno_2.setCheckable(False)
        self.Slno_2.setChecked(False)
        self.Slno_2.setFlat(True)
        self.Slno_2.setObjectName("Slno_2")
        self.Taskslayout_3.addWidget(self.Slno_2, 0, 0, 1, 1)
        self.Priority_4 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Priority_4.setFont(font)
        self.Priority_4.setCheckable(True)
        self.Priority_4.setFlat(True)
        self.Priority_4.setObjectName("Priority_4")
        self.Taskslayout_3.addWidget(self.Priority_4, 0, 4, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.TasksPage = QtWidgets.QWidget()
        self.TasksPage.setObjectName("TasksPage")
        self.gridLayoutWidget = QtWidgets.QWidget(self.TasksPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 39, 631, 471))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.Taskslayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.Taskslayout.setContentsMargins(0, 0, 0, 0)
        self.Taskslayout.setObjectName("Taskslayout")
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Taskslayout.addWidget(self.line_2, 0, 3, 3, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Taskslayout.addWidget(self.line, 0, 1, 3, 1)
        self.DueDate = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DueDate.setFont(font)
        self.DueDate.setStyleSheet("")
        self.DueDate.setCheckable(True)
        self.DueDate.setChecked(False)
        self.DueDate.setFlat(True)
        self.DueDate.setObjectName("DueDate")
        self.Taskslayout.addWidget(self.DueDate, 0, 6, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Taskslayout.addWidget(self.line_3, 0, 5, 3, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.Taskslayout.addWidget(self.checkBox, 1, 2, 1, 1)
        self.msg = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.msg.setFont(font)
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.Taskslayout.addWidget(self.msg, 0, 2, 1, 1)
        self.Folder = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Folder.setFont(font)
        self.Folder.setStyleSheet("")
        self.Folder.setCheckable(True)
        self.Folder.setChecked(False)
        self.Folder.setFlat(True)
        self.Folder.setObjectName("Folder")
        self.Taskslayout.addWidget(self.Folder, 0, 8, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.Taskslayout.addWidget(self.label_3, 1, 8, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.Taskslayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_4.setFont(font)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.Taskslayout.addWidget(self.line_4, 0, 7, 3, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.Taskslayout.addWidget(self.label_2, 1, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(78, 308, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Taskslayout.addItem(spacerItem4, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Taskslayout.addWidget(self.label, 1, 4, 1, 1)
        self.Slno = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Slno.setFont(font)
        self.Slno.setCheckable(False)
        self.Slno.setChecked(False)
        self.Slno.setFlat(True)
        self.Slno.setObjectName("Slno")
        self.Taskslayout.addWidget(self.Slno, 0, 0, 1, 1)
        self.Priority = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Priority.setFont(font)
        self.Priority.setCheckable(True)
        self.Priority.setFlat(True)
        self.Priority.setObjectName("Priority")
        self.Taskslayout.addWidget(self.Priority, 0, 4, 1, 1)
        self.SearchBar = QtWidgets.QLineEdit(self.TasksPage)
        self.SearchBar.setGeometry(QtCore.QRect(150, 10, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SearchBar.setFont(font)
        self.SearchBar.setObjectName("SearchBar")
        self.addTasbkttn = QtWidgets.QPushButton(self.TasksPage)
        self.addTasbkttn.setGeometry(QtCore.QRect(50, 520, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addTasbkttn.setFont(font)
        self.addTasbkttn.setObjectName("addTasbkttn")
        self.searchBttn = QtWidgets.QPushButton(self.TasksPage)
        self.searchBttn.setGeometry(QtCore.QRect(280, 10, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchBttn.setFont(font)
        self.searchBttn.setStyleSheet("")
        self.searchBttn.setCheckable(True)
        self.searchBttn.setChecked(False)
        self.searchBttn.setObjectName("searchBttn")
        self.stackedWidget.addWidget(self.TasksPage)
        self.FoldersPage = QtWidgets.QWidget()
        self.FoldersPage.setObjectName("FoldersPage")
        self.tabWidget = QtWidgets.QTabWidget(self.FoldersPage)
        self.tabWidget.setGeometry(QtCore.QRect(40, 20, 591, 481))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.Folder1 = QtWidgets.QWidget()
        self.Folder1.setStyleSheet("QTabBar::tab {\n"
"    background-color: #0000FF  /* Background color of the tab */\n"
"}\n"
"")
        self.Folder1.setObjectName("Folder1")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.Folder1)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 551, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gridLayoutWidget_2.setFont(font)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.Taskslayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.Taskslayout_2.setContentsMargins(0, 0, 0, 0)
        self.Taskslayout_2.setObjectName("Taskslayout_2")
        self.line_6 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_6.setFont(font)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.Taskslayout_2.addWidget(self.line_6, 0, 3, 3, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("")
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setChecked(False)
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.Taskslayout_2.addWidget(self.pushButton_10, 0, 8, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.Taskslayout_2.addWidget(self.label_6, 1, 4, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.Taskslayout_2.addWidget(self.checkBox_2, 1, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setChecked(False)
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.Taskslayout_2.addWidget(self.pushButton_9, 0, 6, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.Taskslayout_2.addWidget(self.label_8, 1, 8, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_5.setFont(font)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.Taskslayout_2.addWidget(self.line_5, 0, 7, 3, 1)
        self.Priority_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Priority_2.setFont(font)
        self.Priority_2.setCheckable(True)
        self.Priority_2.setFlat(True)
        self.Priority_2.setObjectName("Priority_2")
        self.Taskslayout_2.addWidget(self.Priority_2, 0, 4, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCheckable(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.Taskslayout_2.addWidget(self.pushButton_11, 0, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_8.setFont(font)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.Taskslayout_2.addWidget(self.line_8, 0, 1, 3, 1)
        self.msg_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.msg_2.setFont(font)
        self.msg_2.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_2.setObjectName("msg_2")
        self.Taskslayout_2.addWidget(self.msg_2, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.Taskslayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.Taskslayout_2.addWidget(self.label_7, 1, 6, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(78, 308, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Taskslayout_2.addItem(spacerItem5, 2, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_7.setFont(font)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.Taskslayout_2.addWidget(self.line_7, 0, 5, 3, 1)
        self.tabWidget.addTab(self.Folder1, "")
        self.Folder11 = QtWidgets.QWidget()
        self.Folder11.setObjectName("Folder11")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.Folder11)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(15, 20, 561, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gridLayoutWidget_3.setFont(font)
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line_9 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_9.setFont(font)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_3.addWidget(self.line_9, 0, 3, 3, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setChecked(False)
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_3.addWidget(self.pushButton_12, 0, 8, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 4, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 1, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("")
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setChecked(False)
        self.pushButton_13.setFlat(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_3.addWidget(self.pushButton_13, 0, 6, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 8, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_10.setFont(font)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_3.addWidget(self.line_10, 0, 7, 3, 1)
        self.Priority_3 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Priority_3.setFont(font)
        self.Priority_3.setCheckable(True)
        self.Priority_3.setFlat(True)
        self.Priority_3.setObjectName("Priority_3")
        self.gridLayout_3.addWidget(self.Priority_3, 0, 4, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCheckable(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_14.setFlat(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_3.addWidget(self.pushButton_14, 0, 0, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_11.setFont(font)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_3.addWidget(self.line_11, 0, 1, 3, 1)
        self.msg_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.msg_3.setFont(font)
        self.msg_3.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_3.setObjectName("msg_3")
        self.gridLayout_3.addWidget(self.msg_3, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 6, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(78, 308, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 2, 0, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_12.setFont(font)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout_3.addWidget(self.line_12, 0, 5, 3, 1)
        self.tabWidget.addTab(self.Folder11, "")
        self.addFolderbttn = QtWidgets.QPushButton(self.FoldersPage)
        self.addFolderbttn.setGeometry(QtCore.QRect(40, 520, 101, 23))
        self.addFolderbttn.setObjectName("addFolderbttn")
        self.stackedWidget.addWidget(self.FoldersPage)
        self.MainLayout.addWidget(self.stackedWidget)
        self.SSRVMlogo = QtWidgets.QLabel(self.centralwidget)
        self.SSRVMlogo.setGeometry(QtCore.QRect(820, 10, 71, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SSRVMlogo.setFont(font)
        self.SSRVMlogo.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.SSRVMlogo.setText("")
        self.SSRVMlogo.setPixmap(QtGui.QPixmap("GUI\\../../../../Desktop/ssrvm_logo_9de844bc87.jpg"))
        self.SSRVMlogo.setScaledContents(True)
        self.SSRVMlogo.setObjectName("SSRVMlogo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Filter"))
        self.pushButton_4.setText(_translate("MainWindow", "☀ Today"))
        self.pushButton_2.setText(_translate("MainWindow", "All Tasks"))
        self.pushButton_3.setText(_translate("MainWindow", "Folders"))
        self.DueDate_2.setText(_translate("MainWindow", "DueDate"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.msg_4.setText(_translate("MainWindow", "Task"))
        self.Folder_2.setText(_translate("MainWindow", "Folder"))
        self.label_5.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Label"))
        self.label_14.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "1."))
        self.label_15.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "Label"))
        self.label_16.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "5"))
        self.Slno_2.setText(_translate("MainWindow", "Slno"))
        self.Priority_4.setText(_translate("MainWindow", "Priority"))
        self.DueDate.setText(_translate("MainWindow", "DueDate"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.msg.setText(_translate("MainWindow", "Task"))
        self.Folder.setText(_translate("MainWindow", "Folder"))
        self.label_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Folder"))
        self.label_4.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "1."))
        self.label_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Label"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label.setText(_translate("MainWindow", "5"))
        self.Slno.setText(_translate("MainWindow", "Slno"))
        self.Priority.setText(_translate("MainWindow", "Priority"))
        self.SearchBar.setPlaceholderText(_translate("MainWindow", "Search"))
        self.addTasbkttn.setText(_translate("MainWindow", "+ Add Task"))
        self.searchBttn.setText(_translate("MainWindow", "🔍"))
        self.tabWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_10.setText(_translate("MainWindow", "Folder"))
        self.label_6.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "5"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.pushButton_9.setText(_translate("MainWindow", "DueDate"))
        self.label_8.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Label"))
        self.Priority_2.setText(_translate("MainWindow", "Priority"))
        self.pushButton_11.setText(_translate("MainWindow", "Slno"))
        self.msg_2.setText(_translate("MainWindow", "Task"))
        self.label_9.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "1."))
        self.label_7.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Label"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Folder1), _translate("MainWindow", "Folder-1"))
        self.pushButton_12.setText(_translate("MainWindow", "Folder"))
        self.label_10.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "5"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.pushButton_13.setText(_translate("MainWindow", "DueDate"))
        self.label_11.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Label"))
        self.Priority_3.setText(_translate("MainWindow", "Priority"))
        self.pushButton_14.setText(_translate("MainWindow", "Slno"))
        self.msg_3.setText(_translate("MainWindow", "Task"))
        self.label_12.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "1."))
        self.label_13.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">5</p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Label"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Folder11), _translate("MainWindow", "Folder-2"))
        self.addFolderbttn.setText(_translate("MainWindow", "+ Add Folder"))