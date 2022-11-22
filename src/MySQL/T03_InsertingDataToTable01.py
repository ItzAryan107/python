import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="***************",
    database="ice_cream"  # here already selecting the database, so in future no need to
    # type the command 'use ice_cream'
)

# to know, whether python is connected to mysql or not
print(connection.is_connected())
myCursor = connection.cursor()


def insert(n):
    """Inserting data to table

    old way to insert data to table
    myCursor.execute("insert into costlist values('%s',%s);"%(name, cost))

    new way to insert data to table
    myCursor.execute("insert into costlist values('{}',{});" .format(name, cost))
    """
    if n == 0:
        return

    name = input("Enter ice_cream name ---> ")
    cost = int(input("Enter cost of {} ---> ".format(name)))

    # new way to insert data to table
    myCursor.execute("insert into costlist values('{}',{});" .format(name, cost))
    connection.commit()  # to show a change in database, it's very necessary to commit
    n = n - 1
    insert(n)


def showData():
    """Will show all the data, on console, present in table"""
    try:
        myCursor.execute("select * from costlist;")
        for i in myCursor:
            print(i)
    except Exception as a:
        return


n = int(input("Enter number of data you want to save ---> "))
insert(n)
showData()
# print(insert.__doc__)
# print(showData.__doc__)

