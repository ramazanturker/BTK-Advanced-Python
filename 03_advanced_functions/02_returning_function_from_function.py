# def exponentiation(base):
#     def inner(power):
#         return base ** power
    
#     return inner

# result = exponentiation(2)(3)

# fn = exponentiation(2)
# result = fn(4)
# print(result)

# -----------------------------------------------------------

# def authorization_query(page):
#     def inner(role):
#         if role == "Admin":
#             return f"{role} role can reach {page}"
#         else:
#             return f"{role} role cannot reach {page}"

#     return inner

# authorization = authorization_query("product update page")
# result = authorization("Admin")

# print(result)

# -----------------------------------------------------------

def operation(operation_name):
    def total(*args):
        total = 0
        for i in args:
            total += i
        return total

    def multiplication(*args):
        multiplication = 1
        for i in args:
            multiplication *= i
        return multiplication
    
    if operation_name == "total":
        return total
    else:
        return multiplication

total = operation("total")
multiplication = operation("multiplication")

result = total(10, 20)
print(result)

result = multiplication(10, 20)
print(result)