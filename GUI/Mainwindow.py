# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 652)
        font = QtGui.QFont()
        font.setPointSize(4)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout.addWidget(self.line_14)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(72, 237, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.TasksPage = QtWidgets.QWidget()
        self.TasksPage.setObjectName("TasksPage")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.TasksPage)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.addFolderbttn = QtWidgets.QPushButton(self.TasksPage)
        self.addFolderbttn.setMinimumSize(QtCore.QSize(150, 0))
        self.addFolderbttn.setCheckable(True)
        self.addFolderbttn.setObjectName("addFolderbttn")
        self.verticalLayout_3.addWidget(self.addFolderbttn)
        self.scrollArea = QtWidgets.QScrollArea(self.TasksPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 148, 242))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.Today = QtWidgets.QPushButton(self.TasksPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Today.setFont(font)
        self.Today.setCheckable(True)
        self.Today.setObjectName("Today")
        self.verticalLayout_3.addWidget(self.Today)
        self.CompletedTasks = QtWidgets.QPushButton(self.TasksPage)
        self.CompletedTasks.setCheckable(True)
        self.CompletedTasks.setObjectName("CompletedTasks")
        self.CompletedTasks.setCheckable(True)
        self.verticalLayout_3.addWidget(self.CompletedTasks)
        self.filter = QtWidgets.QPushButton(self.TasksPage)
        self.filter.setCheckable(True)
        self.filter.setObjectName("filter")
        self.verticalLayout_3.addWidget(self.filter)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.TasksPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 148, 242))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SearchBar = QtWidgets.QLineEdit(self.TasksPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SearchBar.setFont(font)
        self.SearchBar.setObjectName("SearchBar")
        self.horizontalLayout_2.addWidget(self.SearchBar)
        self.searchBttn = QtWidgets.QPushButton(self.TasksPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchBttn.setFont(font)
        self.searchBttn.setStyleSheet("")
        self.searchBttn.setCheckable(True)
        self.searchBttn.setChecked(False)
        self.searchBttn.setObjectName("searchBttn")
        self.horizontalLayout_2.addWidget(self.searchBttn)
        self.addTasbkttn = QtWidgets.QPushButton(self.TasksPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addTasbkttn.setFont(font)
        self.addTasbkttn.setObjectName("addTasbkttn")
        self.horizontalLayout_2.addWidget(self.addTasbkttn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.AllTasks_GridLayout = QtWidgets.QGridLayout()
        self.AllTasks_GridLayout.setObjectName("AllTasks_GridLayout")
        self.verticalLayout_2.addLayout(self.AllTasks_GridLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
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
        spacerItem2 = QtWidgets.QSpacerItem(78, 308, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Taskslayout_2.addItem(spacerItem2, 2, 0, 1, 1)
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
        spacerItem3 = QtWidgets.QSpacerItem(78, 308, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 2, 0, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_12.setFont(font)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout_3.addWidget(self.line_12, 0, 5, 3, 1)
        self.tabWidget.addTab(self.Folder11, "")
        self.stackedWidget.addWidget(self.FoldersPage)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "All Tasks"))
        self.addFolderbttn.setText(_translate("MainWindow", "Folders"))
        self.Today.setText(_translate("MainWindow", "☀ Today"))
        self.CompletedTasks.setText(_translate("MainWindow", "Completed Tasks"))
        self.filter.setText(_translate("MainWindow", "Filters"))
        self.SearchBar.setPlaceholderText(_translate("MainWindow", "Search"))
        self.searchBttn.setText(_translate("MainWindow", "🔍"))
        self.addTasbkttn.setText(_translate("MainWindow", "+ Add Task"))
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
