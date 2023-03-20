import mysql.connector
apt=mysql.connector.connect(host="localhost",username="root",passwd="Murmi@2000")
mycursor=apt.cursor()
# execute is predefined module
mycursor.execute("show databases")
for i in mycursor:
 print("Hello world",i)