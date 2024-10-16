#tested
from mysql.connector import MySQLConnection,Error,errorcode
import datetime
import threading
import math

DEFAULT_FOLDER_COLOR =  "#FFFFFF"
TABLE_VERSION = '2.0'
EVENT_TABLE_VERSION= '1.0'
REV_TABLE_VERSION = '2.0'

CREATE_COMMAND_TASKS = f"CREATE TABLE Tasks(ID INT PRIMARY KEY,\
        slno INT AUTO_INCREMENT UNIQUE,\
        msg varchar(100),\
        priority INT,\
        dt DATETIME,\
        Folder VARCHAR(30),\
        isCompleted BOOLEAN DEFAULT FALSE,\
        CHECK (priority BETWEEN 1 AND 10),\
        CONSTRAINT fkFolders \
            FOREIGN KEY(Folder) REFERENCES Folders(folder_name) ON DELETE CASCADE ON UPDATE CASCADE)\
        COMMENT '{TABLE_VERSION}'" #Current schema of the Tasks table       #msg is always in lower caps
    
CREATE_COMMAND_FOLDERS= f"CREATE TABLE Folders(Folder_name VARCHAR(30) PRIMARY KEY,\
    color CHAR(7) DEFAULT '{DEFAULT_FOLDER_COLOR}' )\
    COMMENT '{TABLE_VERSION}'"


REV_TABLE_VERSION = "1.0"  # Define this variable as needed

CREATE_COMMAND_REVT = f"""
CREATE TABLE REVT (
    ID INT,
    Revivaldt DATETIME,
    RevivalInterval INT,
    RevivalType CHAR(1),
    DOC DATETIME DEFAULT NOW(),
    CONSTRAINT fkTasks
        FOREIGN KEY(ID) REFERENCES Tasks(ID) ON DELETE CASCADE ON UPDATE CASCADE
)
COMMENT '{REV_TABLE_VERSION}'
"""     #RevivalType= "A/a" or "E/e"    DOC--> Date Of Creation

CREATE_COMMAND_EVENTS= f"CREATE TABLE Events(slno int AUTO_INCREMENT primary key , \
        msg varchar(20)), \
        description varchar(100), \
        Edate datetime)\
        COMMENT '{EVENT_TABLE_VERSION}'"

default_value = object()
class Filter:
    def __init__(self):
        self.conditions = {self.priorityHigherThan:"Tasks.Priority>%s",
                           self.priorityLowerThan:"Tasks.Priority<%s",
                           self.dateBefore:"Tasks.dt<%s",
                           self.folder:"Tasks.Folder = %s",
                           self.completedTask:"Tasks.isCompleted=%s",
                           self.searchMsg:"Tasks.msg like %s"}
        self.param = {}
    def searchMsg(self,msg:str):
        self.param[self.searchMsg] = "%"+msg+"%"
    def priorityLowerThan(self,num:int):
        """ the priority is lower than num"""
        self.param[self.priorityLowerThan] = num
    def priorityHigherThan(self,num:int):
        """ the priority is higher than num"""
        self.param[self.priorityHigherThan] = num
    def dateBefore(self,date:datetime.datetime):
        """the due date is before given date"""
        self.param[self.dateBefore] = date
    def folder(self,folder:str):
        self.param[self.folder] = folder
    def completedTask(self,status:bool):
        """task must be completed (true) or not completed(false)"""
        self.param[self.completedTask] = status
    def undo(self,function):
        """undoes the effect of any of the functions (removes that parameter)"""
        self.param.pop(function)
    def undoFolder(self,folder:str):
        """removes that folder from the list"""
        self.folders.remove(folder)
    def generateWhereClause(self):
        conditions = []
        values = ()
        for i in self.param:
            val = self.param[i]
            
            conditions.append(self.conditions[i])
            values+=(val,)
        query = ' AND '.join(conditions)
        print(query,values)
        return query,values
    
