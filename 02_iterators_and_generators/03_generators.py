def counter(max):
    number = 1

    while number <= max:
        yield number
        number += 1

generator = counter(20)

# print(generator)
# print(dir(generator))

# print(next(generator))
# print(next(generator))
# print(next(generator))

# for i in generator:
#     print(i)

# result = list(generator)

listing = (i for i in range(1, 20))

print(next(listing))
print(next(listing))