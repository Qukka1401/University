is_difficult: bool = False
lifes: int = 0

def by_difficult() -> int:
    difficult: int = int(input('Выберите сложность: 1 - Легкая, 2 - Средняя, 3 - Сложная '))
    if difficult == 1:
        return 7
    elif difficult == 2:
        return 5
    elif difficult == 3:
        return 3
    else:
        print('Неверная сложность')
        return by_difficult()