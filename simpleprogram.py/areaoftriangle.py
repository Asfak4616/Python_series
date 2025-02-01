import math
a  = float(input("Enter the first number :"))
b  = float(input("Enter the second number :"))
c  = float(input("Enter the third number :"))
s =(a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print('\n Area of the triangle is :',area)
