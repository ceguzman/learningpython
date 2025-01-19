class BankAccount:
    """Class BankAccount"""

    def __init__(self, balance):
        self._balance = 0  # Private attribute with underscore
        self.balance = balance  # Use the setter to validate the initial balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
