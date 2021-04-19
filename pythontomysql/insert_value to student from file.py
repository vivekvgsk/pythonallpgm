import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="student_data",
    auth_plugin="mysql_native_password"
)
cursor = db.cursor()
f=open("student")

for lines in f:
    data = lines.rstrip("\n").split(",")
    #print(tuple(data))

    sql="insert into student(roll_no,name,course,mark) values (%s,%s,%s,%s)"
    cursor.execute(sql,tuple(data))
    db.commit()#it is used in insertion and updation query
db.close