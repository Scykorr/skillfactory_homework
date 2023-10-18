"""
Модуль, содержащий основные классы для формирования игры
"""

from my_exceptions import OutBoardError, BoardWrongShipException, CellRepeatError


class Coord:
    """
    Класс, описывающий координату на игровом поле

    ...

    Attributes
    ----------
        __x_coord : int
            координата х
        __y_coord : int
            координата у
    Methods
    -------
        ask(self) -> None:
            Метод, возвращающий исключение NotImplementedError
        move(self) -> bool:
            Метод, отвечающий за попадание игрока в клетку.
        board(self) -> GameBoard:
            Геттер объекта "игровое поле" игрока.

    """

    def __init__(self, x_coord, y_coord):

        self.__x_coord = x_coord
        self.__y_coord = y_coord

    @property
    def x_coord(self):
        return self.__x_coord

    @property
    def y_coord(self):
        return self.__y_coord

    def __eq__(self, other):
        return self.__x_coord == other.x_coord and self.__y_coord == other.y_coord

    def __str__(self):
        return f"({self.__x_coord}, {self.__y_coord})"


class Ship:

    def __init__(self, first_ship_part, ship_length, direction):
        self.__first_ship_part = first_ship_part
        self.__ship_length = ship_length
        self.__direct = direction
        self.__lives = ship_length

    @property
    def dots(self):
        ship_dots = []
        for num in range(self.__ship_length):
            cur_x = self.__first_ship_part.x_coord
            cur_y = self.__first_ship_part.y_coord

            if self.__direct == 0:
                cur_x += num

            elif self.__direct == 1:
                cur_y += num

            ship_dots.append(Coord(cur_x, cur_y))

        return ship_dots

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, lives):
        self.__lives = lives


class GameBoard:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid

        self.count = 0

        self.field = [["O"] * size for _ in range(size)]

        self.busy = []
        self.ships = []

    def add_ship(self, ship):

        for dot in ship.dots:
            if self.out(dot) or dot in self.busy:
                raise BoardWrongShipException()
        for dot in ship.dots:
            self.field[dot.x_coord][dot.y_coord] = "■"
            self.busy.append(dot)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for dot in ship.dots:
            for dx, dy in near:
                cur_coord = Coord(dot.x_coord + dx, dot.y_coord + dy)
                if not (self.out(cur_coord)) and cur_coord not in self.busy:
                    if verb:
                        self.field[cur_coord.x_coord][cur_coord.y_coord] = "."
                    self.busy.append(cur_coord)

    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res

    def out(self, cur_coord):
        return not ((0 <= cur_coord.x_coord < self.size) and (0 <= cur_coord.y_coord < self.size))

    def shot(self, dot):
        if self.out(dot):
            raise OutBoardError()

        if dot in self.busy:
            raise CellRepeatError()

        self.busy.append(dot)

        for ship in self.ships:
            if dot in ship.dots:
                ship.lives -= 1
                self.field[dot.x_coord][dot.y_coord] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[dot.x_coord][dot.y_coord] = "T"
        print("Мимо!")
        return False

    def begin(self):
        self.busy = []
