class Person:
    """This is a class Person"""

    def __init__(self, *args):
        if len(args) == 1:
            self.nombre = args[0]
            self.edad = 0  # Edad por defecto
        elif len(args) == 2:
            self.nombre = args[0]
            self.edad = args[1]
        else:
            self.nombre = "Desconocido"
            self.edad = 0
