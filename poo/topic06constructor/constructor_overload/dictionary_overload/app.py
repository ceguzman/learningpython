from poo.topic06constructor.constructor_overload.dictionary_overload.person import Person


def main():
    p = Person(name='Esteban', age=23)
    print(p.name, p.age, p.id_card)

    p2 = Person(name='Carlitos', age=24, id_card='789123')
    print(p2.name, p2.age, p2.name)

if __name__ == "__main__":
    main()
