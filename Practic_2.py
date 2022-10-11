def get_name():
    name = input("Введите имя контакта: ")
    name = name.title()
    name = name.strip()
    return name


def get_number():
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

def delete_contact(name):
    print(list.pop(name, 'Такого контакта нет'))
    print("Контакт успешно удален")

def ch_contact(name, number):
    if name in list:
        list[name] = number
    else:
        print('Такого контакта нет')

def menu():
    print(f'Выберите действие: \n1. Добавить контанкт \n2. Просмотреть список контактов \n3. Удалить контакт \n4. Изменить номер телефона \n5. Выход')

list = {}

while True:
    menu()
    p = int(input())
    if p == 1:
        contact(list, get_name(), get_number())
    if p == 2:
        sh_contact(list)
    if p == 3:
        delete_contact(list, get_name())
    if p == 4:
        ch_contact(get_name(), get_number())
    if p == 5:
        print("Спасибо за использование")
        break

