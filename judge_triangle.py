a=int(input("please enter a edge: "))
b=int(input("please enter a edge: "))
c=int(input("please enter a edge: "))
if a+b>c and a+c>b and b+c>a:
    print("this is a triangle")
else:
    print("this is not a triangle")