# Basic operators and Expresstions(input and output)


# Arithmetic operators
num1 = 10 + 5  # Addition operator (+)
num2 = 15 - 7  # Subtraction operator (-)
num3 = 6 * 4  # Multiplication operator (*)
num4 = 20 / 3  # Division operator (/)
num5 = 10 // 3  # Floor division operator (//)
num6 = 20 % 7  # Modulo operator (%)
num7 = 2**4  # Exponentiation operator (**)
print("Results for Arithmetic operators")
print(num1, num2, num3, num4, num5, num6, num7)


# Comparison operators
result1 = num1 == num2  # Equal to operator (==)
result2 = num3 != num4  # Not equal to operator (!=)
result3 = num5 > num6  # Greater than operator (>)
result4 = num6 < num7  # Less than operator (<)
result5 = num1 >= num3  # Greater than or equal to operator (>=)
result6 = num2 <= num4  # Less than or equal to operator (<=)
print("Results for comparison operators")
print(result1, result2, result3, result4, result5, result6)


# Assignment operators
x = 10  # Assignment operator (=)
x += 5  # Addition assignment operator (+=)
x -= 3  # Subtraction assignment operator (-=)
x *= 2  # Multiplication assignment operator (*=)
x /= 4  # Division assignment operator (/=)
x %= 3  # Modulo assignment operator (%=)
x **= 2  # Exponentiation assignment operator (**=)
print("Results for Assignment operators")
print(x)


# Logical operators
is_valid = True
has_permission = False

result7 = is_valid and has_permission  # Logical AND operator (and)
result8 = is_valid or has_permission  # Logical OR operator (or)
result9 = not is_valid  # Logical NOT operator (not)
print("Results for Logical operators")
print(result7, result8, result9)

# Membership operators
list1 = [1, 2, 3, 4, 5]

result10 = 3 in list1  # Membership operator (in)
result11 = 6 not in list1  # Membership operator (not in)
print("Results for Membership operators")
print(result10, result11)

# Identity operators
a = 10
b = 10

result12 = a is b  # Identity operator (is)
result13 = a is not b  # Identity operator (is not)
print("Results for Identity operators")
print(result12, result13)


# Bitwise Operators
print("Results for Bitwise operators")
num1 = 12  # binary: 1100
num2 = 7  # binary: 0111

result_and = num1 & num2  # binary: 0100 (decimal: 4)
print("Bitwise AND result:", result_and)

# Bitwise OR example
result_or = num1 | num2  # binary: 1111 (decimal: 15)
print("Bitwise OR result:", result_or)

# Bitwise XOR example
result_xor = num1 ^ num2  # binary: 1011 (decimal: 11)
print("Bitwise XOR result:", result_xor)

# Bitwise NOT example
num = 42  # binary: 00101010
result_not = ~num  # binary: 11010101 (decimal: -43)
print("Bitwise NOT result:", result_not)

# Bitwise left shift example
num = 5  # binary: 00000101
shifted_left = num << 2  # binary: 00010100 (decimal: 20)
print("Bitwise left shift result:", shifted_left)

# Bitwise right shift example
num = 16  # binary: 00010000
shifted_right = num >> 3  # binary: 00000010 (decimal: 2)
print("Bitwise right shift result:", shifted_right)


# EXERCISE
