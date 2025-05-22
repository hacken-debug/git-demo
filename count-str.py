string=input("please input a string")
char=0
number=0
space=0
other=0
for i in string:
    if i.isalpha():
        char+=1
    elif i.isdigit():
        number+=1
    elif i.isspace():
        space+=1
    else:
        other+=1
print(f"the English word have{char},the number have{number},the space have{space},the other have{other}")