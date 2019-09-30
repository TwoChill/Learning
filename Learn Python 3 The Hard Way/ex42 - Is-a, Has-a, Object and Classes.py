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


# Create instanse of Class Employee
emp_1 = Employee('Michael', 'Python', 50000)  # Initsiate with init arugments
emp_2 = Employee('Maud', 'Ruby', 40000)  # Initsiate with init arugments

#==================================================================#
#==================================================================#
#==================================================================#

print(emp_1.fullname())
print(emp_1.email, '\n')

#==================================================================#
# Class methode is called and printed out.
print(f'{emp_1.fullname()} has a pay of {emp_1.pay}')
print(f'{emp_1.fullname()} got a raise. (* {emp_1.raise_amount_var})')
emp_1.apply_raise()
print(f'{emp_1.fullname()} has a pay of {emp_1.pay}\n')
#------------------------------------------------------------------#
print(f'{emp_2.fullname()} has a pay of {emp_2.pay}')
print(f'{emp_2.fullname()} got a raise. (* {emp_2.raise_amount_var})')
emp_2.apply_raise()
print(f'{emp_2.fullname()} has a pay of {emp_2.pay}\n')

#==================================================================#
# With (<instance>.__dict__) you can see what values that instance or class has.

# print(Employee.__dict__)
print(emp_1.__dict__)
# print(emp_2.__dict__)

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
print(emp_2.raise_amount_var, '\n')
# #==================================================================#

# Using Alternative Constructors

new_emp_1 = 'John-Doe-90000'
new_emp_2 = 'Kim-Jane-80000'
new_emp_3 = 'Doe-John-190000'


emp_3 = Employee.from_string(new_emp_1)
emp_4 = Employee.from_string(new_emp_2)
emp_5 = Employee.from_string(new_emp_3)

print(emp_3.fullname(), '-', emp_3.email, '-', emp_3.pay)
print(emp_4.fullname(), '-', emp_4.email, '-', emp_4.pay)
print(emp_5.fullname(), '-', emp_5.email, '-', emp_5.pay)

print(Employee.__dict__)
