class Marker:
    """Class Marker"""

    def __init__(self, brand: str):
        self.__brand = brand
        self.__color = 'Blue'

    @property
    def brand(self) -> str:
        return self.__brand

    def get_brand(self) -> str:
        """Public Method"""
        return self.__brand

    def _change_ink(self, color: str) -> None:
        """Protected Method"""
        self.__clean_ink()
        self.__color = color

    def __clean_ink(self) -> None:
        """Private Method"""

    def __str__(self):
        return f'This marker is from the brand {self.__brand} and the color is {self.__color}'
