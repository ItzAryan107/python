import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="***************",
    database="ice_cream"
)
myCursor = connection.cursor()
myCursor.execute("select * from costlist;")
myResult = myCursor.fetchall()
for i in myResult:
    print(i)

print()

# let we have to delete a data from the table
myCursor.execute("delete from costlist where Name='Buttered Pecan'")  # if table have multiple Buttered Peacan
# it will even delete that
connection.commit()
myCursor.execute("select * from costlist;")
myResult = myCursor.fetchall()
for i in myResult:
    print(i)


# if you are dropping a table, then don't forget to to commit the cursor, as you are updating the
# database, its necessary to commit


