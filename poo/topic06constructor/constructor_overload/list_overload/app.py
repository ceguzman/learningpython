from poo.topic06constructor.constructor_overload.list_overload.person import Person


def main():
    p1 = Person("Luis")
    p2 = Person("Ana", 25)

    print(p1.nombre, p1.edad)  # ✅ Luis 0
    print(p2.nombre, p2.edad)  # ✅ Ana 25


if __name__ == "__main__":
    main()
