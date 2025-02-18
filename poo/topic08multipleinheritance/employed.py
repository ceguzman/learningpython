class Employed:
    """class Employed"""

    def __init__(self, salary):
        print("Initializing Employed")
        self.salary = salary

    def show_salary(self):
        return f"Salary: {self.salary}"
