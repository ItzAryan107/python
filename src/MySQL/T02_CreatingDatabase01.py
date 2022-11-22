import mysql.connector

# making connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="balaji@25101007"
)


# now we have to create cursor, which actually communicate mysql server
myCursor = connection.cursor()

"""
creating database
myCursor.execute("create database ice_cream")
myCursor.execute("show databases")
myCursor.execute("create database ice_cream")  # this line will give error, bcz ice_cream database already exist
"""


# try to create database in try-except block, like if that particular database exist then it will not show error
try:
    myCursor.execute("create database mysql")
except Exception as alreadyThere:
    myCursor.execute("show databases")
    for cursor in myCursor:
        print(cursor)
