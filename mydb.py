import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Aditya@91'
)

# prepare-a-cursor-object

cursorObject = dataBase.cursor()

#create-database

cursorObject.execute("CREATE DATABASE area51")

print("ALL DONE")