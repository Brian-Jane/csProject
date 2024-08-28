#tested
from mysql.connector import MySQLConnection,Error,errorcode
import datetime

DEFAULT_FOLDER_COLOR =  "#888888"
TABLE_VERSION = '2.0'
EVENT_TABLE_VERSION= '1.0'

CREATE_COMMAND_TASKS = f"CREATE TABLE Tasks(slno INT AUTO_INCREMENT PRIMARY KEY,\
        msg varchar(100),\
        priority INT,\
        dt DATETIME,\
        Folder VARCHAR(30),\
        isCompleted BOOLEAN DEFAULT FALSE,\
        Revivaldt DATETIME,\
        RevInterval INT,\
        CHECK (priority BETWEEN 1 AND 10),\
        CONSTRAINT fkFolders \
            FOREIGN KEY(Folder) REFERENCES Folders(folder_name) ON DELETE CASCADE ON UPDATE CASCADE)\
        COMMENT '{TABLE_VERSION}'" #Current schema of the Tasks table
    
CREATE_COMMAND_FOLDERS= f"CREATE TABLE Folders(Folder_name VARCHAR(30) PRIMARY KEY,\
    color CHAR(7) DEFAULT('{DEFAULT_FOLDER_COLOR}'))\
    COMMENT '{TABLE_VERSION}'"


CREATE_COMMAND_EVENTS= f"CREATE TABLE Events(slno int AUTO_INCREMENT primary key , \
        msg varchar(20)), \
        description varchar(100), \
        Edate datetime)\
        COMMENT '{EVENT_TABLE_VERSION}'"

class Tasks:   

    def __init__(self,conn:MySQLConnection):
        self.conn = conn
        tables = self.getTables()
        tv = fv = 0 #folder and task version
        for i in tables:
            print(i)
            if i[0] == 'folders':fv = i[1]
            elif i[0] == 'tasks':tv = i[1]
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS TEMPTasks")
            cur.execute("DROP TABLE IF EXISTS TEMPFolders")
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
                    cur.execute("DROP TABLE TEMPTasks")
                else:                    
                    cur.execute(CREATE_COMMAND_TASKS) 
            self.checkRevival(False)    
            self.conn.commit()

    def checkRevival(self,commit=True):
        with self.conn.cursor() as cur:
            cur.execute("UPDATE Tasks SET isCompleted=FALSE WHERE NOW()>Revivaldt")
        if commit:self.conn.commit()

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
    def execute(self, cmd:str):
        conn = self.conn
        x = 2 #x number of re-tries
        Err = 0
        while x>0:
            try:
                with conn.cursor() as cur:
                    cur.execute(cmd)
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

    def completeTask(self,slno:int):
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT RevInterval FROM Tasks WHERE slno={slno}")
            L = cur.fetchall()
            assert len(L) == 1
            if L[0][0]!=None:
                Revivaldt = datetime.datetime.now() + datetime.timedelta(seconds=L[0][0])
                cur.execute(f"UPDATE Tasks SET Revivaldt='{Revivaldt}' WHERE slno={slno}")
            cur.execute(f"UPDATE Tasks SET isCompleted=TRUE WHERE slno={slno}")
        self.conn.commit()

    def addTask(self, msg: str, priority: int = 5, dt: datetime.datetime = None, folder: str = None, ReviveInterval: int = None):
        # Prepare the SQL statement with placeholders
        with self.conn.cursor() as cur:
            sql = """
            INSERT INTO Tasks (msg, priority, dt, folder, RevInterval)
            VALUES (%s, %s, %s, %s, %s)
            """            
            # Prepare the values to be inserted
            values = (msg, priority, dt, folder, ReviveInterval)
            
            # Execute the query with parameters
            cur.execute(sql, values)
        self.conn.commit()

    def delTask(self, slno:int):
        self.execute(f"DELETE FROM Tasks WHERE slno={slno}")
        self.execute(f"UPDATE Tasks SET slno = slno-1 WHERE slno>{slno}") #correct the gap 
        self.execute(f"ALTER TABLE Tasks AUTO_INCREMENT = 0") #reset auto increment
        self.conn.commit()
    
    def updateTask(self,  slno:int, msg:str ,priority:int = 5, dt:datetime.datetime='NULL'):
        self.execute(f"UPDATE Tasks SET msg='{msg}',priority={priority},dt={dt} WHERE slno={slno}")
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
    
    def SearchTask(self,t):
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT msg FROM Task WHERE msg='{t}'")      
            L=cur.fetchall()        #List of tuples of tasks
            return L
    
    def filter(self, Status='', DueDate:datetime.datetime=None, Priority:int=0,  Folder:int=""):
        Criteria=[]
        with self.conn.cursor() as cur:
            if Status!='': Criteria.append(f"status='{Status}'")
            if DueDate: Criteria.append(f"dt='{DueDate}'")
            if Priority: Criteria.append(f"priority={Priority}")
            if Folder: Criteria.append(f"folder='{Folder}'")

            q="AND".join(Criteria)
            cur.execute(f"SELECT * FROM Tasks WHERE {q}")
            return cur.fetchall()

    def modify(self, slno:int, task:str='', dt:datetime.datetime=None, Priority:int=0, Folder:str=''):
        with self.conn.cursor() as cur:
            Condition=[]
            if task: 
                Condition.append(f"msg='{task}'")
            if dt:
                Condition.append(f"dt='{dt}'")
            if Priority:
                Condition.append(f"Priority={Priority}")
            if Folder:
                Condition.append(f"Folder='{Folder}'")
            Condition_str= ', '.join(Condition)
            cur.execute(f"UPDATE Tasks SET {Condition_str} WHERE slno={slno}")
            self.conn.commit()

    

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