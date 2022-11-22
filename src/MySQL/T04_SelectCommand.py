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

for row in myResult:
    print(row)

print()

myCursor.execute("select * from costlist;")
myResult = myCursor.fetchone()
for i in myResult:
    print(i)

