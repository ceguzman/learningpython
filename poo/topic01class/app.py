# from poo.topic01class.animal import Animal
from poo.topic01class.sexualy.dog import Dog
from poo.topic01class.asexualy.sponge import Sponge


def main():
    dog = Dog()
    print('==== class Dog ====')
    print(dog.barks())
    print(dog.eat())
    print(dog.die())
    print(dog.reproduce(), end='\n\n')

    print('==== class Sponge ====')
    sponge = Sponge()
    print(sponge.eat())
    print(sponge.reproduce())
    print(sponge.die())

    # You can create an abstract class if it has no abstract methods
    # animal = Animal()


if __name__ == "__main__":
    main()
