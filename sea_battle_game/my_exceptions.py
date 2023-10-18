"""
Модуль, содержащий собственные классы исключений
"""


class OutBoardError(Exception):
    """
    Класс исключения при попадании в координату за игровое поле.
    Родитель - Exception.
    """
    def __str__(self):
        return "Выбранная клетка находится за пределами игрового поля!"


class CellRepeatError(Exception):
    """
    Класс исключения при повторном попадании в точку игрового поля.
    Родитель - Exception.
    """
    def __str__(self):
        return "В выбранную клетку Вы уже стреляли!"


class BoardWrongShipException(Exception):
    """
    Класс исключения при некорректном добавлении корабля.
    Родитель - Exception.
    """
    pass
