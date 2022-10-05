def name():
    name = input("Введите имя контакта: ")
    name = name.title()
    name = name.strip()
    return name

def number():
    number = input("Введите номер телефона: ")
    number = number.replace(' ', '')
    number = number.replace('-', '')
    if number[0] == '9' and len(number) == 10:
        number = '+7' + number
    if number[0] == '8' and len(number) == 11:
        number = '+7' + number[1:]
    if number[0] == '7' and len(number) == 11:
        number = '+' + number
    if number[:2] == '+7' and len(number) == 12:
        return number
    else:
        print('Неправильно набран номер!')
        return number()

def contact(dict, name, number):
    dict[name] = number
    print('Контакт добавлен')
    return dict

def sh_contact(dict):
    print("Список контактов:")
    for i in dict:
        print(i, dict[i])

def menu():
    print(f'Выберите действие: \n1. Добавить контанкт \n2. Просмотреть список контактов \n3. Выход')

list = {}

    while True:
        menu()
        p = int(input())
        if p == 1:
            contact(list, name(), number())
        if p == 2:
            sh_contact(list)
        if p == 3:
            print("Спасибо за использование")
            break





