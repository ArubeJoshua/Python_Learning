# DAY 6
# Advanced Topics in Python
"""
 -Regular Expressions
 -Generators and iterators
 -Decorators
 -context Managers
 -Multithreading and multiprocessing
"""

"""import re

#Example using match()
txt = "Hello, my name is Joshua. I am a programmer with 3 years exp hello"

# match = re.search(r"^\w*",txt)
match = re.search(r"He..o",txt)
if match:
    print("match found:",match.group())
    
email = input("Enter your email: ")
pattern = r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"

val_email = re.search(pattern, email)
if val_email:
    print("Email valid")
else:
    print("Email invalid")
    
    
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)

print(x)
print("The first white-space character is located in position:", x.start())




#Generators(uses yield as a key word)
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# Using the generator
my_generator = even_numbers(10)

for num in my_generator:
    print(num)
    
#Iterator
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Using the iterator
my_list = [1, 2, 3, 4, 5]
my_iter = MyIterator(my_list)

for num in my_iter:
    print(num)
    



#Combined Examples
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.generator = fibonacci_generator()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        value = next(self.generator)
        if value > self.limit:
            raise StopIteration
        return value

# Using the iterator
fibonacci_iter = FibonacciIterator(100)
for num in fibonacci_iter:
    print(num)




#Decorators
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return "Hello, World!"

print(say_hello())"""


# contextManager
class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


# Using the context manager
with FileContextManager("example.txt", "w") as file:
    file.write("Hello, World!")


"""#multithreading and Multiprocessing
import threading
import time

def task():
    print("Thread started")
    time.sleep(2)  # Simulating some work
    print("Thread finished")

# Create and start a new thread
thread = threading.Thread(target=task)
thread.start()

# Continue executing main thread
print("Main thread")

# Wait for the thread to finish
thread.join()

print("Program completed")



#multiprocessing
import multiprocessing

def task():
    print("Process started")
    # Perform some work here
    print("Process finished")

if __name__ == '__main__':
    # Create and start a new process
    process = multiprocessing.Process(target=task)
    process.start()

    # Continue executing main process
    print("Main process")

    # Wait for the process to finish
    process.join()

    print("Program completed")"""
