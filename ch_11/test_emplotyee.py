# Write a test case for Employee called test_employee.py. 
# Write two test methods, test_give_default_raise() and test_give_custom_raise(). 
# Use the setUp() method so you don’t have to create a new employee instance in each test method. 
# Run your test case, and make sure both tests pass.
import unittest
from employee import Employee

class test_employee(unittest.TestCase):
    def setUp(self):
        self.test_case = Employee("oscar", "cisneros", 50000)
    def test_give_default_raise(self):
        self.test_case.give_raise()
        self.assertEqual(self.test_case.salary, 55000)
    def test_give_custom_raise(self):
        self.test_case.give_raise(4500)
        self.assertEqual(self.test_case.salary, 54500)

if __name__ == '__main__':
    unittest.main()