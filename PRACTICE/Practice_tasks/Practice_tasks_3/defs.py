def words(name):
    f = open(name, encoding="UTF-8")
    t = f.read().split(' ')
    f.close()
    return t

def record(r):
    with open('record.txt') as f:
        t = f.read()

    if r > int(t):
        with open('record.txt', "w") as f:
            f.write(str(r))
            print(f"Юху! Ты побил свой рекорд: {r}")
    if r <= int(t):
        print(f"Текущий рекорд: {r}\nВаш рекорд: {t} ")