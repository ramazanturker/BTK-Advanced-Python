def hello(fn):
    def inner(name):
        print("welcome")
        fn(name)
        print("see you later")

    return inner

@hello
def good_morning(name):
    print(f"good morning, my name is {name}")

@hello
def good_day(name):
    print(f"good day, my name is {name}")

# good_morning = hello(good_morning)
# good_morning()

# good_day = hello(good_day)
# good_day()

good_morning("jane")
good_day("maria")