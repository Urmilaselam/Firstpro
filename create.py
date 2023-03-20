import mysql.connector
apt=mysql.connector.connect(host="localhost",username="root",password="Murmi@2000",database="organization")
mycursor=apt.cursor()
# mycursor.execute("CREATE database organization")
mycursor.execute("create table sal(id int primary key, salary varchar(255), phno varchar(255)")

print("success")