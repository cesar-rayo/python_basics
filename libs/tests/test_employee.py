import sys
sys.path.insert(1, '../')

import unittest

from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")
        self.emp_1 = Employee('John', 'Smith', 50000)
        self.emp_2 = Employee('Colm', 'Tox', 60000)

    def tearDown(self):
        print("tearDown")

    def test_email(self):
        self.assertEqual(self.emp_1.email, "John.Smith@company.com")
        self.assertEqual(self.emp_2.email, "Colm.Tox@company.com")

        self.emp_1.first = "Test"

        self.assertEqual(self.emp_1.email, "Test.Smith@company.com")

    def test_fullname(self):
        self.emp_1.fullname = "Test User1"
        self.emp_2.fullname = "Test User2"

        self.assertEqual(self.emp_1.email, "Test.User1@company.com")
        self.assertEqual(self.emp_2.email, "Test.User2@company.com")

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52000)
        self.assertEqual(self.emp_2.pay, 62400)

    def test_monthly_schedule_ok(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Smith/May')
            self.assertEqual(schedule, "Success")

    def test_monthly_schedule_fail(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('Jun')
            mocked_get.assert_called_with('http://company.com/Tox/Jun')
            self.assertEqual(schedule, "Bad response!")

    def test_pay_per_months_ok(self):
        result = int(self.emp_1.pay_per_months(2))
        self.assertEqual(result, 25000)

    def test_pay_per_months_fail(self):
        with self.assertRaises(ValueError):
            self.emp_1.pay_per_months(0)

if __name__ == '__main__':
    unittest.main()
