import sys
sys.path.insert(1, './libs')

from developer import Developer
from manager import Manager
from employee import Employee

def main():
    dev_1 = Developer('John', 'Smith', 50000, "Python")
    dev_2 = Developer('Test', 'User', 50000, "Java")

    mgr_1 = Manager('Guy', 'Kustin', 90000, [dev_1])

    mgr_1.print_emps()

    print("using __add__ : {}".format(dev_1 + dev_2)) # uses the __add__ method in Employee

if __name__ == '__main__':
    main()