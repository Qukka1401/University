# def hst():
#     str = input()
#     str = str.title().split()
#     if not(len(str) >= 140 or len(str) == 0):
#         print('#' + ''.join(str))
#     else:
#         print(False)
# hst()

import os
catalog = os.getcwd()
ans = input(f'Текущий каталог:{catalog}\nСменить каталог ?\n')
if ans == 'да':
    ans = input('Укажите путь к : ')
    if os.path.exists(ans) == True:
        os.chdir(ans)
        catalog = os.getcwd()
        print(f'Текущий каталог:{catalog}')
    else:
        print('Такого каталога нет')
if ans == 'Нет':
    print('Каталог не сменился')

l_f = os.listdir(catalog)
count = 0
for file in l_f:
    couyjnt = count + 1
    print(f'{count}. {file}')

ans =input('Введите паттерн: ')
ans2 =input('Введите расширение(С точкой): ')
W = ''
k = 0
for f in l_f:
    if ans2 in f:
        ws=[]
        for b in f:
            if b!='.':
                ws.append(b)
            if b=='.':
                break
        ws=''.join(ws)
        f2 = f.replace(ws, f'{ans}{W}')
        os.rename(fr'{catalog}\{f}', fr'{catalog}\{f2}')
        k = k+1
        W = f'_{k}'