class Tasks:   

    def __init__(self,conn:MySQLConnection):
        self.conn = conn
        tables = self.getTables()
        tv = fv = rv = 0 #folder and task version
        for i in tables:
            if i[0] == 'folders':fv = i[1]
            elif i[0] == 'tasks':tv = i[1]
            elif i[0] == 'revt':rv = i[1]
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS TEMPTasks")
            cur.execute("DROP TABLE IF EXISTS TEMPFolders")
            cur.execute("DROP TABLE IF EXISTS TEMPRevt")
            if fv!=TABLE_VERSION: #Since Folders is the parent table, it has to be created first.               
                if fv!=0:#outdated table does exist, as opposed to no table at all
                    cur.execute("RENAME TABLE Folders to TEMPFolders")           
                    cur.execute(CREATE_COMMAND_FOLDERS)                 
                    cur.execute("INSERT INTO Folders SELECT * FROM TEMPFolders")
                    if tv!=0:
                        cur.execute("ALTER TABLE Tasks DROP FOREIGN KEY fkFolders")
                        cur.execute("ALTER TABLE Tasks ADD CONSTRAINT fkFolders \
                                    FOREIGN KEY(Folder) REFERENCES Folders(folder_name) \
                                    ON UPDATE CASCADE ON DELETE CASCADE")
                    cur.execute("DROP TABLE TEMPFolders")
                else:                    
                    cur.execute(CREATE_COMMAND_FOLDERS)
            
            if tv!=TABLE_VERSION:
                
                if tv!=0:#outdated table does exist, as opposed to no table at all
                    cur.execute("ALTER TABLE Tasks DROP FOREIGN KEY fkFolders")
                    cur.execute("RENAME TABLE Tasks to TEMPTasks")                    
                    cur.execute(CREATE_COMMAND_TASKS)                 
                    cur.execute("INSERT INTO Tasks SELECT * FROM TEMPTasks")
                    if rv!=0:
                        cur.execute("ALTER TABLE RevT DROP FOREIGN KEY fkTasks")
                        cur.execute("ALTER TABLE RevT ADD CONSTRAINT fkTasks \
                                    FOREIGN KEY(ID) REFERENCES Tasks(ID) \
                                    ON UPDATE CASCADE ON DELETE CASCADE")
                        
                    cur.execute("DROP TABLE TEMPTasks")
                else:                    
                    cur.execute(CREATE_COMMAND_TASKS) 
            
            if rv!=REV_TABLE_VERSION:
                if rv!=0:
                    cur.execute("ALTER TABLE RevT DROP FOREIGN KEY fkTasks")
                    cur.execute("RENAME TABLE RevT to TEMPRevT")                    
                    cur.execute(CREATE_COMMAND_REVT)                 
                    cur.execute("INSERT INTO RevT SELECT * FROM TEMPRevT")
                    cur.execute("DROP TABLE TEMPRevT")
                else:                    
                    cur.execute(CREATE_COMMAND_REVT)
            self.checkRevival(False)
            self.conn.commit()

    def refresh(self):
        self.conn.reconnect() #FOR DEBUGGING
        self.checkRevival()

    def checkConnection(func):
        #checks if the connection has terminated, and can be used to handle that exception,
        # along with  any other common exceptions that are to be handled by more than 1 function
        def wrapper(self,*args,**kwargs):
            if not self.conn.is_connected():
                raise ConnectionError("CONNECTION NO LONGER EXISTS")
            func(self,*args,**kwargs)
        return wrapper
    
    def getTables(self):
        """returns a list of all tables with its versions in the database"""

        with self.conn.cursor() as cur:
            cur.execute(f"SELECT table_name, table_comment FROM information_schema.tables\
                        WHERE table_schema='{self.conn.database}'") #queries all the tables from database
            x = cur.fetchall()
        return x

    @checkConnection
    def execute(self, cmd:str,values=()):
        conn = self.conn
        x = 2 #x number of re-tries
        Err = 0
        while x>0:
            try:
                with conn.cursor() as cur:
                    if values:
                        print(cmd,values)
                    cur.execute(cmd,values)
                break
            except Error as e:
                Err = e
                x-=1
                if e.errno == errorcode.ER_NO_SUCH_TABLE:
                    self.createTable(conn)
                    conn.commit()
                #elif blocks to handle any other exceptions
                else:
                    raise e
        else: #while else
            return 0 #return 0 if execution occured successfully
        return Err #return the error if execution gets stuck on "NO SUCH TABLE" error, 
        #or you can re raise the error

    def extract(self,Type:str='T'):     
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT slno, msg, priority, dt WHERE type='{Type}'")
            return cur.fetchall()
        
    def checkRevival(self,commit=True):
        with self.conn.cursor() as cur:
            cur.execute("UPDATE Tasks,Revt SET isCompleted=FALSE WHERE NOW()>Revivaldt AND\
                        Tasks.ID = Revt.ID")
        if commit:self.conn.commit()

    def completeTask(self,ID:int):
        """Completes Task"""
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT RevivalInterval, RevivalType, DOC FROM RevT WHERE ID={ID}")
            L = cur.fetchall()            
            if L:
                RevInterval,revtype,doc = L[0]
                if revtype == 'a':
                    Revdt = datetime.datetime.now() + datetime.timedelta(seconds=RevInterval)
                elif revtype == 'e':
                    x:datetime.timedelta = (datetime.datetime.now() - doc)
                    n:int = math.ceil(x.total_seconds()/RevInterval)
                    Revdt = doc + datetime.timedelta(seconds=n * RevInterval)
                cur.execute("UPDATE RevT SET Revivaldt=%s WHERE ID = %s",(Revdt,ID))
            cur.execute(f"UPDATE Tasks SET isCompleted=TRUE WHERE ID={ID}")
        self.conn.commit()
    def redoTask(self,ID:int):
        with self.conn.cursor() as cur:
            cur.execute("UPDATE Tasks SET isCompleted=FALSE WHERE Tasks.ID=%s",(ID,))
        self.conn.commit()
    def getRevdt(self,ID:int):
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT RevivalInterval, RevivalType, DOC FROM RevT WHERE ID={ID}")
            L = cur.fetchall()            
            if L:
                RevInterval,revtype,doc = L[0]
                if revtype.lower() == 'a':
                    raise TypeError("only e type functions are allowed")
                elif revtype.lower() == 'e':
                    x:datetime.timedelta = (datetime.datetime.now() - doc)
                    n:int = math.ceil(x.total_seconds()/RevInterval)
                    Revdt = doc + datetime.timedelta(seconds=n * RevInterval)
                return Revdt

    def isCompleted(self,ID:int) ->bool:
        """Checks whether a Task is completed"""
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT isCompleted FROM Tasks WHERE ID=%s",(ID,) )
                return(cur.fetchone()[0])
        except AttributeError:
            return "ID passed is none."

    def addTask(self, msg: str, priority: int = 5, dt: datetime.datetime = None, folder: str = None,
                ReviveInterval: int = None, Revivaldt:datetime.datetime=None, RevivalType:str = 'e' ):
        """Adds task"""
        # Prepare the SQL statement with placeholders
        # Revivaldt must not be given for Recurring functions
        DOC= datetime.datetime.now()
        with self.conn.cursor() as cur:
            sql = """
            INSERT INTO Tasks (ID,msg, priority, dt, folder)
            VALUES (%s, %s, %s, %s, %s)
            """            
            # Prepare the values to be inserted
            ID = self._genID()
            values = (ID,msg, priority, dt, folder)
            cur.execute("SELECT msg from Tasks")
            if (msg,) in cur.fetchall(): 
                print("Don't repeat tasks")
                return None
            # Execute the query with parameters
            cur.execute(sql, values)
            self.conn.commit()

            if ReviveInterval:      #RevivalInterval is in seconds
                if dt: print("Please don't give deadline for a recureing function :)")
                revdt= datetime.datetime.now() + datetime.timedelta(seconds=ReviveInterval)
                cur.execute("INSERT INTO RevT(ID,Revivaldt,RevivalType, RevivalInterval, Doc) \
                            VALUES(%s,%s, %s, %s,%s)",(ID,revdt,RevivalType, ReviveInterval,DOC)) 
            self.conn.commit()

            slno = self.fetchall(order_by='Tasks.slno')[-1].slno + 1
            task=taskobject(ID,slno,msg,priority,dt,folder,RevivalType=RevivalType,RevivalInterval=ReviveInterval,DOC=DOC,Revivaldt=Revivaldt,color=DEFAULT_FOLDER_COLOR)

            return task
            
    def _genID(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT ID FROM Tasks")
            idList = cur.fetchall()
            if (1,) not in idList: return 1
            for (i,) in idList:
                if (i+1,) not in idList:
                    return i+1
            raise Exception("BRUHHH")
                

    def delTask(self, slno:int):
        self.execute(f"DELETE FROM Tasks WHERE slno={slno}")
        self.execute(f"UPDATE Tasks SET slno = slno-1 WHERE slno>{slno}") #correct the gap 
        self.execute(f"ALTER TABLE Tasks AUTO_INCREMENT = 0") #reset auto increment
        self.conn.commit()
    
    def updateTask(self,  slno:int, **kwargs):
        msg=''
        q1 = "UPDATE Tasks SET "
        q2 = "UPDATE RevT SET"
        Lq1,Lq2,Lv1,Lv2 = [],[],[],[]
        for column in kwargs:
            if column not in ['msg','priority','dt','Folder']:
                raise ValueError(f"'{column}' is an unknown column")
            
            if column in ['msg','priority','dt','Folder']:
                Lq1.append(f'{column}=%s')
                if column=='msg':
                    Lv1.append(kwargs[column].lower())
                else:
                    Lv1.append(kwargs[column])
            if column in ['RevivalInterval', 'RevivalType']: 
                Lq2.append(f'{column}=%s')
                Lv2.append(kwargs[column])
            
        query1  = q1 + ','.join(Lq1) + "WHERE slno=%s"
        query2 = q2 + ','.join(Lq2) + "WHERE slno=%s"
        Lv1.append(slno)
        Lv2.append(slno)
        if Lv1[1:]:self.execute(query1,Lv1)
        if Lv2[1:]:self.execute(query2,Lv2)
        self.conn.commit()

    def searchTask(self, task:str) ->list:
        """Searches for a task"""
        TaskList=[]
        with self.conn.cursor() as cur:
            cur.execute(f"""SELECT {','.join(taskobject.attributes)}
                        FROM Tasks LEFT JOIN Revt ON Tasks.ID = Revt.ID
                        LEFT JOIN Folders ON Tasks.Folder = Folders.folder_name
                        WHERE msg='{task}'""")
            for i in cur:
                t = taskobject(*i) #passes the tuple i as arguments
                TaskList.append(t)
        print(len(TaskList),"items in TaskList")
        return TaskList
    
    def addFolder(self, folder_name:str, colorhex:str = DEFAULT_FOLDER_COLOR):
        """Adds a Folder"""
        for i,c in self.fetchFolders():
            if i == folder_name:
                print("don't repeat folders")
                return None
        self.execute(f"INSERT INTO Folders(Folder_name,color) VALUES('{folder_name}', '{colorhex}')")
        self.conn.commit()
        return (folder_name,colorhex)
    
    def delFolder(self,folder_name:str):
        """Deletes a folder"""
        self.execute(f"DELETE FROM FOLDERS WHERE folder_name='{folder_name}'")
        self.conn.commit()
    
    def updateFolder(self,old_folder_name:str, new_folder_name:str, colorhex:str=''):
        """Updates Folder"""
        if colorhex:
            self.execute(f"UPDATE Folders SET folder_name='{new_folder_name}',color='{colorhex}'\
                        WHERE folder_name='{old_folder_name}'")
        else:
            self.execute(f"UPDATE Folders SET folder_name='{new_folder_name}'\
                        WHERE folder_name='{old_folder_name}'")
        self.conn.commit()
    
    def reorderTasks(self,slno:int,new_pos_slno:int):
        self.execute(f"UPDATE Tasks SET slno=0 where slno={slno}")
        if(slno > new_pos_slno):
            self.execute(f"UPDATE Tasks SET slno=slno+1 WHERE slno BETWEEN {new_pos_slno} AND {slno} ORDER BY slno DESC")
        else:
            self.execute(f"UPDATE Tasks SET slno=slno-1 WHERE slno BETWEEN {slno} AND {new_pos_slno} ORDER BY slno ASC")
        self.execute(f"UPDATE Tasks SET slno={new_pos_slno} WHERE slno=0")
        self.conn.commit()
    
    def fetchall(self,order_by:str='Tasks.slno',folder:str='',filter:Filter=Filter(),filter2 = Filter()):
        if order_by not in taskobject.attributes:
            print(order_by)
            raise ValueError("The order by argument must be a valid attribute")
        whereClause,whereParam = filter.generateWhereClause()
        if filter2.param:
            a,b = filter2.generateWhereClause()
            whereClause += " AND "+ a
            whereParam +=b
        if whereClause:
            whereClause = "WHERE "+whereClause
        clause = whereClause+f" ORDER BY {order_by}"
        param = whereParam
        if folder:
            clause = " GROUP BY %s" + clause
            param = (folder,)+param 
        TaskList = []
    
        with self.conn.cursor() as cur:
            cur.execute(f"""SELECT {','.join(taskobject.attributes)}
                        FROM Tasks LEFT JOIN Revt ON Tasks.ID = Revt.ID
                        LEFT JOIN Folders ON Tasks.Folder = Folders.folder_name
                        {clause}""",param) #left joined table for reviving tasks
            for i in cur:
                t = taskobject(*i) #passes the tuple i as arguments
                TaskList.append(t)
        return TaskList
    
    def fetchFolders(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM Folders")
            return cur.fetchall()
        
    def close(self):
        self.conn.close()
    
    def filter(self, msg: str='', Status='', DueDate:datetime.datetime=None, Priority:int=0,  Folder:int=""):
        Criteria=[]
        with self.conn.cursor() as cur:
            if Status!='': Criteria.append(f"iscompleted='{Status}'")
            if DueDate: Criteria.append(f"dt='{DueDate}'")
            if Priority: Criteria.append(f"priority={Priority}")
            if Folder: Criteria.append(f"folder='{Folder}'")
            if msg:
                msg=msg
                Criteria.append(f"msg LIKE '%{msg}%'")

            q="AND".join(Criteria)
            cur.execute(f"SELECT * FROM Tasks WHERE {q}")
            return cur.fetchall()
           
class taskobject:
    # Make sure the instance is not None.
    # While adding task, if the task is repeated, then it will give None.
    attributes = ['Tasks.ID','Tasks.slno','Tasks.msg',
                  'Tasks.priority','Tasks.dt','Tasks.folder',
                  'Folders.color','Revt.RevivalType','Revt.RevivalInterval',
                  'Revt.DOC','Revt.Revivaldt']
    
    revAttributes = ['RevivalType','RevivalInterval','DOC','Revivaldt']
    taskAttributes = ['ID','slno','msg','priority','dt','folder']
    folderAttributes  = ['color']
    def __init__(self,ID,slno,msg,priority,dt,folder,color,RevivalType=None,RevivalInterval=None,DOC=None,Revivaldt=None):
        self.ID = ID
        self.slno = slno
        self.msg = msg
        self.priority = priority
        self.dueDate = dt
        self.folder = folder
        self.color = color
        self.RevType = RevivalType
        self.RevInterval = RevivalInterval
        self.Revdate = Revivaldt
        self.DOC = DOC
    def __str__(self):
        string = f"""TaskID:{self.ID}
slno:{self.slno}
msg:{self.msg}
priority:{self.priority}
dueDate:{self.dueDate}
folder:{self.folder}
color:{self.color}
revType:{self.RevType}
revInterval:{self.RevInterval}
doc:{self.DOC}
revdt:{self.Revdate}
""" 
        return string

class Event:
    def __init__(self, conn:MySQLConnection):
        self.conn=conn
        with conn.cursor() as cur:
            tables = self.getTables()
            ev = 0
            for i in tables:
                if i[0]=='events':ev=i[1]
            if ev!=EVENT_TABLE_VERSION:
                if ev!=0:
                    cur.execute("RENAME TABLE Events to TEMPEvents")                    
                    cur.execute(CREATE_COMMAND_EVENTS)                 
                    cur.execute("INSERT INTO Events SELECT * FROM TEMPEvents")
                    cur.execute("DROP TABLE TEMPEvents")
                else:                    
                    cur.execute(CREATE_COMMAND_EVENTS)

            cur.execute(CREATE_COMMAND_EVENTS)
        conn.commit()

    def getTables(self):#returns a list of all tables with its versions in the database
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT table_name, table_comment FROM information_schema.tables\
                        WHERE table_schema='{self.conn.database}'") #queries all the tables from database
            x = cur.fetchall()
        return x
    
    def execute(self,query):
        with self.conn.cursor() as cur:
            cur.execute(query)
    
    def addEvents(self, msg:str ,priority:int = 5, dt:datetime.datetime='', folder:str=''):
        if folder:folder = f'"{folder}"' #annoyingly enough mysql needs quotes around string
        else:folder = "NULL"             #but quotes around "NULL" immediately makes it a string of "NULL", so this
        if dt!='':dt = f'"{str(dt)}"' #same issue
        else: dt = 'NULL'
        self.execute(f"INSERT INTO Events(msg,priority,dt,folder) VALUES\
                    ('{msg}',{priority},{str(dt)},{folder})")    
        self.conn.commit()

    def delEvents(self, slno:int):
        self.execute(f"DELETE FROM Events WHERE slno={slno}")
        self.execute(f"UPDATE Events SET slno = slno-1 WHERE slno>{slno}") #correct the gap 
        self.execute(f"ALTER TABLE Events AUTO_INCREMENT = 0") #reset auto increment
        self.conn.commit()
    
    def updateEvents(self,  slno:int, msg:str ,priority:int = 5, dt:datetime.datetime='NULL'):
        self.execute(f"UPDATE Events SET msg='{msg}',priority={priority},dt={dt} WHERE slno={slno}")
        self.conn.commit()

    def reorderEvents(self,slno:int,new_pos_slno:int):
        self.execute(f"UPDATE Events SET slno=0 where slno={slno}")
        if(slno > new_pos_slno):
            self.execute(f"UPDATE Events SET slno=slno+1 WHERE slno BETWEEN {new_pos_slno} AND {slno} ORDER BY slno DESC")
        else:
            self.execute(f"UPDATE Events SET slno=slno-1 WHERE slno BETWEEN {slno} AND {new_pos_slno} ORDER BY slno ASC")
        self.execute(f"UPDATE Events SET slno={new_pos_slno} WHERE slno=0")
        self.conn.commit()
    
    def modify(self, slno:int, event:str='', dt:datetime.datetime=None):
        with self.conn.cursor() as cur:
            Condition=[]
            if event: 
                Condition.append(f"msg='{event}'")
            if dt:
                Condition.append(f"dt='{dt}'")

            Condition_str= ', '.join(Condition)
            cur.execute(f"UPDATE Events SET {Condition_str} WHERE slno={slno}")
            self.conn.commit()
