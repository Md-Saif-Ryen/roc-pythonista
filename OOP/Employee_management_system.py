"""
Employee first,last name, email, bonus-pa, increament salary -pa 
"""

import datetime

class Employee:
    annual_increament = 1.10

    def __init__(self, first,  last, salary, wrkng_yr, ex_yr, gender=None, hobbies = None):
        self.first = first
        self.last = last
        self.salary = salary
        self.wrkng_yr = wrkng_yr
        self.ex_yr = ex_yr

        if gender == None:
            self.gender = ''
        else:
            self.gender = gender
        if hobbies == None:
            self.hobbies = []
        else:
            self.hobbies = hobbies 
    
    def emp_fullname(self):
        return f'{self.first.capitalize()} {self.last.capitalize()}'

    def emp_email(self):
        return f'{self.first.lower()}.{self.last.lower()}@company.com'
    
    def emp_nextyr_salary(self):
        return f'Your salary in next year will be {self.salary * self.annual_increament}'
    
    def emp_bonus(self):
        if self.wrkng_yr < 5:
            Employee.bonus_pa = 15000
            return f'Your bonus at this point per annum is {Employee.bonus_pa}'
        elif self.wrkng_yr >= 5 and self.wrkng_yr <= 10:
            Employee.bonus_pa = 18000
            return f'Your bonus at this point per annum is {Employee.bonus_pa}'
        else:
            Employee.bonus_pa = 20000
            return f'Your bonus at this point per annum is {Employee.bonus_pa}'

    def salary_inc_pa(self):
        if self.ex_yr <= 5:
            Employee.annual_increament = 1.10
            return f'Your salary will increase by {self.annual_increament} annualy\nYour next year salary will be {self.salary * self.annual_increament}'
        elif self.ex_yr > 5 and self.ex_yr <= 10:
            Employee.annual_increament = 1.15
            return f'Your salary will increase by {self.annual_increament} annualy\nYour next year salary will be {self.salary * self.annual_increament}'
        else:
            Employee.annual_increament = 1.20
            return f'Your salary will increase by {self.annual_increament} annualy\nYour next year salary will be {self.salary * self.annual_increament}'
    
    @classmethod
    def from_str(cls, string):
        first, last, salary, wrkng_yr, ex_yr, gender, hobbies = string.split('-')
        return cls(first, last, salary, wrkng_yr, ex_yr, gender, hobbies)

    @staticmethod
    def is_holiday(self, day):
        if day.weekday() == 5 or day.weekday() == 6:
            return 'Yes'
        return 'No'
    
    def __str__(self):
        return f'Fullname : {self.emp_fullname()}\nEmail : {self.emp_email()}\nSalary : {self.salary}'





