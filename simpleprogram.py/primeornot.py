num = int(input("Enter a number"))
flag = 0
if(num>1):
 for i in range (2,num):
    if(num%i==0):
     flag = 1
    break
if flag == 1:
    print(num,"Is not a prime number")
else:
    print(num,"Is a prime number") 

