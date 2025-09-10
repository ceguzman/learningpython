from poo.topic01class.animal import Animal
from poo.topic01class.sexualy.dog import Dog
from poo.topic01class.asexualy.sponge import Sponge


def main():
    dog = Dog()
    print('==== class Dog ====')
    print(dog.barks())
    print(dog.eat())
    print(dog.die())
    print(dog.reproduce())
    print(Dog.__bases__)
    print('The specie is', Dog.specie, end='\n\n')

    print('==== class Sponge ====')
    sponge = Sponge()
    print(sponge.eat())
    print(sponge.reproduce())
    print(sponge.die())
    print(Sponge.__bases__)
    print('The specie is', Sponge.specie)

    # You can create an abstract class if it has no abstract methods
    # animal = Animal()

    print('\n\n==== class Animal ====')
    print(Animal.__subclasses__())


if __name__ == "__main__":
    main()
