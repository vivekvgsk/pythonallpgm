from functools import reduce
lst=[10,20,30,50,80,5]
high=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(high)
min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(min)