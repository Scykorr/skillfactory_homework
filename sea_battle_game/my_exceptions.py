class BoardException(Exception):
    pass


class OutBoardError(BoardException):
    def __str__(self):
        return "Выбранная клетка находится за пределами игрового поля!"


class CellRepeatError(BoardException):
    def __str__(self):
        return "В выбранную клетку Вы уже стреляли"


class BoardWrongShipException(BoardException):
    pass
