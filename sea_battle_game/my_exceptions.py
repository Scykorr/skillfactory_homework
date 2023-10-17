class OutBoardError(Exception):
    def __str__(self):
        return "Выбранная клетка находится за пределами игрового поля!"

class CellRepeatError(Exception):
    def __str__(self):
        return "В выбранную клетку Вы уже стреляли"

class BoardWrongShipException(Exception):
    pass