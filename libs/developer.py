from employee import Employee

class Developer(Employee):
    raise_amount = 1.10 # overwrites amount for this class

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # Goes to Employee init
        self.prog_lang = prog_lang

    def __repr__(self):
        return "Developer('{}', '{}', {}, '{}')".format(self.first, self.last, self.pay, self.prog_lang)
