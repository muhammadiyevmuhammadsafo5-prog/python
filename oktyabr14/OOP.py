# OOP - Object Oriented Programming(Obektga yo'naltirilgan dasturlash)
# snake case
# def python_programming():
#   pass
# camel case 
# class PythonProgramming:
#   pass


# class Animal:
#     def __init__(self, name: str):
#         self.name = name

#     def bark(self):
#         print("Waw waaaaw")

# animal1 = Animal("Dog")
# animal2 = Animal("Cat")

# animal1.bark()

class Car:
    def __init__(self, name: str, color: str, year: int):
        self.name = name
        self.color = color
        self.year = year
        self.age = 2026 - year

    def say_name(self):
        print("My name is", self.name)

    def say_age(self):
        print("I am", self.age, "years old")

    def honk(self):
        print("Beep beeeeeeeeeeeep")

car1 = Car("Cobalt", "White", 2020)
car2 = Car("Malibun 2", "Blue", 2024)

car1.say_age()
car2.say_name()