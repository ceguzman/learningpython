from poo.topic01class.package01.animal import Animal


class Dog(Animal):
    """Concrete Class Dog"""

    specie = 'Mammal'

    def reproduce(self) -> str:
        return 'The dog reproduces sexually'

    def barks(self) -> str:
        return 'The Dog braks'
