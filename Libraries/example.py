#import Tasks
import  mysql.connector as m
import datetime
from Tasks import Tasks

conn = m.connect(user='root',passwd='',database='yourdatabase',host='localhost')

a = Tasks(conn)
a.addFolder("folder1")
a.addTask("hei",4,folder='folder1')
a.addTask("heyy",6,datetime.datetime(2024,2,4,6,7,3),'folder1')
a.updateFolder('folder1','folder1.1')

a.addFolder('folder2')
a.addTask("haia",7,folder='folder2')
a.addTask("yaha",4)
a.delFolder("folder2")

conn.close()
