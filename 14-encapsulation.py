class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name:str):
        self.__name = name.capitalize()

    def get_name(self):
        return self.__name
    
    def set_age(self, age:int):
        self.__age = age

    def get_age(self):
        return self.__age
    
    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}"

person1 = Person("Hassan", 26)
print(person1)
# print(person1.__name) # will give an error there is no attribute called __name 
print(person1.get_name())
person1.set_name("ahmed")
print(person1.get_name())
