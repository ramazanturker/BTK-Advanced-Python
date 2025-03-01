# The function that squares numbers in the interval (1 - ∞)

# def generate_number():
#     number = 0

#     while True:
#         yield number ** 2
#         number += 1

# generator = generate_number()

# print(next(generator))
# print(next(generator))
# print(next(generator))

# for i in generator:
#     print(i)

# ------------------------------------------------------------

# Generate fibonacci series with both normal and generator function

def fibonacci_list(max):
    numbers = []

    a, b = 0, 1

    while len(numbers) <= max:
        numbers.append(b)
        a, b = b, a + b

    return numbers

# print(fibonacci_list(90))

def fibonacci_generator(max):
    a, b = 0, 1
    count = 0

    while count <= max:
        a, b = b, a + b
        yield b
        count += 1

# for i in fibonacci_generator(90):
#    print(i)

import sys

listing = [i for i in range(10000)]
print(sys.getsizeof(listing))


generator = (i for i in range(10000))
print(sys.getsizeof(generator))

import time

list_start_time = time.time()
sum([i for i in range(9000000)])
list_stop = time.time() - list_start_time

generator_start_time = time.time()
sum((i for i in range(9000000)))
generator_stop = time.time() - generator_start_time

print(list_stop)
print(generator_stop)