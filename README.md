```
    # emp_1 = Employee('John', 'Smith', 50000)

    # print(emp_1.email)
    # emp_1.first = "Jim"
    # print(emp_1.email)

    # emp_1.fullname = "Corey Schafer" # triggers the fullname setter
    # print(emp_1.email)

    # del emp_1.fullname

    # print(isinstance(mgr_1, Developer))
    # print(issubclass(Manager, Developer))

    # mgr_1.print_emps()

    # mgr_1.add_emp(dev_2)
    # mgr_1.print_emps()

    # mgr_1.remove_emp(dev_1)
    # mgr_1.print_emps()

    # emp_1 = Employee('John', 'Smith', 50000)
    # emp_2 = Employee('Test', 'User', 50000)
    # emp_3 = Employee.from_string("First-Last-50000")

    # print(emp_1) # triggers str method by default
    # print(repr(dev_1))
    # print(emp_1 + emp_2) # uses the __add__ method in Employee
    # print(len(emp_1)) # uses the __len__ method

    # print(help(Developer)) #Check the class description
    # print(dev_1.__dict__)

    #================
    # import datetime
    # my_date = datetime.date(2019, 7, 27)
    # print(Employee.is_workday(my_date))

    #================
    # Employee.set_raise_amt(1.06)

    # print(emp_1.pay)
    # emp_1.apply_raise()
    # print(emp_1.pay)

    # print(emp_3.pay)
    # emp_3.apply_raise()
    # print(emp_3.pay)

    #================

    #emp_2.raise_amount = 1.05

    # print(emp_1.pay)
    # emp_1.apply_raise()
    # print(emp_1.pay)

    # print(emp_2.pay)
    # emp_2.apply_raise()
    # print(emp_2.pay)

    # print(Employee.num_of_emps)
```