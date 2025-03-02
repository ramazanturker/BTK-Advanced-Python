def double(fn):
    def inner(*args, **kwargs):
        fn(*args, **kwargs)
        return fn(*args, **kwargs)

    return inner

@double
def hello():
    print("hello")

@double
def hi(name):
    print("hi", name)

@double
def good_day():
    return "good day"

hello()
hi("scarlet")
print(good_day())