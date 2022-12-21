'''from CLASS_WORK import Geom

print(Geom.birthday(10000))
print(Geom.montihall(10000))'''
import os
catalog=os.getcwd()
answer=input(f'Текущий каталог:{catalog}\nСменить каталог ?\nНапишите "да" или "нет"\n')
if answer=='да':
    answer= input('Укажите корректный путь к рабочему каталогу: ')
    if os.path.exists(answer) == True:
        os.chdir(answer)
        catalog=os.getcwd()
        print(f'Текущий каталог:{catalog}')
    else:
        print('Такого каталога нет')
if answer=='Нет':
    print('Каталог не изменился')

list_of_files = os.listdir(catalog)
count = 0
for file in list_of_files:
    couyjnt = count + 1
    print(f'{count}. {file}')

answer=input('Введите паттерн: ')
answer2=input('Введите расширение(С точкой): ')
W=''
k=0
for file in list_of_files:
    if answer2 in file:
        ws=[]
        for b in file:
            if b!='.':
                ws.append(b)
            if b=='.':
                break
        ws=''.join(ws)
        #print(ws, 'ws')
        file2=file.replace(ws, f'{answer}{W}')
        #print(file2, 'file2')
        #print(file, 'file')
        os.rename(fr'{catalog}\{file}', fr'{catalog}\{file2}')
        k = k+1
        W = f'_{k}'