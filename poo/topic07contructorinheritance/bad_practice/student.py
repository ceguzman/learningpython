from poo.topic07contructorinheritance.bad_practice.person import Person

class Student(Person):

    """This is a class Studen"""

    # Esto es un ejemplo de una mala practia, al no utilizar el metodo super()
    # Para poder llamar al metodo constructor de la clase padre.

    # pylint: disable=super-init-not-called
    def __init__(self, name, age, university):
        self.name = name
        self.age = age
        self.university = university
