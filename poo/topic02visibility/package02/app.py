from poo.topic02visibility.package02.table import Table


def main():
    table = Table()
    print(table.legs)
    # print(table._color) # Warning
    print(table.material)
    # print(table.__material) AttributeError: 'Table' object has no attribute '__material'. Did you mean: 'material'?


if __name__ == "__main__":
    main()
