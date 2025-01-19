from poo.topic05encapsulation.package01.person import Person


def main():
    person = Person("Alice")
    print(person.name)
    person.name = "Bob"
    print(person.name)

    person1 = Person('Carlos')
    person1.name = 'Esteban'
    print(person1.name)


if __name__ == "__main__":
    main()
