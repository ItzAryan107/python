import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="***************",
    database="ice_cream"
)
myCursor = connection.cursor()

sqlQuery = "update costlist set Cost=65 where Name='Black Current';"
myCursor.execute(sqlQuery)
connection.commit()  # to update anything to the database commit is necessary

# limit keyword gives the first n data of the table
myCursor.execute("select * from costlist limit 5")
myResult = myCursor.fetchall()

for i in myResult:
    print(i)

print()

# let you want to start from a particular place, from there you want to print 5 data down
myCursor.execute("select * from costlist limit 5 offset 4")
myResult = myCursor.fetchall()

for i in myResult:
    print(i)

