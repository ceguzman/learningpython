from poo.topic09staticatrributes.car import Car


def main():
    car1 = Car(brand='Toyota', model='2020')
    print(car1.display_info())

    car2 = Car("Ford", "Mustang")
    print(car2.display_info())

    # 🔹 Acceso al atributo estático
    print(Car.wheels)   # ➡ 4 (accediendo desde la clase)
    print(car1.wheels)  # ➡ 4 (accediendo desde la instancia)
    print(car2.wheels)  # ➡ 4 (todas las instancias comparten el valor)

    # 🔹 Modificando el atributo estático
    Car.wheels = 6  # Cambia para todas las instancias
    print(car1.wheels)  # ➡ 6
    print(car2.wheels)  # ➡ 6


if __name__ == "__main__":
    main()
