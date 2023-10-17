from main import Coord
from random import randint
from my_exceptions import OutBoardError


class Player:
    def __init__(self, board, enemy):
        self.__board = board
        self.__enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.__enemy.shot(target)
                return repeat
            except OutBoardError as e:
                print(e)

    @property
    def board(self):
        return self.__board


class Computer(Player):
    def ask(self):
        comp_coord = Coord(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {comp_coord.x_coord + 1} {comp_coord.y_coord + 1}")
        return comp_coord


class User(Player):

    def __init__(self, board, enemy):
        super().__init__(board, enemy)
        self.__name = 'User'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, _name):
        self.__name = _name

    def ask(self):
        while True:
            coords = input("Ваш ход: ").split()

            if len(coords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x_coord, y_coord = coords

            if not (x_coord.isdigit()) or not (y_coord.isdigit()):
                print(" Введите числа! ")
                continue

            x_coord, y_coord = int(x_coord), int(y_coord)

            return Coord(x_coord - 1, y_coord - 1)
