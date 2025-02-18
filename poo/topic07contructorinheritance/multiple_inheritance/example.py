class A:
    """class A"""
    def __init__(self):
        print("Constructor de A")


class B:
    """class B"""
    def __init__(self):
        print("Constructor de B")


class C(A, B):
    """class C"""
    def __init__(self):
        super().__init__()  # Llama al primer constructor según el MRO
        print("Constructor de C")


#  No es recomendado, ya que ignora super() y el MRO.
# class C(A, B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         print("Constructor de C")



obj = C()