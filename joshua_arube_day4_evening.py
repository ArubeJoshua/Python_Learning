# FUNCTIONS


# Defining functions
def greet():
    print("Hey there")


# calling functions
greet()


# paramters and arguments
def sum(num1, num2):
    return num1 + num2


# to pass arguments
print(sum(50, 57))


# Using pass key word
def myF():
    pass


# keyword as a parameter **kargs
def process_arguments(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Example usage
process_arguments(name="John", age=25, city="New York")


# using *args
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# default parameter value
def my_function(country="Norway"):
    print("I am from " + country)


my_function()
my_function("Brazil")


# MODULES
import module as mo

print(mo.sum(14, 1))

# printing the directory
# x = dir(mo)
# print(x)

from math import sqrt, factorial

print(sqrt(1000))
print(factorial(5))


# INPUT AND OUTPUT
def register_student():
    name = input("Enter name: ")
    regno = input("Enter regno: ")
    age = int(input("Enter age: "))

    if age < 18:
        print("Your not old enough to complete registration")
    else:
        print("Registration complete")


# Function to process user input
def process_input(value):
    return int(value) ** 2  # Square the input value


# Get multiple inputs from the user
numbers = input("Enter multiple numbers, separated by spaces: ").split()

# Use map() to process the inputs
result = list(map(process_input, numbers))

# Print the processed inputs
print("Processed inputs:", result)


# Initialize an empty list
my_list = []

# Loop to get user input and update the list
while True:
    value = input("Enter a value (or 'q' to quit): ")
    if value.lower() == "q":
        break  # Exit the loop if 'q' is entered
    my_list.append(value)  # Add the value to the list

# Print the updated list
print("Updated list:", my_list)
