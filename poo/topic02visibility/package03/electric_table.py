from poo.topic02visibility.package02.table import Table


class ElectricTable(Table):
    """Electric Table"""

    @property
    def color(self) -> str:
        return self._color

    def change_color(self, color: str):
        self._color = color  # Protected
