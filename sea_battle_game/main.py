from random import randint
from my_exceptions import BoardWrongShipException
from players import Computer, User
from main_elements import GameBoard, Ship, Coord


class Game:
    def __init__(self, size=6):
        self.size = size
        user_board = self.get_board()
        comp_board = self.get_board()
        comp_board.hid = True

        self.computer = Computer(comp_board, user_board)
        self.user = User(user_board, comp_board)

    def get_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        ship_lens = [3, 2, 2, 1, 1, 1, 1]
        board = GameBoard(size=self.size)
        attempts = 0
        for len_ship in ship_lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Coord(randint(0, self.size), randint(0, self.size)), len_ship, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def get_first_page(self):
        self.user.name = input('Игра - Морской Бой\n'
                               'Введите свой игровой nickname: ')
        print(f"\nПриветсвуем Вас, {self.user.name}!\n\n"
              f"формат ввода: x y\n"
              f" x - номер строки\n"
              f" y - номер столбца\n")
        input('Для начала игры нажмите клавишу "Enter"\n')

    def play_game(self):
        num = 0
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
                repeat = self.user.move()
            else:
                print("-" * 20)
                print("Ходит компьютер!")
                repeat = self.computer.move()
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

    def start(self):
        self.get_first_page()
        self.play_game()


if __name__ == "__main__":
    game = Game()
    game.start()
