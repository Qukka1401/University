def s(filename):
    try:
        f = open(filename)
        chisla = int(f.readline())
        return [int(a) for a in [f.readline() for _ in range(chisla)]]
    except ValueError:
        return 'Неверные значения'
    except FileNotFoundError:
        return 'Неправильное имя файла'
    except:
        return 'Неизвестная ошибка'
filename = input('Введите имя файла: ')
s(filename)