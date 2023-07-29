# Control Flow

# Conditional Statements(if, elif, else)

# if statement
age = 21
if age > 18:
    print("You have been given access for your above 18")

# if, else satatement
check = True
if check == True:
    print("your condition is true")
else:
    print("Condition is false")

# if, elif, else statements

# Example1
if age < 18:
    print("You are under age")
elif age >= 18 and age <= 65:
    print("Your are an adult")
else:
    print("Your are a senior adult")


# Loops(for, while)

# for loop using to iterarte through a list and tuple
list1 = ["apples", "mango", "banana", "orange"]
for x in list1:
    print(x)

tuple1 = (3, 1, 6, 7, 8)
for y in tuple1:
    print(y)

# while loop
k = int(0)
while k < 5:
    print(k)
    k += 1

for x in list1:
    if x == "mango":
        break
    print(x)


# using the continue statement
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lit = list([])
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    lit.append(num)

print(lit)


# Exception handling(try, except, finally)
try:
    print(x)
except NameError:
    print("x is not defined")
else:
    print("No exception occurred")
finally:
    print("Code execution complete")


# Exercise one(Asking students about there mental health


print("Welcome to mental health assessment")
name = str(input("Please enter your name: "))
mental_health_scale = int(input("On a scale of 1 to 10, how is your mental health? "))

assessment_responses = {
    "low": name + " Sorry about that, you need immediate assistance.",
    "fair": name
    + " Your condition is fair, but it is recommended to seek medical assistance.",
    "good": name + " Your mental health is good.",
}

if 1 <= mental_health_scale <= 10:
    if mental_health_scale < 4:
        response = assessment_responses["low"]
    elif 4 <= mental_health_scale <= 7:
        response = assessment_responses["fair"]
    else:
        response = assessment_responses["good"]
    print(response)
else:
    print("Invalid input. Please enter a number between 1 and 10.")
