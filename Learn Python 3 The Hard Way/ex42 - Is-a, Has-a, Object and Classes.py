class Employee:
                 # Arguments
    def __init__(self, first, last, pay):
        # Atributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.com'
    # Methode

    def fullname(self):
        # The 'self' in 'self.first/last' is used because then this method will work with other instances
        return '{} {}'.format(self.first, self.last)


# Create instanse of Class Employee
emp_1 = Employee('Michael', 'Python', 50000)  # Initsiate with init arugments
emp_2 = Employee('Maud', 'Ruby', 40000)  # Initsiate with init arugments

# Use method on a instance of a Class
print(emp_1.fullname())
print(emp_2.fullname())

# This is what happends in the background and why we need 'self' as a standard argument.
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))

# Use attribute of a instance of a Class
print(emp_1.email)
print(emp_2.email)