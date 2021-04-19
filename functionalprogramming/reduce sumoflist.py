from functools import reduce
lst=[10,20,30,50,80]
total=reduce(lambda no1,no2:no1+no2,lst)
print(total)