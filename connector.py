import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="credentials"
)

mycursor = mydb.cursor()

sql = "INSERT INTO login_credentials (, address) VALUES (%s, %s)"



value = ("first", "blabla")
mycursor.execute(sql,value)

mydb.commit()

print(mycursor.rowcount, "record inserted.")