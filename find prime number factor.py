#enter a number
a=int(input("enter the number: "))
#2 is the smallest number factor
y=2
#define a list
list=[]
while a!=y:#assert the a !=2

    if a%y==0:
        list.append(y)
        a=a/y
    else:
        y=y+1
list.append(int(a))
print(list)
for i in list:
    print(i)