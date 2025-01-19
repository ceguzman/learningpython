from poo.topic02visibility.package01.class_one import ClassOne


def main():
    # Create an instance of ClassOne
    class_one = ClassOne()

    # Use the method to create an instance of _ClassTwo
    clas_two = class_one.create_object_class_two()

    # Access the value of the inner class instance
    print(clas_two.value)  # Output: This is an instance of _ClassTwo


if __name__ == "__main__":
    main()
