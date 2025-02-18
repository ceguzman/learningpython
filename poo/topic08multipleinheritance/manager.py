from poo.topic08multipleinheritance.employed import Employed
from poo.topic08multipleinheritance.user import User


class Manager(User, Employed):
    """class Manager"""

    def __init__(self, username, password, salary, department):
        print("initializing Manager")
        super().__init__(username, password) # Llama al primer constructor según el MRO
        super(User, self).__init__(salary)   # Llama al siguiente constructor en la jerarquía
        # Employed.__init__(self, salary)
        self.departamento = department

    def mostrar_info(self):
        return f"{self.show_user()} | {self.show_salary()} | Department: {self.departamento}"
