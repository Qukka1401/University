def f():
    try:
        a=int(input())
        b=int(input())
        return a / b
    except ValueError:
        return "Ошибка исходных данных!"
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    except:
        return "Произошло фатальная ошибка!"
    else:
        return "Ошибок нет!"
    finally:
        print("ВЫВОД ВСЕГДА!")
    return "Ты ошибся"
print(f())