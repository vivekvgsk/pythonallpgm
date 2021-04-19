lst=[4,2,1,6,7,8] #output 3,1,0,7,8,9


result=list(map(lambda num:num-1 if num<5 else num+1,lst))
print(result)

# if num<5:
#     num-1
# else:
#     num+1