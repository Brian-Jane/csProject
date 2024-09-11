#import Tasks
import  mysql.connector as m
import datetime
from Tasks import Tasks
from Tasks import info

conn = m.connect(user='root',passwd='',database='yourdatabase',host='localhost')

a = Tasks(conn)
a.addTask("hei",4,folder='folder1')
a.addTask("heyy",6,datetime.datetime(2024,2,4,6,7,3),'folder1')

a.addTask("haia",7,folder='folder2')
a.addTask("yaha",4)
a.delFolder("folder2")

#Examples of info class     When entering string, it is case insensitive
i=info(conn, Table='Tasks')
i.ID(msg="hei")
i.msg(ID=3) 
i.iscompleted(i.ID("hei"))

conn.close()
