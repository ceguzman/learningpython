class Person:
    """Class Person"""
    def greet(self):
        return "Hello!"

class Student(Person):
    """Class Student"""
    def greet(self):
        """Extiende el saludo de Person"""
        return super().greet() + " I am a student."
