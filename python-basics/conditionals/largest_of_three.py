a=int(input('enter the number 1 : '))
b=int(input('enter the number 2 : '))
c=int(input('enter the number 3 : '))
if(a>b and a>c):
    print(f'{a} is the greatest number ')
elif(b>a and b>c):
     print(f'{b} is the greatest number ')
elif(c>a and c>b):
     print(f'{c} is the greatest number ')
else:
    print('input is invalid')
