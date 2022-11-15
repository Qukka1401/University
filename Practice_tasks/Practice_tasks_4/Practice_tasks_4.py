def read_file(filename):
    ss = {}
    with open(filename, encoding='UTF-8', mode='r') as f:
        s = (f.read().split(' '))
    for i in range(0, len(s)):
        s[i] = s[i].lower()
        s[i] = "".join(j for j in s[i] if j.isalpha())
    ss = set(s)
    return list(ss)

def save_file(filename, s):
    s = sorted(s)
    with open(filename, encoding='utf-8', mode='w') as f:
        f.write(f'Количество уникальных слов: ' + str(len(s)))
        f.write("\n=====================\n")
        f.write('\n'.join(s))

