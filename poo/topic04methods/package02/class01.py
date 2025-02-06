class Class01:
    """"This is a Class"""

    def normal_method(self):
        return 'Normal Method / Intance - Object', self

    @classmethod
    def class_method(cls):
        return 'Class Method', cls

    @staticmethod
    def static_method():
        return "Static Method"
