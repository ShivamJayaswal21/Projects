print('!!!! MENUE !!!!')
print('1.Addition\
        \n2.Sutraction\
        \n3.Multiplication\
        \n4.dividation\
        \n5.power\
        \n0.exist ')
while True :
    choice=int(input('enter the choice='))
    if choice==0:
        break
    if choice <= 5:
        x=eval(input('enter the first number='))
        y=eval(input('enter the second number='))
        
        if choice==1:
            print(f'addition{x+y}')
        elif choice==2:
            print(f'subrraction{x-y}')
        elif choice==3:
            print(f'multiplication{x*y}')
        elif choice==4:
            print(f'dividation{x/y}')
        else:
            print(f'power{x**y}')
    else:
            print('invalid choice')
    choice=input('continue?(y/n)')
    if choice=='n':
            break
        
