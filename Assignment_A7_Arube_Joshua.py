# Part a
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


# using the manager
with FileContextManager("FILE.txt", "a+") as f:
    f.write("Done with context manager")


# Part b
import sqlite3


class SQLiteConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()


# Using the context manager
db_file = "University.db"

with SQLiteConnection(db_file) as conn:
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE Student (id INTEGER, name TEXT)")


# Part c
# Multithreading
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


# multiprocessing
import multiprocessing


def task():
    print("Process started")
    # Perform some work here
    print("Process finished")


if __name__ == "__main__":
    # Create and start a new process
    process = multiprocessing.Process(target=task)
    process.start()

    # Continue executing main process
    print("Main process")

    # Wait for the process to finish
    process.join()

    print("Program completed")


# combination


# Function to execute
def my_function(duration):
    print(f"Starting function for {duration} seconds")
    time.sleep(duration)
    print(f"Finished function for {duration} seconds")


# Using multithreading
thread1 = threading.Thread(target=my_function, args=(2,))
thread2 = threading.Thread(target=my_function, args=(4,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

if __name__ == "__main__":
    # Using multiprocessing
    process1 = multiprocessing.Process(target=my_function, args=(3,))
    process2 = multiprocessing.Process(target=my_function, args=(5,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
