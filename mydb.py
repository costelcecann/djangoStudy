import mysql.connector

dataBase = mysql.connector.connect(

host = 'localhost',
user = 'root',
password = 'password'

)


# prepare a curosr object

cursorObject = dataBase.cursor()

# Create a database 

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
