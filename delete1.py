import mysql.connector
apt=mysql.connector.connect(host="localhost",username="root",password="Murmi@2000",database="organization")
query= "DELETE from emp where id=%s"
value= (13)
cursor=apt.cursor()

cursor.execute(query,value)
apt.commit()
print(cursor.rowcount, "row(s) deleted successfully")