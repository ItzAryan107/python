import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="balaji@25101007",
    database="ice_cream"
)
print(connection.is_connected())
myCursor = connection.cursor()

# inserting many data at a time, using list
ice_creams = [("Buttered Pecan", 65),
              ("Chocolate Chip", 75),
              ("Birthday Cake", 87),
              ("Strawberry", 55)]

for i in ice_creams:
    myCursor.execute("insert into costlist values('%s', %s);" % i)
    connection.commit()


