import mysql.connector
import datetime
from dbclass import db

def mysqlop(db_parameters,command):
    try:
        db = mysql.connector.connect(host = db_parameters[0], user = db_parameters[1], passwd = db_parameters[2], database = db_parameters[3], charset = db_parameters[4])
        print("Connected to the database")
    except:
        print("Cannot connect to the database")
        exit()
    dbcursor = db.cursor()
    try: 
        dbcursor.execute(command)
    except:
        db.clsoe()
        print(str(datetime.datetime.now()) + ": FAILD: " + command)
        exit()
    print(str(datetime.datetime.now()) + ": EXCECUTED: " + command)
    try:
        dbresult = dbcursor.fetchall()
    except:
        dbresult = ""
    db.close()
    return dbresult


#Example code

db1 = db()
db1.ip = "x.x.x.x"
db1.username = "username"
db1.password = "password"
db1.dbname = "database name"

db_para_list = db1.dbpara()

sql_command = "select * from TABLE_NAME"

output = mysqlop(db_para_list,sql_command)

print(output)

