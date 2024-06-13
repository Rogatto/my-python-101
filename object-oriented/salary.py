class Salary:
    def __init__(self, identify, amount):
        self.identify = identify
        self.amount = amount

    def increase_salary(self, amount):
        self.amount += amount

    def decrease_salary(self, amount):
        self.amount -= amount