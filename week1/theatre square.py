import math
numbers =  input()
new = numbers.split()
print(new)
m= int(new[0])
n= int(new[1])
a= int(new[2])
ctr = 0
row =math.ceil(m/a)
col = math.ceil(n/a)
ctr= row*col
print(ctr)