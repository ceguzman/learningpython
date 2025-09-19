class Animal:
    """Class Animal"""
    def sound(self):
        """Método que será sobreescrito por las subclases"""
        return "Some generic sound"

class Dog(Animal):
    """Class Dog"""
    def sound(self):
        """Sobreescritura del método sound"""
        return "Woof!"

class Cat(Animal):
    """Class Cat"""
    def sound(self):
        return "Meow!"
