import os
from docx2pdf import convert
from pdf2docx import parse
from PIL import Image


def directory() -> str:
    return os.getcwd()

def file_list(*args: str) -> list:
    file: list = []
    files: list = []
    for filename in os.listdir(directory()):
        if filename.endswith(args):
            file.append(filename)
    for filename in enumerate(file, start=1):
        files.append(filename)
    return files

def choice() -> int:
    choice: list = ['1. Удалить все файлы начинающиеся на определенную подстроку',
                    '2. Удалить все файлы заканчивающиеся на определенную подстроку',
                    '3. Удалить все файлы содержащую на определенную подстроку',
                    '4. Удалить все файлы по расширению',
                    '5. Удалить определенный файл' '\n'
                    ]
    list_com = range(1, 6)
    print("Выберите действие:\n", *choice, sep='\n')
    a: int = int(input('Ваш выбор: '))
    while a not in list_com:
        a = int(input())
    return a

def change_directory() -> str:
    path: str = input('Введите путь: ')
    while path == '':
        path = input('Введите путь: ')
    os.chdir(path)
    return '\nРабочий каталог успешно изменён!\n'

def D2P() -> str:
    for k in file_list('docx', 'DOCX', 'doc'):
        print(*k)
    inp: int = int(input('Выберите файл: '))
    if inp != 0:
        for k in file_list('docx'):
            if k[0] == inp:
                convert(k[1])
                return 'Файл успешно конвертирован!'

def P2D() -> str:
    print('Список pdf файлов в этом каталоге: \n')
    for k in file_list('pdf'):
        print(*k)
    inp: int = int(input('Выберите файл: '))
    if inp != 0:
        for k in file_list('pdf'):
            if k[0] == inp:
                parse(k[1])
                return '\nФайл успешно конвертирован! \n'


def delite_file() -> None:
    for k in file_list(''):
        print(*k)


def del_first() -> str:
    delite_file()
    podstroka: str = input('Введите подстроку: ')
    for k in file_list(''):
        if k[1].startswith(podstroka):
            os.remove(k[1])
    return '\nФайл(ы) успешно удален(ы)!\n'


def del_last() -> str:
    delite_file()
    podstroka: str = input('Введите подстроку: ')
    for k in os.listdir(os.getcwd()):
        if k.split('.')[0].endswith(podstroka):
            os.remove(rf'{os.getcwd()}\{k}')
    return '\nФайл(ы) успешно удален(ы)!\n'


def del_second() -> str:
    delite_file()
    podstroka: str = input('Введите подстроку: ')
    for k in file_list(''):
        if podstroka in k[1]:
            os.remove(k[1])
    return '\nФайл(ы) успешно удален(ы)!\n'

def del_extension() -> str:
    delite_file()
    extension: str = input('Введите расширение: ')
    if extension != '0':
        for k in file_list(''):
            if k[1].endswith(extension):
                os.remove(k[1])
        return '\nФайл(ы) успешно удален(ы)!\n'

def del_file() -> str:
    delite_file()
    f: int = int(input('Выберите файл: '))
    if f != 0:
        for k in file_list(''):
            if k[0] == f:
                os.remove(k[1])
        return '\nФайл успешно удалён!\n'

def menu_delite_file() -> None:
    fc = choice()
    if fc == 1:
        print(del_first())
    if fc == 2:
        print(del_last())
    if fc == 3:
        print(del_second())
    if fc == 4:
        print(del_extension())
    if fc == 5:
        print(del_file())

def photo() -> str:
    for k in file_list('png', 'jpg', 'jpeg', 'gif'):
        print(*k)
    p: int = int(input('Выберите фотографию/гифку: '))
    if p != 0:
        quality = int(input('Выберите уровень сжатия изображения (0%-100% (0% - самое сильно сжатие)): '))
        for k in file_list('png', 'jpg', 'jpeg', 'gif'):
            if k[0] == p:
                Image.open(k[1]).save(k[1], quality=quality)
                return 'Фотография/гифка успешно сжата!'