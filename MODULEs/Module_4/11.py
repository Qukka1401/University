a = int(input('Введите координату шахматной доски '))
b = int(input('Введите координату шахматной доски '))
c = int(input('Введите координату шахматной доски '))
d = int(input('Введите координату шахматной доски '))
if (a+b+c+d) % 2 == 0:
    print('Да')
else:
    print('Нет')