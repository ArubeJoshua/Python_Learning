# Inhertance
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def action(self, action):
        return self.name + " is " + self.type + " and it is " + action


# Creating a class cat which inherits all the attributes and methods of animal


class Cat(Animal):
    pass


obj_1 = Cat("cat", "domestic")
print(obj_1.action("meowing"))

# When you define the init function in the sub class


class Dog(Animal):
    def __init__(self, name, type, breed):
        super().__init__(name, type)
        self.breed = breed

    def breed_d(self):
        print(self.breed)


obj_2 = Dog("dog", "domestic", "German Shepherd")
obj_2.action("barking")
obj_2.breed_d()


# Exercise
# Polyomorphism
import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Method overriding
        return math.pi * self.radius**2

    def perimeter(self):  # Method overriding
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):  # Method overriding
        return self.length * self.width

    def perimeter(self):  # Method overriding
        return 2 * (self.length + self.width)


def shape_area(shape):
    return shape.area()


def shape_perimeter(shape):
    return shape.perimeter()


# Example usage:
circle = Circle(5)
rectangle = Rectangle(4, 6)

# print("Circle area:", circle.area())
# print("Circle perimeter:", circle.perimeter())

# print("Rectangle area:", rectangle.area())
# print("Rectangle perimeter:", rectangle.perimeter())

print(shape_area(circle))
print(shape_perimeter(circle))
print(shape_area(rectangle))
print(shape_perimeter(rectangle))


class Water:
    def __init__(self, water_type):
        self.water_type = water_type


# multiple Inheritance
class Crocodile(Animal, Water):
    def __init__(self, name, animal_type, water_type):
        Animal.__init__(self, name, animal_type)
        Water.__init__(self, water_type)


crocodile = Crocodile("Croc", "reptile", "freshwater")
print(crocodile.action("swimming"))
print("Water type:", crocodile.water_type)


# Polymorphism with overloading
# class MathOperations:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c

# math_ops = MathOperations()
# print(math_ops.add(2, 3))       # Output: 5
# print(math_ops.add(2, 3, 4))    # Output: 9


# using a loop
class MathOperations:
    def add(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c


math_ops = MathOperations()
print(math_ops.add(2, 3))  # Output: 5
print(math_ops.add(2, 3, 4))  # Output: 9


# Abstraction
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_details(self):
        pass


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_details(self):
        print(f"Employee: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_details(self):
        print(f"Student: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")


# Creating objects of concrete classes
employee = Employee("John Doe", 30, "EMP001")
student = Student("Alice Smith", 20, "STU001")

# Accessing the abstract interface
employee.display_details()
print()  # Print a blank line
student.display_details()


# Exercise 2
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Create objects of concrete classes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Access the abstract interface
print("Area of Circle:", circle.area())  # Output: Area of Circle: 78.53981633974483
print(
    "Perimeter of Circle:", circle.perimeter()
)  # Output: Perimeter of Circle: 31.41592653589793
print("Area of Rectangle:", rectangle.area())  # Output: Area of Rectangle: 24
print(
    "Perimeter of Rectangle:", rectangle.perimeter()
)  # Output: Perimeter of Rectangle: 20
