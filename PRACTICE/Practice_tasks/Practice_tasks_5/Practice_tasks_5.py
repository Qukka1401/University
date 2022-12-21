def s(filename):
    try:
        f = None
        f = open(filename, encoding='utf-8')
        chisla = f.read().splitlines()
        chisla = [int(a) for a in chisla]

        if chisla[0] != len(chisla[1:]):
            raise KeyError
        return chisla[1:]

    except KeyError:
        return 'Количество чисел не соответсвует первому числу'
    except ValueError: #Неправильный тип
        return 'Неверные значения'
    except FileNotFoundError: #Файла не существует, ошибка в имени
        return 'Неправильное имя файла'
    except IndexError:
        return 'Количество чисел неправильное'
    except:
        return 'Неизвестная ошибка'
    finally:
        if f is not(None):
            f.close()

filename = input('Введите имя файла: ')
print(s(filename))
