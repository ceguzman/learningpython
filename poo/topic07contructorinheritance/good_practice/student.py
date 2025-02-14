from poo.topic07contructorinheritance.bad_practice.person import Person


class Student(Person):

    """This is a class Studen"""

    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university
