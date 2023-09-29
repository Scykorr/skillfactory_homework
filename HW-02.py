def gen_playing_field() -> list:
    """
    Функция генерации чистого игрового поля
    :return: field список ячеек игрового поля с исходным значением '-'
    :rtype: list
    """
    field = [['-' for _ in range(3)] for _ in range(3)]
    return field


def print_playing_field(field) -> None:
    """
    Функция вывода игрового поля в консоль
    :param field:(list) список ячеек игрового поля
    :return: None
    """
    print(' ', 0, 1, 2)
    for num in range(3):
        print(num, *field[num])


def play_game(field) -> None:
    """
    Функция, описывающая общий процесс игры
    :param field:(list) список ячеек игрового поля
    :return: None
    """
    print('Начало игры!')
    print_playing_field(field)
    for step in range(1, 10):
        if step % 2 == 0:
            step_player(field, player_num='2', player_sign='o')
        else:
            step_player(field, player_num='1', player_sign='x')
        print_playing_field(field)
        check_win(field, step)


def step_player(field, player_num, player_sign) -> None:
    """
    Функция, описывающая шаг соответствующего игрока
    :param player_num:(str) номер игрока
    :param player_sign:(str) знак игрока
    :param field:(list) список ячеек игрового поля
    :return: None
    """
    print('Ход {name}ого игрока'.format(
        name=player_num,
    ))
    while True:
        inp_coord_y, inp_coord_x = map(int, input('Введите через пробел координаты: ').split())
        if not ((0 <= inp_coord_x <= 2) or (0 <= inp_coord_y <= 2)):
            print('Ошибка! Введите верные координаты!')
            continue
        elif field[inp_coord_y][inp_coord_x] == '-':
            field[inp_coord_y][inp_coord_x] = player_sign
            break
        else:
            print('Ошибка! Данная ячейка уже занята!')


def check_win(field, curr_step) -> None:
    """
    Функция проверки выигрыша
    :param curr_step: текущий шаг
    :param field:(list) список ячеек игрового поля
    :return: None
    """
    win_state = [{field[0][0], field[0][1], field[0][2]},
                 {field[1][0], field[1][1], field[1][2]},
                 {field[2][0], field[2][1], field[2][2]},
                 {field[0][0], field[1][0], field[2][0]},
                 {field[0][1], field[1][1], field[2][1]},
                 {field[0][2], field[1][2], field[2][2]},
                 {field[0][0], field[1][1], field[2][2]},
                 {field[0][2], field[1][1], field[2][0]}]
    result = list(map(len, win_state))
    for index, el in enumerate(result):
        if el == 1 and list(win_state[index])[0] != '-':
            winner_sign = list(win_state[index])[0]
            if winner_sign == 'x':
                print('Поздравляем первого игрока с победой!')
            else:
                print('Поздравляем второго игрока с победой!')
            start_game()
        elif curr_step == 9:
            print('Ничья!')
            start_game()


def start_game() -> None:
    """
    Функция начала новой игры
    :return: None
    """
    while True:
        inp_message = input('Хотите начать новую игру?(Y/N): ').lower()
        if inp_message == 'y':
            game_field = gen_playing_field()
            play_game(game_field)
        elif inp_message == 'n':
            exit()
        else:
            print('Введите корректное значение!')


if __name__ == '__main__':
    start_game()