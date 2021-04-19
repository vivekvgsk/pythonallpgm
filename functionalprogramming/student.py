class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
s1=Student(101,"vivek","BCA",100)
s2=Student(102,"vinayak","BCA",98)
s3=Student(103,"sijoy","BCA",85)

studentlist=[]
studentlist.append(s1)
studentlist.append(s2)
studentlist.append(s3)
studenttotal=list(map(lambda stud:stud.total,studentlist))
print(studenttotal)
print(max(studenttotal))
# stud=list(filter(lambda stud:stud.course=="BCA",studentlist))
# for course in stud:
#     print(course)