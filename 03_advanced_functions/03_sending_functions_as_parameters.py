def filter(fn, listing):
    result = []
    for item in listing:
        if fn(item):
            result.append(item)

    return result

def is_even(num):
    return num % 2 == 0

def is_positive(num):
    return num > 0

numbers = [1, 2, 3, 5, 7, 9, -5, 10]

result = filter(is_even, numbers)
print("even numbers : ", result)

result = filter(is_positive, numbers)
print("positive numbers : ", result)