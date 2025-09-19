from poo.topic11methodsoverwrite.package01.animals import Animal, Cat, Dog


def main():
    a = Animal()
    d = Dog()
    c = Cat()

    print(a.sound())  # ➡ Some generic sound
    print(d.sound())  # ➡ Woof!
    print(c.sound())  # ➡ Meow!


if __name__ == "__main__":
    main()
