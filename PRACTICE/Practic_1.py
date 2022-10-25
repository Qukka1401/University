import random

vin1 = 0
vin2 = 0
for i in range (0,10000):
    a = [0,1,0]
    o = random.choice(a)
    a.remove(o)
    a.remove(0)
    if o == 1:
        vin1 +=1
    elif a[0] == 1:
        vin2 += 1

print(f'Процент выигрыша при первоначальном выборе: {vin1//100}, Процент выигрыша при изменении выбора {vin2//100}')


