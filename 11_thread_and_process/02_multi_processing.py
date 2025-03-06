import time
import multiprocessing

def calculate_square(numbers, listing):
    for index, value in enumerate(numbers):
        time.sleep(0.3)
        # print("square: ", number * number)
        listing[index] = value * value

def calculate_cube(numbers, listing):
    for index, value in enumerate(numbers):
        time.sleep(0.3)
        # print("cube: ", number * number * number)
        listing[index] = value * value * value

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 12, 56, 126, 256, 24555]

    t = time.time()

    list_square = multiprocessing.Array('i', 9)
    list_cube = multiprocessing.Array('i', 9)

    processing1 = multiprocessing.Process(target=calculate_square, args=(arr, list_square,))
    processing2 = multiprocessing.Process(target=calculate_cube, args=(arr, list_cube,))

    processing1.start()
    processing2.start()

    processing1.join()
    processing2.join()

    print(time.time() - t)

    print(list_square[:])
    print(list_cube[:])