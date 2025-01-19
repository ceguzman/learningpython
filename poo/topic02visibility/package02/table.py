class Table:
    """Class Table"""

    def __init__(self):
        self.legs: int = 4  # Public
        self._color: str = 'Green'  # Protected
        self.__material: str = 'Wood'  # Private

    @property
    def material(self) -> str:
        return self.__material
