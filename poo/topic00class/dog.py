class Dog:
    """Class representing a dog."""
    espiecie = 'Canis lupus familiaris'  # Atributo de clase

    def __init__(self, name, breed):
        print(f'Creating a dog named {name} of breed {breed}')
        # breed-> raza de perro
        self.name = name
        self.breed = breed

    def bark(self):
        return 'Woof! Woof!'

    def walk(self):
        return f'{self.name} is walking.'
