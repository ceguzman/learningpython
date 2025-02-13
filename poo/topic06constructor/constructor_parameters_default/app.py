from poo.topic06constructor.constructor_parameters_default.person import Person


def main():
    p1 = Person()
    print(p1.name, p1.age)

    p2 = Person(name='Carlitos', age=23)
    print(p2.name, p2.age)


if __name__ == "__main__":
    main()
