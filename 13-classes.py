# a class defines what an object should look like
# object is created based on that class
# to define class use keyword class:
# class Person:
# then can create object from that class:
# person1 = Person("Hassan", 26)
# the class can contain attributes and method
# to give the attribute values at initial object use __init__ method:
# def __init__(self, name: str, age: int):
#        self.name = name
#        self.age = age
# the first parameter at the __init__ method must be self, then the attributes and like that at any other defined methods
# the __str__ method is used to control what should be returned when the class object is represented as a string
# self at be the first the parameter at any defined method at the class is reference from the current instance of the class, used to access the class attribute at class methods
# to use inheritance at python:
# class Student(Person):
# class student is inherit from class Person

class Skill:
    def __init__(self, name: str, rate: int):
        self.name = name
        self.rate = rate
    def __str__(self):
        return f"{self.name}: {self.rate}/5"
    def edit_name(self):
        self.name = self.name.upper()

communication = Skill("Communication", 4)

communication.edit_name()
print(type(communication.rate))

class Person:
    num_of_persons = 0
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.num_of_persons += 1

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
person1 = Person("Hassan", 26)
print(person1)

class Student(Person):
    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"

student1 = Student("Ahmed", 15)
print(student1)
print(Person.num_of_persons)