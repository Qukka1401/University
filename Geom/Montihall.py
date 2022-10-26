import random

def monti_hall():
    count = 0
    lives = 3
    while lives>0:
        n = random.randint(-10, 10)
        m = random.randint(-10, 10)
        s = n + m
        an = int(input(f'Введите ответ: {n} + {m} = '))
        if an == s:
            print('Правильный ответ!')
            count += 1
        else:
            print(f'Неправильный ответ! Жизней: {lives - 1}')
            lives -= 1
    print(f'Игра окончена! Жизни закончились! Правильно решенных примеров {count}.')
