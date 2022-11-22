import mysql.connector

# now we have connected our python to database
connection = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="***************")

print(connection)
