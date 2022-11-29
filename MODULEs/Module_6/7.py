ls = [int(i) for i in input('Введите числа: ').split()]
v = set()    # Создаем набор
for l in ls:
    if l in v:
        print("ДА")
    else:
        print("НЕТ")
        v.add(l)    # Добавляем l в набор v

print(v)