list=[1,2,3,4]
list1=[1,2,3,4]
print(list1)
list1=list
list[0]=30
print(list1)
import copy
list3=[1,2,3,4]
list4=copy.copy(list3)
print(list4)