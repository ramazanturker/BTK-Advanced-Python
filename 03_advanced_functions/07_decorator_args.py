# def dec_hello(count):
#     def hello(fn):
#         def inner(name):
#             for _ in range(count):
#                 fn(name)
#         return inner
#     return hello

# @dec_hello(count = 2)
# def good_morning(name):
#     print(f"good morning, my name is {name}")

# @dec_hello(count = 3)
# def good_day(name):
#     print(f"good day, my name is {name}")


# good_morning("jane")
# good_day("maria")

# -------------------------------------------------

import time

def dec_speed_test(count):
    def speed_test(fn):
        def inner(*args, **kwargs):
            start_time = time.perf_counter()
            print(f"{fn.__name__} running method")
            for _ in range(count):
                result = fn(*args, **kwargs)
                end_time = time.perf_counter()
                run_time = end_time - start_time
                print(f"elapsed time : {run_time}")
            return result
        return inner
    return speed_test

@dec_speed_test(count = 2)
def sum_gen():
    return sum((x for x in range(10000000)))

@dec_speed_test(count = 3)
def sum_list():
    return sum([x for x in range(10000000)])

print(sum_gen())
print(sum_list())