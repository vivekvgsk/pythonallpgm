import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="student_data",
    auth_plugin="mysql_native_password"
)
cursor = db.cursor()
# sql = "create table student (roll_no int,name varchar(50),course varchar(25),mark int)"
# cursor.execute(sql)
# cursor.execute(sql2)
# data = cursor.fetchone()
#  print(data)
# db.close()
#sql="insert into student(roll_no,name,course,mark) values (101,'vinayak','BCA',95)"
sql="update student set mark=100 where roll_no=100"
try:
    cursor.execute(sql)
    db.commit()#it is used in insertion and updation query
except Exception as e:
    print(e.args)
    db.rollback()
finally:
    db.close