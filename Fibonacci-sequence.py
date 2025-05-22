#we should find the n number
#the first way(recursion)
def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))

#the second way(without recursion)
n=6
fibs=[1,1]
for i in range(2,n+1):
    fibs.append(fibs[i-1]+fibs[i-2])
print(fibs)