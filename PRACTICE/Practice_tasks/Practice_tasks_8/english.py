import pymorphy2
import translate


def learn_english(name, name2):
    with open(name, "r", encoding='utf-8') as file:
        tekst = file.read().split()
        newfile(name2, sort(redactor(tekst)))


def redactor(list):
    for i in range(len(list)):
        letter = [a for a in list[i] if a.isalpha()]
        word = "".join(letter)
        list[i] = infin(word)
    return list


def infin(word):
    norm = pymorphy2.MorphAnalyzer()
    return norm.parse(word)[0].normal_form


def sort(words):
    wdict = {}
    for word in words:
        wdict[word] = str(words.count(word))
    if '' in wdict:
        wdict.pop('')
    dict = sorted(wdict.values(), reverse=True)
    sotrdict = {}
    for i in dict:
        for k in wdict.keys():
            if wdict[k] == i:
                sotrdict[k] = wdict[k]
    return sotrdict


def newfile(name, count):
    translat = translate.Translator(from_lang='ru', to_lang='en')

    with open(name, 'w', encoding='utf-8') as file:
        for word in count:
            file.write(f'{word} | {translat.translate(word)} | {count[word]}\n')


learn_english('text.txt', 'translate.txt')