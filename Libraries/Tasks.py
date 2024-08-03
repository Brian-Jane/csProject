#tested
from mysql.connector import MySQLConnection,Error,errorcode
import datetime

DEFAULT_FOLDER_COLOR =  "#888888"

CREATE_COMMAND_TASKS = "CREATE TABLE Tasks(task_id INT AUTO_INCREMENT PRIMARY KEY,\
        msg varchar(100),\
        priority INT DEFAULT(5) CHECK(priority<=10 AND priority>=1),\
        dt DATETIME,\
        Folder VARCHAR(30),\
        FOREIGN KEY(Folder) REFERENCES Folders(folder_name) ON DELETE CASCADE ON UPDATE CASCADE)" #Current schema of the Tasks table
    
CREATE_COMMAND_FOLDERS= f"CREATE TABLE Folders(Folder_name VARCHAR(30) PRIMARY KEY,\
    color CHAR(7) DEFAULT('{DEFAULT_FOLDER_COLOR}'))"

class Tasks:   

    def __init__(self,conn:MySQLConnection):
        self.conn = conn
        tables = self.getTables()
        if 'folders' not in tables: #Since Folders is the parent table, it has to be created first.
            with conn.cursor() as cur:
                cur.execute(CREATE_COMMAND_FOLDERS)
            conn.commit()

        if 'tasks' not in tables:
            with conn.cursor() as cur:
                cur.execute(CREATE_COMMAND_TASKS)
            conn.commit()        
            
    
    def checkConnection(func):
        #checks if the connection has terminated, and can be used to handle that exception,
        # along with  any other common exceptions that are to be handled by more than 1 function
        def wrapper(self,*args,**kwargs):
            if not self.conn.is_connected():
                raise ConnectionError("CONNECTION NO LONGER EXISTS")
            func(self,*args,**kwargs)
        return wrapper
    
    def getTables(self):#returns a list of all tables in the database
        x = []
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT table_name FROM information_schema.tables\
                        WHERE table_schema='{self.conn.database}'") #queries all the tables from database
            for i in cur.fetchall():
                x.append(i[0])
                print(i)
        
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

    def addTask(self, msg:str ,priority:int = 5, dt:datetime.datetime='', folder:str=''):
        if folder:folder = f'"{folder}"' #annoyingly enough mysql needs quotes around string
        else:folder = "NULL"             #but quotes around "NULL" immediately makes it a string of "NULL", so this
        if dt!='':dt = f'"{str(dt)}"' #same issue
        else: dt = 'NULL'
        self.execute(f"INSERT INTO Tasks(msg,priority,dt,folder) VALUES\
                    ('{msg}',{priority},{str(dt)},{folder})")    
        self.conn.commit()

    def delTask(self, task_id:int):
        self.execute(f"DELETE FROM Tasks WHERE task_id={task_id}")
        self.conn.commit()
    
    def updateTask(self,  task_id:int, msg:str ,priority:int = 5, dt:datetime.datetime='NULL'):
        self.execute(f"UPDATE Tasks SET msg='{msg}',priority={priority},dt={dt} WHERE task_id={task_id}")
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
    


