# def hello(name):
#     return f"hello {name}"

# # print(hello("Jesse"))
# # print(hello)

# hi = hello

# print(hello("John"))
# print(hi("Michael"))

# del hello
# print(hi)

# # print(hello("Adam"))
# print(hi("James"))

# -----------------------------------------------------

# def outer(number):
#     def inner(number):
#         print(number)

#     inner(number)

# outer(10)

# -----------------------------------------------------

def factorial(number):

    if not isinstance(number, int):
        raise TypeError("number must be an int")

    if not number >= 0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):
        if number <= 1:
            return 1

        return number * inner_factorial(number - 1)
    
    return inner_factorial(number)

result = factorial(7)
print(result)

try:
    result = factorial(-3)
    print(result)
except Exception as e:
    print(e)

try:
    result = factorial("-3")
    print(result)
except Exception as e:
    print(e)