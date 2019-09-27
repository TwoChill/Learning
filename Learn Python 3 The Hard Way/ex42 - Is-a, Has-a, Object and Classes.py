class Employee:
                 # Arguments
    def __init__(self, first, last, pay):
        # Atributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    # Methode
    def fullname(self):
        # The 'self' in 'self.first/last' is used because then this method will work with other instances
        return '{} {}'.format(self.first, self.last)
        
# Create instanse of Class Employee
emp_1 = Employee('Michael', 'de France', 50000) # Initsiate with init arugments
emp_2 = Employee('Maud', 'vandeHaterd', 40000) # Initsiate with init arugments

# Use method on a instance of a Class
print(emp_1.fullname())
# Use attribute of a instance of a Class
print(emp_1.email)

# # Animal is-a object and a parent Class
# class Animal(object):
#     def __init__(self, owner):
#         # Class Animal has-a attribute owner
#         self.owner = owner

#         print(f'This Animal has a owner namend: {self.owner}')


# # Dog is-a object and inherits attributes from Animal
# class Dog(Animal):
#     # Dog has-a attrinute name
#     def __init__(self, name):
#         self.name = name
#         self.owner = Person.

#     def get_info(self):
#         # Dog has-a methode called 'get_info' that inhertis atributesfrom Animal.
#         super().__init__(self.owner)
#         print(f'This is a Dog named {self.name} ')


# # Cat is-a object and inherits from attributes from Animal
# class Cat(Animal):
#     # Cat has-a attribute name
#     def __init__(self, name):
#         self.name = name

#     def get_info(self):
#         super().__init__(self.owner)
#         print(f'This is a Cat named {self.name}')


# # Person is-a object and a parent class
# class Person(object):
#     # That has-a attribute called name and some kinde of pet
#     def __init__(self, name):
#         self.name = name
#         self.pet = None

#     def get_pet(self):
#         print(f"This Person's name is {self.name}")

#         if self.pet == None:
#             self.pet = input(f'Does {self.name} has a pet?')
#             if self.pet == 'yes'.lower():
#                 self.pet = input(f'What is his or her name?')
#         else:
#             print(f"{self.name} has no pets!")


# # Employee is-a object and inherits form class Person
# class Employee(Person):
#     # Employee has-a name and a salary
#     def __init__(self, name, salary):
#         # Employee has-a super() method that taks name from parent class Person.
#         super().__init__(name)
#         # Employee has-a attribute named salary
#         self.salary = salary

# # Fish is-a object


# class Fish(object):
#     def __init__(self, name, eatable):
#         self.name = name
#         self.eatable = eatable

#     def get_info(self):

#         print(f'The name of this Fish is {self.name}')

#         if self.eatable == 'yes'.lower():
#             print('This fish is eatable!')
#         else:
#             print('This fish is not eatable!')


# # Salmon is-a object and inherits from parent Class Fish
# class Salmon(Fish):
#     def __init__(self, name):
#         self.name = name

#     def get_info(self):
#         super().__init__(self.name, self.eatable)


# # Halibut is-a object


# class Halibut(Fish):
#     pass


# mike = Person('Mike')
# #mike.get_pet()

# # rover is-a Dog
# rover = Dog('Roverr')
# rover.get_info()

# # # satan is-a instance of class Cat.
# # satan = Cat('Satan')

# # # mary is-a instance of class Person
# # mary = Person("Mary")

# # # mary has-a attribute pet named satan
# # mary.pet = satan

# # # frank is-a instance of class Employee
# # frank = Employee('Frank', 100000)

# # # Frank has-a attribute pet named rover
# # frank.pet = rover

# # flipper is-a instance of class Fish
# # flipper = Fish('flipper', 'NO')
# # flipper.get_info()

# # # crouse is a instance of class Salmon
# # crouse = Salmon('crouse')

# # # Harry is a instance of class Halibut
# # harry = Halibut('Maby')
