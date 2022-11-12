import requests

class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay,month):
        self.first = first
        self.last = last
        self.pay = pay
        self.month=month
    # @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    # @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay

    def monthly_schedule(self):   #activities happening each month
        response = requests.get("http://company.com/")
        if response.ok:
            return 'hello'
        else:
            return 'Bad Response!'
# employee2=Employee("Shamim","Gard",3400,"August")
# print(employee2.email())
# print(employee2.fullname())
# print(employee2.apply_raise())
# print(employee2.monthly_schedule())

