# from poo.topic01class.animal import Animal
from poo.topic01class.dog import Dog


def main():
    dog = Dog()
    print(dog.eat())
    print(dog.die())
    print(dog.reproduce())

    # You can create an abstract class if it has no abstract methods
    # animal = Animal()


if __name__ == "__main__":
    main()
