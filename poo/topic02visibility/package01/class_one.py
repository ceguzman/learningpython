class ClassOne:
    """Class One"""

    class _ClassTwo:
        """Class Two"""

        def __init__(self):
            self.value = "This is an instance of _ClassTwo"

    def create_object_class_two(self):
        return ClassOne._ClassTwo()
