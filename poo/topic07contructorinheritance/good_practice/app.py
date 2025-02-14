from poo.topic07contructorinheritance.bad_practice.student import Student


def main():
    s = Student(name='Sharid', age=18, university='UNAL')
    print(s.name, s.age, s.university)


if __name__ == "__main__":
    main()
