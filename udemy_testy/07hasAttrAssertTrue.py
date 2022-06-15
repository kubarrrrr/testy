import unittest


class Employee:
    """A simple class that describes an employee of the company."""

    tax_rate = 0.17
    bonus_rate = 0.10

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@mail.com'

    @property
    def tax(self):
        return round(self.salary * self.tax_rate, 2)

    def apply_bonus(self):
        self.salary = int(self.salary * (1 + self.bonus_rate))


# enter your solution here
class TestEmployee(unittest.TestCase):
    
    def test_has_email_attr(self):
        sentence1 = 'The Employee class does not have an email attribute'
        self.assertTrue(hasattr(Employee, 'email'), sentence1)
        
    def test_has_tax_attr(self):
        sentence2 = 'The Employee class does not have a tax attribute'
        self.assertTrue(hasattr(Employee, 'tax'), sentence2)
        
    def test_has_apply_bonus(self):
        sentence3 = 'The Employee class does not has an apply_bonus attribute'
        self.assertTrue(hasattr(Employee, 'apply_bonus'), sentence3)
        
if __name__=='__main__':
    unittest.main()