import requests

class Employee:
    
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first # Instance's variables
        self.last = last
        self.pay = int(pay)
        Employee.num_of_emps += 1 # Class' variable

    @property #Kind of get method in java
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None

    def monthly_schedule(self, month):
        response = requests.get("http://company.com/{}/{}".format(self.last, month))
        if response.ok:
            return response.text
        else:
            return 'Bad response!'


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def pay_per_months(self, months):
        if months == 0:
            raise ValueError("Can not divide by zero")
        else:
            return self.pay / months

    @classmethod
    def set_raise_amt(cls, amount): # Receives class as argument
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day): # Does not receive any class or instance
        if day.weekday() == 5 or day.weekday() == 5:
            return False
        return True

    #Special methods
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.first, self.last)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)
