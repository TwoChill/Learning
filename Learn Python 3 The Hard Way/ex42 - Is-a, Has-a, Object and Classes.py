# Animal is-a object
class Animal(object):
    print("I is Animal")

# Dog is-a object Animal


class Dog(Animal):

    def __init__(self, name):
        # That has-a attribute name
        self.name = name

# Cat is-a object


class Cat(Animal):

    def __init__(self, name):
        # That has-a attribute name
        self.name = name

# Person is a object


class Person(object):

    def __init__(self, name):
        # That has-a attribute name
        self.name = name

        # That also has-a attribute pet of some kind
        self.pet = None

# Employee is-a object


class Employee(Person):

    def __init__(self, name, salary):
        # Employee has-a super() method that taks name from parent class Person.
        super(Employee, self).__init__(name)
        # Employee has-a attribute named salary
        self.salary = salary

# Fish is-a object


class Fish(object):
    pass

# Salmon is-a object


class Salmon(Fish):
    pass

# Halibut is-a object


class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog('Rover')

# satan is-a instance of class Cat.
satan = Cat('Satan')

# mary is-a instance of class Person
mary = Person("Mary")

# mary has-a attribute pet named satan
mary.pet = satan

# frank is-a instance of class Employee
frank = Employee('Frank', 100000)

# Frank has-a attribute pet named rover
frank.pet = rover

# flipper is-a instance of class Fish
flipper = Fish()

# crouse is a instance of class Salmon
crouse = Salmon()

# Harry is a instance of class Halibut
harry = Halibut()
