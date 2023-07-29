# Exception Handling

# Exception handling is a mechanism in programming languages that allows you to handle and respond to errors or exceptional situations that may occur during the execution of a program.

# When an error or exceptional situation occurs, it typically disrupts the normal flow of the program and may cause it to terminate abruptly. Exception handling provides a way to gracefully handle these situations, allowing the program to recover, take appropriate actions, or provide meaningful error messages to the us


try:
    # Code that may raise exceptions
    x = 10 / 0  # Division by zero
    name = "John"
    print(name[5])  # Index out of range
    file = open("nonexistent.txt", "r")  # File not found
except ZeroDivisionError:
    print("Error: Division by zero")
except IndexError:
    print("Error: Index out of range")
except FileNotFoundError:
    print("Error: File not found")
except Exception as e:  # used to catch all exceptions
    print("An unexpected error occurred:", str(e))
else:
    print("No exceptions occurred.")
finally:
    print("Finally block executed.")


"""try:
    # Some code that may raise a NameError
    print(variable)  # Assuming 'variable' is not defined
except NameError:
    print("An error occurred: NameError - variable is not defined")
else:
    print("No errors occurred. The variable is defined.")
finally:
    print("This will always execute, regardless of whether an exception occurred.")"""


# File handling

# Opening a file and reading from the file using the r mode pointer is placed at the beginning of the file
try:
    file = open("file1.txt", "r")
    # File operations
    content = file.read()
    file.close()
    print(content)
except IOError:
    print("An error occurred while opening the file.")

# Using r+ allows reading and writing but pointer is placed at beginning of file and overrides existing data
try:
    file = open("file2.txt", "r+")
    cont2 = file.read()
    file.write("\nThis is a statement")
    # File operations
    file.close()
except IOError:
    print("An error occurred while opening the file.")

# Using w (Opens files for writing and clears file data before writing and if file is not there it creates it)
try:
    file = open("file3.txt", "w")
    file.write("Hello, World!")
    file.close()
except IOError:
    print("An error occurred while writing to the file.")

# Using w+ (Reads and writes data)
try:
    file = open("file4.txt", "w+")
    cont3 = file.readlines()  # stores lines in the file as a list
    for line in cont3:
        print(line)

    file.write("Hello, World!")
    file.close()
except IOError:
    print("An error occurred while writing to the file.")


# Using a(appends )
try:
    file = open("file5.txt", "a")
    file.write("\nThis is a new line.")
    file.close()
except IOError:
    print("An error occurred while appending to the file.")

# Using a+(appends and reads from the file)
try:
    file = open("file6.txt", "a+")
    cont4 = file.read()
    file.close()

    print(cont4)
except IOError:
    print("An error occurred while appending to the file.")


# Using the os module
import os


# File Existence Check (os.path.exists()):
# This function checks whether a file or directory exists at the specified path. It returns True if the path exists and False otherwise

file_path = "myfile.txt"
if os.path.exists(file_path):
    print("The file exists.")
else:
    print("The file does not exist.")


"""File/Directory Creation (os.mkdir() and os.makedirs()):
These functions are used to create directories. os.mkdir() creates a single directory, while os.makedirs() creates multiple directories recursively."""

"""dir_name = "my_directory"
os.mkdir(dir_name)  # Create a single directory

# Create multiple directories recursively
nested_dir = "parent_dir/child_dir"
os.makedirs(nested_dir)"""

"""File Renaming (os.rename()):
The os.rename() function is used to rename a file or directory. It takes two arguments: the current path and the new path"""

"""current_path = "old_name.txt"
new_path = "new_name.txt"
os.rename(current_path, new_path)
"""
"""File Deletion (os.remove()):
The os.remove() function is used to delete a file."""

"""file_path = "file_to_delete.txt"
os.remove(file_path)"""

"""Directory Deletion (os.rmdir() and os.removedirs()):
These functions are used to remove directories. os.rmdir() removes a single empty directory, while os.removedirs() removes multiple directories recursively"""

"""dir_to_delete = "directory_to_delete"
os.rmdir(dir_to_delete)  # Remove a single empty directory

# Remove multiple directories recursively
nested_dir = "parent_dir/child_dir"
os.removedirs(nested_dir)"""
