import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="balaji@25101007",
    database="ice_cream"
)
myCursor = connection.cursor()

sqlQuery = "select * from costlist where Cost>=65;"
myCursor.execute(sqlQuery)
myResult = myCursor.fetchall()
for i in myResult:
    print(i)

print()

sqlQuery = "select * from costlist where Name like 'B%';"
myCursor.execute(sqlQuery)
myResult = myCursor.fetchall()

for i in myResult:
    print(i)




