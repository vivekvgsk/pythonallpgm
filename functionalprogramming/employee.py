employees={
    1000:{"name":"vivek","desig":"developer","exp":2},
    1001:{"name":"vinayak","desig":"bigdata","exp":3},
    1002:{"name":"sijoy","desig":"developer","exp":2}
}
eid=int(input("enter employee id"))

if(eid in employees):
    print(employees[eid]["name"])

else:
    print("employee id does not exist")