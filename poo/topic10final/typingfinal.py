from typing import Final, final

class Config:
    """Atrribute Final"""

    # Este atributo no debe cambiar
    VERSION: Final = "1.0.0"


class Animal:
    """Method Final"""

    @final
    def breathe(self):
        """Este método no debe ser sobrescrito en subclases."""
        print("Breathing...")


class Dog(Animal):
    """Class Dog"""
    # Esto generaría error en análisis estático (mypy/pyright)
    # def breathe(self):
    #     print("Dog breathing differently")


@final
class Database:
    """Class Final"""

# Esto marcaría error en el analizador estático
# class MySQL(Database):
#     pass
