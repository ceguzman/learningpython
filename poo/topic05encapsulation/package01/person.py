class Person:
    """Class Person"""

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        """Getter for name."""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Setter for name."""
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError(
                "Name must be a string with alphabetic characters")
