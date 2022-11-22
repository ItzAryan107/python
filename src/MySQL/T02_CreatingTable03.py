import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="***************",
    database="ice_cream"
)
myCursor = connection.cursor()


def createTable():
    try:
        myCursor.execute("create table costlist(Name varchar(15), Cost int(3));")
    except Exception as e:
        myCursor.execute("describe costlist;")
        print("=============================================")
        for i in myCursor:
            print(i)
        print("=============================================")
        return


createTable()
