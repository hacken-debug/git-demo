import math
a=int(input("enter a number: "))
b=int(input("enter b number: "))
c=int(input("enter c number: "))
if a+b>c and a+c>b and b+c>a:
    p=float(a+b+c)/2
    s=float(p*(p-a)*(p-b)*(p-c))**0.5
    print(s)
else:
    print("this is not a triangle")