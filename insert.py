import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",passwd="Murmi@2000",database="organization")
# mydb=mysql.connector.connect(
    # host="3306"
    # user="root"
    # password="Murmi@2000"
    # database="organization"
# )
cursor=mydb.cursor()
query="insert into emp (id,name,address,salary)values(%s,%s,%s,%s)"
values= [
    (11, "raj", "bangalore", 3000),
    (12, "manu", "btm2", 13000),
    (13, "urmi", "btm", 23000)
]
cursor.executemany(query,values)
mydb.commit()
print(cursor.rowcount, "row(s) inserted")