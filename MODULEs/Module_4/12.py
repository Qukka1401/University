a = int(input('Введите календарный месяц '))
b = int(input('Введите день месяца '))
if b>=31:
    a += 1
    b = 1
    print(f'{b}-{a}-2022')
elif (a==2) and b>=28:
    a += 1
    b = 1
    print(f'{b}-{a}-2022')
else:
    print(f'{b+1}-{a}-2022')