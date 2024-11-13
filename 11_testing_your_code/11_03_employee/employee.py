class Employee:
    """Model of stored info on employees"""

    def __init__(self, first, last, salary):
        """Initialize name and salary attributes"""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, pay_increase=5000):
        """Method to increase an employee's salary"""
        self.salary += pay_increase