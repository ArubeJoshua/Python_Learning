import threading
import multiprocessing
import time


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
