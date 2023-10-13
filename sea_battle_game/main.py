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

    @pos.setter
    def pos(self, pos):
        self.__positions = pos

    def _set_name(self, _pos):
        if len(_pos) == 1:
            self.__name = 'Подводная лодка'
        elif len(_pos) == 2:
            self.__name = 'Эсминец'
        elif len(_pos) == 3:
            self.__name = 'Крейсер'


class GameGraphic:
    def __init__(self):
        pass

    def draw_field(self):
        print()


if __name__ == "__main__":
    first_coord = Coord()
    first_coord.x_coord = 5
    first_coord.y_coord = 6
    first_ship = Ship()
