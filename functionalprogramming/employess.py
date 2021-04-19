class Employee:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def print_emp(self):
        print(self.ename)
e1=Employee(100,"vivek","developer",25000)
e2=Employee(101,"vinayak","developer",24000)
e3=Employee(102,"sijoy","qa",27000)
e4=Employee(103,"ashik","mrkt",28000)
employees=[]
employees.append(e1)
employees.append(e2)
employees.append(e3)
employees.append(e4)
# sal=[]
# for emp in employees:
#     sal.append(emp.salary)
# print(sal)
salary=list(map(lambda emp:emp.salary,employees))
print(salary)
