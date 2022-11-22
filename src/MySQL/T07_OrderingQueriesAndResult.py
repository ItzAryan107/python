import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="***************",
    database="ice_cream"
)
myCursor = connection.cursor()

# if you want to get the data in order
myCursor.execute("select * from costlist order by Cost")  # you can also try with order by Name
myResult = myCursor.fetchall()

for i in myResult:
    print(i)

print()

myCursor.execute("select * from costlist order by Cost desc")  # if we have to get Cost in descending order
myResult = myCursor.fetchall()
for i in myResult:
    print(i)

