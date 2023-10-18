"""
Основной файл игры "Морской бой"
"""

from random import randint
from my_exceptions import BoardWrongShipException
from players import Computer, User
from main_elements import GameBoard, Ship, Coord
from typing import Optional


class Game:
    """
    Класс игры.

    ...

    Attributes
    ----------
        size : int
            размер игрового поля
        user_board : GameBoard
            объект игровой доски пользователя
        comp_board : GameBoard
            объект игровой доски компьютера
        computer : Computer
            объект игрока компьютера
        user : User
            объект игрока человека

    Methods
    -------
        get_board(self) -> GameBoard:
            Метод, возвращающий игровое поле.
        random_place(self) -> Optional[GameBoard]:
            Метод, размещающий корабли на игровом поле
        get_first_page(self) -> None:
            Метод, выводящий приветственное сообщение
        play_game(self) -> None:
            Метод, реализующий основные действия игры с проверкой выигрыша участников
        start(self) -> None:
            Метод, запускающий игру
    """

    def __init__(self, size: int = 6) -> None:
        """
        Конструктор класса игры.

        Parameters
        ----------
            size : int
                размер игрового поля
        Returns
        -------
            None
        """
        self.size: int = size
        self.user_board: GameBoard = self.get_board()
        self.comp_board: GameBoard = self.get_board()
        self.comp_board.hid = True

        self.computer: Computer = Computer(self.comp_board, self.user_board)
        self.user: User = User(self.user_board, self.comp_board)

    def get_board(self) -> GameBoard:
        """
        Метод, возвращающий игровое поле.

        Returns
        -------
            board : GameBoard
                объект класса игрового поля
        """
        board: Optional[GameBoard] = None
        while board is None:
            board: GameBoard = self.random_place()
        return board

    def random_place(self) -> Optional[GameBoard]:
        """
        Метод, размещающий корабли на игровом поле.

        Returns
        -------
            board : Optional[GameBoard]
                объект класса игрового поля
        """
        ship_lens: list = [3, 2, 2, 1, 1, 1, 1]
        board: GameBoard = GameBoard(size=self.size)
        attempts: int = 0
        for len_ship in ship_lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship: Ship = Ship(Coord(randint(0, self.size), randint(0, self.size)), len_ship, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def get_first_page(self) -> None:
        """
        Метод, выводящий приветственное сообщение.

        Returns
        -------
            None
        """
        self.user.name = input('Игра - Морской Бой\n'
                               'Введите Ваш игровой nickname: ')
        print(f"\nПриветсвуем Вас, {self.user.name}!\n\n"
              f"формат ввода: x y\n"
              f" x - номер строки\n"
              f" y - номер столбца\n")
        input('Для начала игры нажмите клавишу "Enter"\n')

    def play_game(self) -> None:
        """
        Метод, реализующий основные действия игры с проверкой выигрыша участников.

        Returns
        -------
            None
        """
        num: int = 0
        while True:
            print("-" * 20)
            print(f"Доска {self.user.name}:")
            print(self.user.board)
            print("-" * 20)
            print("Доска компьютера:")
            print(self.computer.board)
            if num % 2 == 0:
                print("-" * 20)
                print(f"Ходит {self.user.name}!")
                repeat: bool = self.user.move()
            else:
                print("-" * 20)
                print("Ходит компьютер!")
                repeat: bool = self.computer.move()
            if repeat:
                num -= 1

            if self.computer.board.count == 7:
                print("-" * 20)
                print(f"{self.user.name} выиграл!")
                break

            if self.user.board.count == 7:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self) -> None:
        """
        Метод, запускающий игру.

        Returns
        -------
            None
        """
        self.get_first_page()
        self.play_game()


if __name__ == "__main__":
    game = Game()
    game.start()
