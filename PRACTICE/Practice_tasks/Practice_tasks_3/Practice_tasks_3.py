from defs import *
import random

r = 0

def game():
    global r
    kw = "\u25A0"
    word = random.choice(words("words.txt"))
    word1 = ' '.join(word).split()
    word = ''.join(word)
    while True:
        slives = input('Выберите уровень сложности:\n1 - Новичок (7 жизней)\n2 - Любитель (5 жизней)\n3 - Мастер (3 жизни)\n')
        if slives == '1':
            lives = 7
        if slives == '2':
            lives = 5
        if slives == '3':
            lives = 3
        break

    lenw = len(word)
    for i in range(lenw):
        word1[i] = kw
    kws = " ".join(word1)

    while lives > 0:
        print(f"{kws} | Кол-во жизней: {lives}")
        letter = input('Введи слово или букву: ')
        if letter == word:
            print('Вы выиграли! Ура')
            r += 1
            break
        if len(letter) > 1:
            print('Неверный ответ(')
            lives -= 1
        elif letter in word:
            for let in range(lenw):
                if word[let] == letter:
                    kws = kws.split(" ")
                    kws[let] = letter
                    kws = " ".join(kws)
        else:
            print('Такой буквы нет!')
            lives -= 1
        if kw not in kws:
            print('Вы выиграли! Ура')
            r += 1
            break
    if lives == 0:
        print(f"Вы проиграли!\nСлово: {word}")

while True:
    hg = ""
    regame = input(f'Хотите сыграть в игру {hg}?\n')
    if regame == 'да':
        game()
        record(r)
        hg = 'еще раз'
    if regame == 'нет':
        break