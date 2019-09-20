## Animal is-a object
class Animal(object):
    pass

## Dog is-a object Animal
class Dog(Animal):

    def __init__(self, name):
        ## That has-a attribute name
        self.name = name

## Cat is-a object
class Cat(Animal):

    def __init__(self, name):
        ## That has-a attribute name
        self.name = name

## Person is a object
class Person(object):

    def __init__(self, name):
        ## That has-a attribute name
        self.name = name

        ## That also has-a attribute pet of some kind
        self.pet = None

## Employee is-a object
class Employee(object):

    def __init__(self, name, salary):
        ## Employee has-a super() function that lets child classes inherit certain attributes?
        super().__init__(name)
        ## Employee has-a attribute named salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salamon is-a object
class Salamon(Fish):
    pass

## Halibut is-a object
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog('Rover')

## satan is-a Cat
satan = Cat('Satan')

## mary is-a person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank is-a Employee and has-a salary
frank = Employee('Frank', 100000)

## Frank has-a pet called rover
frank.pet = rover

## flipper is-a instance of class Fish()
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
