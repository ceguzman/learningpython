class Square:
    """Class Square"""

    def __init__(self):
        self.__side: int = 0
        self.__area: int = 0

    @property
    def side(self) -> int:
        return self.__side

    @side.setter
    def side(self, side: int) -> None:
        self.__side = side
        self.__area = self.side * self.side

    @property
    def area(self) -> int:
        return self.__area
