from poo.topic04methods.marker import Marker


def main():
    m1 = Marker('CranDache')
    print(m1)
    m2 = Marker('Faber-Castell')
    print(m2)

    print(m1.get_brand())
    print(m2.brand)

    # m1._change_ink('Red') Warning
    # m1.__clean_ink Error
    # m1._Marker__clean_ink() # All methods and attributes in python are public


if __name__ == "__main__":
    main()
