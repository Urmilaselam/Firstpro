import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",passwd="Murmi@2000",database="organization")
cursor=mydb.cursor()
query= "update emp set address= 'mangalore' where id=12"
cursor.execute(query)
mydb.commit()
rows=cursor.fetchall()
print("ID \tname \taddress \tsalary")
print(cursor.rowcount, "record(s) updated")
# for row in rows:
    # print(row[0], "\t", row[1], "\t", row[2], row[3])