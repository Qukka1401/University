import rounds as s
def start() -> None:
    while True:
        command = int(input('1 - Начать игру, 2 - Выход \n'))
        if command == 1:
            s.start_game()
            print('Хотите сыграть еще?')
        elif command == 2:
            break