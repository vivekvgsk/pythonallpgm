class Employee:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def print_emp(self):
        print(self.ename)
f=open("emp")
employees=[]
for lines in f:
    eid,ename,desig,sal=lines.rstrip("\n").split(",")
    e1=Employee(eid,ename,desig,sal)
    employees.append(e1)
salary=[]
for emp in employees:
    salary.append(emp.salary)
print(salary)
highsal=max(salary)

if (emp.salary==highsal):
    print(emp.eid,":",emp.ename,":",emp.desig,":",emp.salary)