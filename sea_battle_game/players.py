"""
Модуль, содержащий классы игроков
"""

from main_elements import Coord, GameBoard
from random import randint
from my_exceptions import OutBoardError, CellRepeatError


class Player:
    """
    Базовый класс игрока

    ...

    Attributes
    ----------
        __board : GameBoard
            собственное игровое поле
        __enemy : GameBoard
            игровое поле соперника

    Methods
    -------
        ask(self) -> None:
            Метод, возвращающий исключение NotImplementedError
        move(self) -> bool:
            Метод, отвечающий за попадание игрока в клетку.
        board(self) -> GameBoard:
            Геттер объекта "игровое поле" игрока.

    """

    def __init__(self, board, enemy) -> None:
        """
        Конструктор базового класса игрока.

        Parameters
        ----------
            board : GameBoard
                собственное игровое поле
            enemy : GameBoard
                игровое поле соперника
        Returns
        -------
            None
        """
        self.__board = board
        self.__enemy = enemy

    def ask(self) -> None:
        """
        Метод, возвращающий исключение NotImplementedError.

        Returns
        -------
            None
        """
        raise NotImplementedError()

    def move(self) -> bool:
        """
        Метод, отвечающий за попадание игрока в клетку.

        Returns
        -------
            repeat : bool
                проверка успешного попадания
        """
        while True:
            try:
                target = self.ask()
                repeat = self.__enemy.shot(target)
                return repeat
            except OutBoardError as e:
                print(e)
            except CellRepeatError as e:
                print(e)

    @property
    def board(self) -> GameBoard:
        """
        Геттер объекта "игровое поле" игрока.

        Returns
        -------
            __board : GameBoard
                объект игрового поля игрока
        """
        return self.__board


class Computer(Player):
    """
    Класс игрока Компьютер. Родитель - Player.

    ...

    Methods
    -------
    ask(self) -> Coord:
        Переопределенный метод, возвращающий объект Coord, отвечающий за координаты игрового поля компьютера.

    """

    def ask(self) -> Coord:
        """
        Переопределенный метод, возвращающий объект Coord, отвечающий за координаты игрового поля компьютера.

        Returns
        -------
            comp_coord : Coord
                объект класса Coord, отвечающий за координаты игрового поля.

        """
        comp_coord = Coord(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {comp_coord.x_coord + 1} {comp_coord.y_coord + 1}")
        return comp_coord


class User(Player):
    """
    Класс игрок-человек. Родитель - Player.

    ...

    Attributes
    ----------
        __name : str
            игровое имя человека
    Methods
    -------
        name(self) -> str:
            Геттер имени игрока-человека.
        name(self, _name) -> None:
            Сеттер имени игрока-человека.
        ask(self) -> Coord:
            Переопределенный метод, возвращающий объект Coord, отвечающий за координаты игрового поля игрока-человека.


    """

    def __init__(self, board, enemy):
        """
        Конструктор класса игрок-человек.

        Parameters
        ----------
            board : GameBoard
                собственное игровое поле
            enemy : GameBoard
                игровое поле соперника

        Returns
        -------
            None
        """
        super().__init__(board, enemy)
        self.__name = 'User'

    @property
    def name(self) -> str:
        """
        Геттер имени игрока-человека.

        Returns
        -------
            __name : str
                имя игрока-человека
        """
        return self.__name

    @name.setter
    def name(self, _name) -> None:
        """
        Сеттер имени игрока-человека.

        Parameters
        ----------
            _name : str
                имя игрока-человека

        Returns
        -------
            None
        """
        self.__name = _name

    def ask(self) -> Coord:
        """
        Переопределенный метод, возвращающий объект Coord, отвечающий за координаты игрового поля игрока-человека.

        Returns
        -------
            comp_coord : Coord
                объект класса Coord, отвечающий за координаты игрового поля.

        """
        while True:
            coords: list = input("Ваш ход: ").split()

            if len(coords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x_coord, y_coord = coords

            if not (x_coord.isdigit()) or not (y_coord.isdigit()):
                print(" Введите числа! ")
                continue

            x_coord, y_coord = int(x_coord), int(y_coord)

            return Coord(x_coord - 1, y_coord - 1)
