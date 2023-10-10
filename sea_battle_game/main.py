class Coord:
    """
    Класс, описывающий координату на игровом поле
    """

    def __init__(self):
        self.__x_coord = None
        self.__y_coord = None

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


class GameGraphic:
    def __init__(self):
        pass

    def draw_field(self):
        pass


if __name__ == "__main__":
    first_coord = Coord()
    first_coord.x_coord = 5
    first_coord.y_coord = 6
    print(first_coord.x_coord)
    print(first_coord.y_coord)
