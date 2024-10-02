#tested
from mysql.connector import MySQLConnection,Error,errorcode
import datetime
import math

DEFAULT_FOLDER_COLOR =  "#888888"
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
class Tasks:   

    def __init__(self,conn:MySQLConnection):
        self.conn = conn
        tables = self.getTables()
        tv = fv = rv = 0 #folder and task version
        for i in tables:
            print(i)
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

    
    def checkConnection(func):
        #checks if the connection has terminated, and can be used to handle that exception,
        # along with  any other common exceptions that are to be handled by more than 1 function
        def wrapper(self,*args,**kwargs):
            if not self.conn.is_connected():
                raise ConnectionError("CONNECTION NO LONGER EXISTS")
            func(self,*args,**kwargs)
        return wrapper
    
    def getTables(self):#returns a list of all tables with its versions in the database
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
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT RevivalInterval, RevivalType, DOC FROM RevT WHERE ID={ID}")
            L = cur.fetchall()            
            if L:
                RevInterval,revtype,doc = L[0]
                if revtype.lower() == 'a':
                    Revdt = datetime.datetime.now() + datetime.timedelta(seconds=RevInterval)
                elif revtype.lower() == 'e':
                    x:datetime.timedelta = (datetime.datetime.now() - doc)
                    n:int = math.ceil(x.total_seconds()/RevInterval)
                    Revdt = doc + datetime.timedelta(seconds=n * RevInterval)
                cur.execute("UPDATE RevT SET Revivaldt=%s WHERE ID = %s",(Revdt,ID))
            cur.execute(f"UPDATE Tasks SET isCompleted=TRUE WHERE ID={ID}")
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

    def addTask(self, msg: str, priority: int = 5, dt: datetime.datetime = None, folder: str = None,
                ReviveInterval: int = None, Revivaldt:datetime.datetime=None, RevivalType:str = 'e' ):
        # Prepare the SQL statement with placeholders
        # Revivaldt must not be given for Recurring functions
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

            if ReviveInterval:
                if dt: print("Please don't give deadline for a recureing function :)")
                DOC= datetime.datetime.now()
                revdt= datetime.datetime.now() + datetime.timedelta(seconds=ReviveInterval)
                cur.execute("INSERT INTO RevT(ID,Revivaldt,RevivalType, RevivalInterval, Doc) \
                            VALUES(%s,%s, %s, %s,%s)",(ID,revdt,RevivalType, ReviveInterval,DOC)) 
            self.conn.commit()
            
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
    def addFolder(self, folder_name:str, colorhex:str = DEFAULT_FOLDER_COLOR):
        self.execute(f"INSERT INTO Folders(Folder_name,color) VALUES('{folder_name}', '{colorhex}')")
        self.conn.commit()
    
    def delFolder(self,folder_name:str):
        self.execute(f"DELETE FROM FOLDERS WHERE folder_name='{folder_name}'")
        self.conn.commit()
    
    def updateFolder(self,old_folder_name:str, new_folder_name:str, colorhex:str=''):
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
    
    def fetchall(self,order_by:str='slno',folder:str=''):
        with self.conn.cursor() as cur:
            if folder:
                cur.execute(f"SELECT * FROM Tasks GROUP BY {folder} ORDER BY {order_by}")
            else:
                cur.execute(f"SELECT * FROM Tasks ORDER BY {order_by}")
            r = cur.fetchall()
        return r
    
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
            
    

class info:
    def __init__(self, conn:MySQLConnection, Table:str):
        self.Table=Table
        self.conn=conn
    
    def ID(self, msg:str):
        with self.conn.cursor() as cur:
            cur.execute("SELECT ID FROM Tasks WHERE msg=%s",(msg,))
            r=cur.fetchone()
            if r: return r[0]
            else: print("Task not present")
    def slno(self, ID:int):
        if self.Table.lower()=='tasks':
            with self.conn.cursor() as cur:
                cur.execute("SELECT slno FROM Tasks WHERE ID=%s",(ID,))
                r=cur.fetchone()
                if r: return r[0]
        else: print("Column not present in the given Table")

    def msg(self,ID:int):
        if self.Table.lower()=='tasks':
            with self.conn.cursor() as cur:
                cur.execute("SELECT msg FROM Tasks WHERE ID=%s",(ID,))
                r=cur.fetchone()
                if r: return r[0].capitalize()
        else: print("Column not present in the given Table")

    def priority(self,ID:int):
        if self.Table.lower()=='tasks':
            with self.conn.cursor() as cur:
                cur.execute("SELECT priority FROM Tasks WHERE ID=%s",(ID,))
                r=cur.fetchone()
                if r: return r[0]
        else: print("Column not present in the given Table")

    def deadline(self,ID:int):
        if self.Table.lower()=='tasks':
            with self.conn.cursor() as cur:
                cur.execute("SELECT dt FROM Tasks WHERE ID=%s",(ID,))
                r=cur.fetchone()
                if r: return r[0]
        else: print("Column not present in the given Table")

    def folder(self,ID:int):
        if self.Table.lower()=='tasks':
            with self.conn.cursor() as cur:
                cur.execute("SELECT folder FROM Tasks WHERE ID=%s",(ID,))
                r=cur.fetchone()
                if r: return r[0]
        else: print("Column not present in the given Table")

    def iscompleted(self,ID:int):
        if self.Table.lower()=='tasks':
            with self.conn.cursor() as cur:
                cur.execute("SELECT iscompleted FROM Tasks WHERE ID=%s",(ID,))
                r=cur.fetchone()
                if r: return r[0]
        else: print("Column not present in the given Table")


    def Revivaldt(self,ID:int):
        if self.Table.lower()=='revt':
            with self.conn.cursor() as cur:
                cur.execute("SELECT Revivaldt FROM RevT WHERE ID=%s",(ID,))
                r=cur.fetchone()
                if r: return r[0]
        else: print("COlumn not present in the given table")

    def RevivalInterval(self,ID:int):
        if self.Table.lower()=='revt':
            with self.conn.cursor() as cur:
                cur.execute("SELECT RevivalInterval FROM RevT WHERE ID=%s",(ID,))
                r=cur.fetchone()
                if r: return r[0]
        else: print("COlumn not present in the given table")

    def RevivalType(self,ID:int):
        if self.Table.lower()=='revt':
            with self.conn.cursor() as cur:
                cur.execute("SELECT RevivalType FROM RevT WHERE ID=%s",(ID,))
                r=cur.fetchone()
                if r: return r[0]
        else: print("COlumn not present in the given table")

    
    def selectfolders(self):
        if self.Table.lower()=='folders':
            with self.conn.cursor() as cur:
                cur.execute("SELECT Folder_name FROM Folders")
                r=cur.fetchall()    #List of Tuples
                return [i[0] for i in r] if r else []


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
