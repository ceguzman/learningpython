class Car:
    """📌 Clase que representa un coche con un atributo estático."""
    # 📌 Atributo estático (compartido por todas las instancias)
    wheels = 4

    def __init__(self, brand, model):
        """📌 Constructor de la clase Car."""
        self.brand = brand  # Atributo de instancia
        self.model = model  # Atributo de instancia

    def display_info(self):
        return f"{self.brand} {self.model} with {Car.wheels} wheels"
