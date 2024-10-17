import mysql.connector as con
try:
    a = con.connect(user='root', host='localhost', password='3553a7')
    print("Connected successfully!")
except con.Error as err:
    print(f"Error: {err}")