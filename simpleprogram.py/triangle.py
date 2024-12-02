import math
a = int(input("Enter the first side number"))
b = int(input("Enter the second side number"))
c = int(input("Enter the third side number"))
s = (a+b+c)/2
print(s)
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)