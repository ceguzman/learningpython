from poo.topic11methodsoverwrite.package02.user import Person, Student


def main():
    p = Person()
    s = Student()

    print(p.greet())  # ➡ Hello!
    print(s.greet())  # ➡ Hello! I am a student.


if __name__ == "__main__":
    main()
