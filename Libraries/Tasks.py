#untested

from mysql.connector import MySQLConnection,Error,errorcode
import datetime
import mysql.connector as m

CREATE_COMMAND = "CREATE TABLE Tasks(task_id INT AUTO_INCREMENT PRIMARY KEY,\
     msg varchar(100),\
     priority INT DEFAULT=5 CHECK(priority<=10 AND priority>=1),\
     dt DATETIME)" #Current schema of the Tasks table

def exists(conn:MySQLConnection):
    exist = 1
    with conn.cursor() as cur:
        cur.execute(f"SELECT COUNT(*) FROM information_schema.tables\
                    WHERE table_schema='{conn.database}' AND table='Tasks'")
        if not cur.fetchone():
            exist = 0
    return exist

def createTable(conn:MySQLConnection):
    with conn.cursor() as cur:
        cur.execute(CREATE_COMMAND);

def addTask(conn:MySQLConnection ,msg:str ,priority:int = 5 ,date:datetime.datetime='NULL'):
    x = 2 #x number of re-tries
    while x:
        try:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO Tasks(msg,priority,dt) VALUES({msg},{priority},{str(date)})")
            x = 0
        except Error as e:
            x-=1
            if e.errno == errorcode.ER_NO_SUCH_TABLE:
                createTable(conn)
                conn.commit()
            #elif blocks to handle any other exceptions
            else:
                raise e