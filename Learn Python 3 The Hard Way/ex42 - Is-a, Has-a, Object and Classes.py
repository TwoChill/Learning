class Employee:

    # This is a Class variable
    raise_amount = 1.04

    # dunder __init__ takes arguments
    def __init__(self, first, last, pay):
        # These are the attributes of class Employee
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.com'

    def fullname(self):
        # The 'self' in 'self.first/last' is used because then this method will work with other instances
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # Class variables (raise_amount) can be access throught the Class itself ('Employee.) or a instance of that clas ('self.')
        self.pay = int(self.pay * self.raise_amount)


# Create instanse of Class Employee
emp_1 = Employee('Michael', 'Python', 50000)  # Initsiate with init arugments
emp_2 = Employee('Maud', 'Ruby', 40000)  # Initsiate with init arugments


print(emp_1.fullname())
print(emp_1.email, '\n')

#==================================================================#
# Class methode is called and printed out.
print(f'{emp_1.fullname()} has a pay of {emp_1.pay}')

print(f'{emp_1.fullname()} got a raise. (* {emp_1.raise_amount})')
emp_1.apply_raise()

print(f'{emp_1.fullname()} has a pay of {emp_1.pay}\n')
#------------------------------------------------------------------#
print(f'{emp_2.fullname()} has a pay of {emp_2.pay}')

print(f'{emp_2.fullname()} got a raise. (* {emp_2.raise_amount})')
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

emp_1.raise_amount = 1.05    # Creats a new attribute only in this instance!
print(Employee.raise_amount)
print(emp_1.raise_amount)    
print(emp_1.__dict__)        # You'll see that the raise_amount has been added.
                             # This way the class doesn't need to  be enfoked

# Change class variable (for the entire class and subclasses)
Employee.raise_amount = 1.05 # Creates a new attribute for the entire class.
print(Employee.raise_amount)
print(emp_1.raise_amount)
#==================================================================#

