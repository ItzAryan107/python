import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="balaji@25101007"
)

myCursor = connection.cursor()


def createDatabase():
    """creating database ice_cream"""
    try:
        myCursor.execute("create database ice_cream;")
    except Exception as e:
        return


def showDatabases():
    try:
        myCursor.execute("show databases;")
        for database in myCursor:
            print(database)

    except Exception as e:
        return


createDatabase()  # we wont we using this line, as we have already created the given database
showDatabases()

