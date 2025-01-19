from poo.topic03atrributes.package01.square import Square


def main():
    square = Square()
    square.side = 5
    print(square.area)
    print(square)


if __name__ == "__main__":
    main()
