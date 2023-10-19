"""
Модуль, содержащий основные классы для формирования игры
"""

from my_exceptions import OutBoardError, BoardWrongShipException, CellRepeatError


class Coord:
    """
    Класс, описывающий координату на игровом поле.

    ...

    Attributes
    ----------
        __x_coord : int
            координата х
        __y_coord : int
            координата у
    Methods
    -------
        x_coord(self) -> int:
            Геттер координаты х.
        y_coord(self) -> int:
            Геттер координаты y.

    """

    def __init__(self, x_coord: int, y_coord: int) -> None:
        """
        Конструктор класса координаты.

        Parameters
        ----------
            x_coord : int
                координата х
            y_coord : int
                координата y
        Returns
        -------
            None
        """
        self.__x_coord = x_coord
        self.__y_coord = y_coord

    @property
    def x_coord(self) -> int:
        """
        Геттер координаты х.

        Returns
        -------
            __x_coord : int
                координата х
        """
        return self.__x_coord

    @property
    def y_coord(self) -> int:
        """
        Геттер координаты y.

        Returns
        -------
            __y_coord : int
                координата y
        """
        return self.__y_coord

    def __eq__(self, other):
        return self.__x_coord == other.x_coord and self.__y_coord == other.y_coord

    def __str__(self):
        return f"({self.__x_coord}, {self.__y_coord})"


class Ship:
    """
    Класс корабля.

    ...

    Attributes
    ----------
        __first_ship_part : Coord
            координата начала корабля
        __ship_length : int
            длина корабля
        __direct : int
            направление размещения корабля
        __lives : int
            количество жизней корабля

    Methods
    -------
        dots(self) -> list:
            Метод получения координат корабля.
        lives(self) -> int:
            Геттер жизней корабля.
        lives(self, _lives) -> None:
            Сеттер жизней корабля.

    """

    def __init__(self, first_ship_part: Coord, ship_length: int, direction: int) -> None:
        """
        Конструктор класса корабля.

        Parameters
        ----------
            first_ship_part : Coord
            координата начала корабля
            ship_length : int
                длина корабля
            direction : int
                направление размещения корабля
        Returns
        -------
            None
        """
        self.__first_ship_part = first_ship_part
        self.__ship_length = ship_length
        self.__direct = direction
        self.__lives = ship_length

    @property
    def dots(self) -> list:
        """
        Метод получения координат корабля.

        Returns
        -------
            ship_dots : list
                список координат корабля
        """
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
    def lives(self) -> int:
        """
        Геттер жизней корабля.

        Returns
        -------
            __lives : int
                количество жизней корабля
        """
        return self.__lives

    @lives.setter
    def lives(self, _lives) -> None:
        """
        Сеттер жизней корабля.

        Parameters
        ----------
            _lives : int
                количество жизней корабля

        Returns
        -------
            None
        """
        self.__lives = _lives


class GameBoard:
    """
    Класс игрового поля.

    ...

    Attributes
    ----------
        __size : int
            размер игрового поля
        __hid : bool
            флаг поля о наличии корабля
        __count : int
            счетчик уничтоженных кораблей
        field : list
            список, отражающий игровое поле
        busy : list
            список клеток, в которые нельзя поставить корабли
        ships : list
            список клеток с кораблями

    Methods
    -------


    """

    def __init__(self, hid=False, size=6) -> None:
        """
        Конструктор класса игрового поля.

        Parameters
        ----------
            hid : bool
                флаг поля о наличии корабля
            size : int
                размер игрового поля
        Returns
        -------
            None
        """
        self.__size = size
        self.__hid = hid

        self.__count = 0

        self.field = [["O"] * size for _ in range(size)]

        self.busy = []
        self.ships = []

    @property
    def size(self) -> int:
        """
        Геттер размера игрового поля.

        Returns
        -------
            __size : int
                размер игрового поля
        """
        return self.__size

    @size.setter
    def size(self, _size: int) -> None:
        """
        Сеттер размера игрового поля.

        Parameters
        ----------
            _size : int
                размер игрового поля

        Returns
        -------
            None
        """
        self.__size = _size

    @property
    def hid(self) -> bool:
        """
        Геттер флага поля о наличии корабля.

        Returns
        -------
            _hid : bool
                флаг поля о наличии корабля
        """
        return self.__hid

    @hid.setter
    def hid(self, _hid: bool) -> None:
        """
        Сеттер флага поля о наличии корабля.

        Parameters
        ----------
            _hid : bool
                флаг поля о наличии корабля

        Returns
        -------
            None
        """
        self.__hid = _hid

    @property
    def count(self) -> int:
        """
        Геттер счетчика подбитых кораблей.


        Returns
        -------
            __count : int
                счетчик подбитых кораблей
        """
        return self.__count

    @count.setter
    def count(self, _count: int) -> None:
        """
        Сеттер счетчика подбитых кораблей.

        Parameters
        ----------
            _count : bool
                счетчик подбитых кораблей

        Returns
        -------
            None
        """
        self.__count = _count

    def add_ship(self, ship: Ship) -> None:
        """
        Метод добавления корабля на игровое поле.

        Parameters
        ----------
            ship : Ship
                объект класса корабль

        Returns
        -------
            None
        """
        for dot in ship.dots:
            if self.out(dot) or dot in self.busy:
                raise BoardWrongShipException()
        for dot in ship.dots:
            self.field[dot.x_coord][dot.y_coord] = "■"
            self.busy.append(dot)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship: Ship, verb=False) -> None:
        """
        Метод обведения по контуру корабля.

        Parameters
        ----------
            ship : Ship
                объект класса корабль
            verb : bool
                флаг уничтожения корабля
        Returns
        -------
            None
        """
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

        if self.__hid:
            res = res.replace("■", "O")
        return res

    def out(self, cur_coord: Coord) -> bool:
        """
        Метод проверки координаты на попадание за пределы игрового поля.

        Parameters
        ----------
            cur_coord : Coord
                объект проверяемой координаты

        Returns
        -------
             : bool
             флаг выхода за пределы игрового поля
        """
        return not ((0 <= cur_coord.x_coord < self.__size) and (0 <= cur_coord.y_coord < self.__size))

    def shot(self, dot: Coord) -> bool:
        """
        Метод реализующий "выстрел" игрока.

        Parameters
        ----------
            dot : Coord
                координата, в которую происходит выстрел

        Returns
        -------
             : bool
             флаг ранения корабля
        """
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

    def begin(self) -> None:
        """
        Метод, обнуляющий список занятых клеток.

        Returns
        -------
             None
        """
        self.busy = []
