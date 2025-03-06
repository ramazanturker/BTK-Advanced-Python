import threading
import time

def calculate_square(numbers):
    print("calculating the squares of numbers")

    for number in numbers:
        time.sleep(0.3)
        print("square: ", number * number)

def calculate_cube(numbers):
    for number in numbers:
        time.sleep(0.3)
        print("cube: ", number * number * number)

numbers = [3, 5, 8, 9, 5, 25]

t = time.time()

# calculate_square(numbers)
# calculate_cube(numbers)

thread1 = threading.Thread(target=calculate_square, args=(numbers,))
thread2 = threading.Thread(target=calculate_cube, args=(numbers,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("process done: ", time.time() - t)