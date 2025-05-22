n=100
count_rebound=0
list=[]
while count_rebound<10:
    if count_rebound==0:
        list.append(n)
        n=n/2
        count_rebound+=1
    else:
        list.append(2*n)
        n=n/2
        count_rebound+=1
print(list)
print(sum(list))