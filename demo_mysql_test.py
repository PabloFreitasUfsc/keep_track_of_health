# https://www.w3schools.com/python/python_mysql_getstarted.asp
# Get start with MySQL Database

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="pablofreitas",
    password=r"eJTtZ4/^rQ*eTa5",
    database="testdatabase",
)

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute(
# "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
# )

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#     ("Peter", "Lowstreet 4"),
#     ("Amy", "Apple st 652"),
#     ("Hannah", "Mountain 21"),
#     ("Michael", "Valley 345"),
#     ("Sandy", "Ocean blvd 2"),
#     ("Betty", "Green Grass 1"),
#     ("Richard", "Sky st 331"),
#     ("Susan", "One way 98"),
#     ("Vicky", "Yellow Garden 2"),
#     ("Ben", "Park Lane 38"),
#     ("William", "Central st 954"),
#     ("Chuck", "Main Road 989"),
#     ("Viola", "Sideway 1633"),
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)

# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid)

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
