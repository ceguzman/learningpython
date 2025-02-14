class Person:

    """This a class Person"""
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Desconocido')
        self.age = kwargs.get('age', 0)
        self.id_card = kwargs.get('id_card', None)
