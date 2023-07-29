# PYTHON OOP CONCEPTS

# CLASSES


class Student:
    # the __init__() function assigns values to object properties(this code is executed when the code is first run as the class is being initialized)
    def __init__(self, name, regno, age, course, year):
        self.name = name
        self.regno = regno
        self.age = age
        self.course = course
        self.year = year

    # Is used to return string values of the object
    # def __str__(self):
    #     return f"{self.name} \n {self.regno} \n {self.age} \n {self.course} \n {self.year}"

    def update_age(self, age):
        self.age = age

    def update_age(self, year):
        self.age = year

    def display(self):
        output = self.name + "\n" + self.regno + "\n{}\n" + self.course + "\n{}"
        print(output.format(self.age, self.year))


# creating student object
std_1 = Student("Arube Joshua", "21/U/1102", 21, "BSSE", 2)
# std_1.display()

std_2 = Student("Mike", "21/U/30402/PS", 23, "BIST", 3)
std_2.update_age(22)
# print(std_2.age)


# Exercise
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.142 * self.radius**2

    def calculate_circumfirance(self):
        return 2 * 3.142 * self.radius


circle_1 = Circle(5)
# print(circle_1.calculate_area())
# print(circle_1.calculate_circumfirance())


# Excercise 2
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calc_bonus(self):
        perc = 15 / 100
        bonus = perc * self.salary
        return bonus


emp1 = Employee("Mike", 150000)
print(emp1.name, emp1.calc_bonus())

emp2 = Employee("Dawn", 230000)
print(emp1.name, emp2.calc_bonus())


# ENCAPSULATION
# Example
class MyClass:
    def __init__(self):
        self.public_var = 10
        self._protected_var = 20
        self.__private_var = 30

    def public_method(self):
        print("This is a public method.")

    def _protected_method(self):
        print("This is a protected method.")

    def __private_method(self):
        print("This is a private method.")


my_object = MyClass()

# Accessing public members
print(my_object.public_var)  # Output: 10
my_object.public_method()  # Output: This is a public method.

# Accessing protected members
print(my_object._protected_var)  # Output: 20
my_object._protected_method()  # Output: This is a protected method.

# Accessing private members (name mangling is applied)
print(my_object._MyClass__private_var)  # Output: 30
my_object._MyClass__private_method()  # Output: This is a private method.


# Exercise
class TemperatureConverter:
    def __init__(self, celsius):
        self._celsius = celsius

    # def celsius(self):
    #     return self._celsius

    # def celsius(self, value):
    #     self._celsius = value

    def convert(self):
        return (self._celsius * 9 / 5) + 32


temperature = TemperatureConverter(37)
# print(temperature.celsius())  # Output: 37
# print(temperature.fahrenheit())  # Output: 98.6

temperature._celsius = 25
print(temperature.convert())  # Output: 77.0
