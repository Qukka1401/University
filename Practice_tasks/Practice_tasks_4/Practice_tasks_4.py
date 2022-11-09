
def read_file():
    word_list = open('data.txt', mode='r', encoding= 'utf-8')
    s = word_list.read().lower()
    a = 'йцукенгшщзхъфывапролджэячсмитьбюё'
    for i in range(len(s)):
        if not (s[i] in a):
            s = s.replace(s[i], ' ')
    return word_list
print(read_file())