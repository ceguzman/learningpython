from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Class Animal"""

    def eat(self) -> str:
        return 'I eat'

    def die(self) -> str:
        return 'I die'

    @abstractmethod
    def reproduce(self) -> None:
        pass
