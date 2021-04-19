employees={
    1000:{"name":"vivek","desig":"developer","exp":2},
    1001:{"name":"vinayak","desig":"bigdata","exp":3},
    1002:{"name":"sijoy","desig":"developer","exp":2}
}
def emp_details(**kwargs):
    id=kwargs["eid"]
    prop=kwargs["prop"]
    if(id in employees):
        print(employees[id]["name"])
        print(employees[id][prop])
    else:
        print("employee id does not exist")
emp_details(eid=1000,prop="desig")

