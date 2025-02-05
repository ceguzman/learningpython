from poo.topic01class.animal import Animal


class Dog(Animal):
    """Concrete Class Dog"""

    def reproduce(self) -> str:
        return 'The dog reproduces sexually'

    def barks(self) -> str:
        return 'The Dog braks'
