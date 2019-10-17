import os
os.system('clear')


class Employee:

    # This is a Class variable
    num_of_emps = 0
    raise_amount_var = 1.04

    # dunder __init__ takes arguments
    def __init__(self, first, last, pay):
        # These are the attributes of class Employee
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        # The 'self' in 'self.first/last' is used because then this method will work with other instances
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # Class variables (raise_amount) can be access throught the Class itself ('Employee.) or a instance of that clas ('self.')
        self.pay = int(self.pay * self.raise_amount_var)

    # This DECORATOR makes sure that we use the class as the first argument instead of an instance.
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount_var = amount

    # Alternative Constructor.
    @classmethod
    def from_string(cls, string):
        first, last, pay = string.split('-')
        return cls(first, last, pay)
        # This will create and return the new employee. Like the creation of an instance (Employee(frist, last, pay))

    # It's a reqular function that does not take an instance or a class as its first argument.
    # @staticmethod vs requalar fucnton: If this function has a logical reason for this class, use staticmetod.
    @staticmethod
    def static_func():
        pass


class Developer(Employee):
    def __init__(self, first, last, pay, program_lang):
        # Class Employee handels the (first, last and pay) arguments
        super().__init__(first, last, pay)
        self.program_lang = program_lang

    raise_amount_var = 1.50


class Manager(Employee):
    # !! Never pass in meutable datatypes as default args.
    def __init__(self, first, last, pay, employees=None):
        # Class Employee handels the (first, last and pay) args.
        super().__init__(first, last, pay)
        self.employees = employees

        if employees is None:
            self.employees == []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(self.fullname(), 'manages over:', emp.fullname())


# Create instanse of Class Employee / Developer
emp_1 = Employee('Maud', 'Ruby', 50000)  # Initsiate with init arugments
# Initsiate with init arugments
dev_1 = Developer('Michael', 'deF', 40000, 'Python')
# print(help(Developer))
mng_1 = Manager('Mattijs', 'Koning', 100000, [emp_1, dev_1])

#==================================================================#
#==================================================================#
#==================================================================#

print(emp_1.fullname())
print(emp_1.email, '\n')
print(dev_1.email)
print('Primary Language:', dev_1.program_lang, '\n')
print(mng_1.fullname())
print(mng_1.email, '\n')

#==================================================================#
# Class methode is called and printed out.
print(f'{emp_1.fullname()} has a pay of {emp_1.pay}')
print(f'{emp_1.fullname()} got a raise. (* {emp_1.raise_amount_var})')
emp_1.apply_raise()
print(f'{emp_1.fullname()} has a pay of {emp_1.pay}\n')
#------------------------------------------------------------------#
print(f'{dev_1.fullname()} has a pay of {dev_1.pay}')
print(f'{dev_1.fullname()} got a raise. (* {dev_1.raise_amount_var})')
dev_1.apply_raise()
print(f'{dev_1.fullname()} has a pay of {dev_1.pay}\n')
#------------------------------------------------------------------#
print(f'{mng_1.fullname()} has a pay of {mng_1.pay}')
print(f'{mng_1.fullname()} got a raise. (* {mng_1.raise_amount_var})')
mng_1.apply_raise()
print(f'{mng_1.fullname()} has a pay of {mng_1.pay}\n')
#==================================================================#
# With (<instance>.__dict__) you can see what values that instance or class has.

# print(Employee.__dict__)
print(emp_1.__dict__)
print(dev_1.__dict__)
print(mng_1.__dict__, '\n')
#==================================================================#
# You can change the class variable of the entere class OR just for a instance

# Change class variable (for an instance)

emp_1.raise_amount_var = 1.05    # Creats a new attribute only in this instance!
print(Employee.raise_amount_var)
print(emp_1.raise_amount_var)
print(emp_1.__dict__)        # You'll see that the raise_amount has been added.
# This way the class doesn't need to  be enfoked

# Change class variable (for the entire class and subclasses)
# Creates a new attribute for the entire class.
Employee.raise_amount_var = 1.05
print(Employee.raise_amount_var)
print(emp_1.raise_amount_var, '\n')
#==================================================================#

print('Number of employees:', Employee.num_of_emps)
#==================================================================#
#==================================================================#
#==================================================================#

# Using the Class Method (@classmetod)
# This is how you can change the Class Variable for the enteir class.
Employee.set_raise_amount(1.25)

print(Employee.raise_amount_var)
print(dev_1.raise_amount_var, '\n')

# Using Alternative Constructors

new_emp_1 = 'John-Doe-90000'
new_dev_1 = 'Kim-Jane-80000'
new_emp_3 = 'Doe-John-190000'


emp_3 = Employee.from_string(new_emp_1)
emp_4 = Employee.from_string(new_dev_1)
emp_5 = Employee.from_string(new_emp_3)

print(emp_3.fullname(), '-', emp_3.email, '-', emp_3.pay)
print(emp_4.fullname(), '-', emp_4.email, '-', emp_4.pay)
print(emp_5.fullname(), '-', emp_5.email, '-', emp_5.pay, '\n')
# #==================================================================#

# The inheritance works. Apply_raise is defined in class Employee. Which now has been used in the class Developer.
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay, '\n')
# #==================================================================#

# Created manger class with abilities to do things
mng_1.print_emp()
print('\n')

mng_1.add_emp(emp_3)
mng_1.add_emp(emp_4)
mng_1.add_emp(emp_5)
mng_1.print_emp()
print('\n')

mng_1.remove_emp(emp_3)
mng_1.remove_emp(emp_5)

mng_1.print_emp()
# #==================================================================#
