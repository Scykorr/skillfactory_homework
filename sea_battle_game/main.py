from random import randint


class Coord:
    """
    Класс, описывающий координату на игровом поле
    """

    def __init__(self):
        self.__x_coord = None
        self.__y_coord = None
        self.__sign = None

    @property
    def x_coord(self):
        return self.__x_coord

    @x_coord.setter
    def x_coord(self, _x_coord):
        check_flag = self._check_coord(_x_coord, _name_coord='x')
        if check_flag:
            self.__x_coord = _x_coord

    @property
    def y_coord(self):
        return self.__y_coord

    @y_coord.setter
    def y_coord(self, _y_coord):
        check_flag = self._check_coord(_y_coord, _name_coord='y')
        if check_flag:
            self.__y_coord = _y_coord

    @property
    def sign(self):
        return self.__x_coord

    @sign.setter
    def sign(self, _sign):
        self.__sign = _sign

    @staticmethod
    def _check_coord(_coord, _name_coord):
        try:
            if not isinstance(_coord, int):
                raise TypeError
            elif not 0 <= _coord <= 6:
                raise ValueError
            else:
                return True
        except TypeError:
            print(f'Значение {_name_coord} должно быть целым неотрицательным числом')
        except ValueError:
            print(f'Значение {_name_coord} должно находиться в промежутке от 0 до 6')


class Ship:

    def __init__(self, positions):
        self.__positions = positions
        self.__name = None
        self._set_name(positions)

    @property
    def pos(self):
        return self.__positions

    def _set_name(self, _pos):
        if len(_pos) == 1:
            self.__name = 'Подводная лодка'
        elif len(_pos) == 2:
            self.__name = 'Эсминец'
        elif len(_pos) == 3:
            self.__name = 'Крейсер'


class Gamer:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class GameBoard:

    def __init__(self, ships, coords):
        pass


class Errors(Exception):

    def __init__(self):
        pass


class GameLogic:

    def __init__(self):
        self.ships = []
        self.coordinates = []

class GameEvent:
    # пустое событие
    Event_None = 0
    # событие таймера
    Event_Tick = 1
    # событие "выстрела" по цели
    Event_Hit = 2

    def __init__(self, type, data) -> None:
        self.type = type
        self.data = data

    def getType(self):
        return self.type

    def getData(self):
        return self.data

class GameGraphic:

    def __init__(self, w, h, logic) -> None:
        self.main_w = w
        self.main_h = h
        self.logic = logic

    def draw_field(self):
        draw_list = [[0 for _ in range(6)] for _ in range(6)]
        for el in draw_list:
            print(*el)

        # тут будет цикл обработки сообщений и взаимодействия с пользователем
    def run(self):
        running = True
        while running:
            # сначала посылаем сообщение Event_Tick, чтобы была сгенерирована цель
            self.processEvent(GameEvent(GameEvent.Event_Tick, None))

            # отрисовываем то, что сейчас должно быть на доске
            self.draw()

            # запрашиваем команды у пользователя
            print('------------------')
            print('0. exit')
            print('1. hit target')
            cmd = int(input())

            # значение пустого события по умолчанию
            event = GameEvent(GameEvent.Event_None, None)
            # если команда 0 - идем на выход
            if cmd == 0:
                running = False
                continue
            # если команда 1 запрашиваем координаты
            if cmd == 1:
                x = int(input('input X: '))
                y = int(input('input Y: '))
                event = GameEvent(GameEvent.Event_Hit, Pos(x, y))

            # отрабатываем событие
            self.processEvent(event)

    def processEvent(self, event):
        self.logic.processEvent(event)

if __name__ == "__main__":
    first_coord = Coord()
    first_coord.x_coord = 5
    first_coord.y_coord = 6
    # first_ship = Ship()
    game = GameGraphic()
    game.draw_field()
