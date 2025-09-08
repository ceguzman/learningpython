from poo.topic00class.dog import Dog


def main():
    dog1 = Dog('Firulais', 'Labrador')
    dog2 = Dog('Max', 'German Shepherd')

    print(end='\n')
    print(f"The dog: {dog1.name} is a: {dog1.breed} \n Type of class: {type(dog1)} \n Espiecie: {dog1.espiecie}", end='\n\n')
    print(f"The dog: {dog2.name} is a: {dog2.breed} \n Type of class: {type(dog1)} \n Espiecie: {dog2.espiecie}", end='\n\n')

    print(dog1.bark(), dog1.walk())
    print(dog2.bark(), dog2.walk(), end='\n\n')

    # Accediendo al atributo de clase
    print(f"Attribute of the class {Dog.espiecie}")


if __name__ == "__main__":
    main()
