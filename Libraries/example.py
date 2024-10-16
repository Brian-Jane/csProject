#import Tasks
import  mysql.connector as m
import datetime
from Tasks import Tasks

conn = m.connect(user='root',passwd='0000',database='csp',host='localhost')

a = Tasks(conn)
a.updateTask(108,msg="Task-30")

conn.close()
