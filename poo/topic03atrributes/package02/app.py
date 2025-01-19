from poo.topic03atrributes.package01.square import Square


def main():
    square1 = Square()
    square1.side = 6
    square2 = square1
    square3 = square2
    square1.side = 10

    square4 = Square()
    square4 = square1

    print(square1.side, square1.__hash__)
    print(square2.side, square2.__hash__)
    print(square3.side, square3.__hash__)
    print(square4.side, square4.__hash__)

    square4.side = 1

    print(square4.side, square4.__hash__)


if __name__ == "__main__":
    main()
