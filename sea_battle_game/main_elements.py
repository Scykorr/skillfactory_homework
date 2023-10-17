from my_exceptions import OutBoardError

class Coord:
    """
    Класс, описывающий координату на игровом поле
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
        self.__name = None
        self._set_name(ship_length)

    @property
    def dots(self):
        ship_dots = []
        for num in range(self.__ship_length):
            cur_x = self.__first_ship_part.x
            cur_y = self.__first_ship_part.y

            if self.__direct == 0:
                cur_x += num

            elif self.__direct == 1:
                cur_y += num

            ship_dots.append(Coord(cur_x, cur_y))

        return ship_dots

    def _set_name(self, _length):
        if len(_length) == 1:
            self.__name = 'Подводная лодка'
        elif len(_length) == 2:
            self.__name = 'Эсминец'
        elif len(_length) == 3:
            self.__name = 'Крейсер'


class GameBoard:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid

        self.count = 0

        self.field = [["O"] * size for _ in range(size)]

        self.busy = []
        self.ships = []

    def add_ship(self, ship):

        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise OutBoardError()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Coord(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x_coord][cur.y_coord] = "."
                    self.busy.append(cur)

    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def shot(self, d):
        if self.out(d):
            raise OutBoardError()

        if d in self.busy:
            raise OutBoardError()

        self.busy.append(d)

        for ship in self.ships:
            if d in ship.dots:
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[d.x][d.y] = "."
        print("Мимо!")
        return False

    def begin(self):
        self.busy = []
