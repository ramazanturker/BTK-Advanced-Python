# class Test():
#    pass

# class BaseClass():
#     def show(self):
#         return "hello"

# def add_attribute(self):
#     self.number2 = 12

# Test = type("Test", (BaseClass,), {"number1": 7, "add_attribute": add_attribute})
# test1 = Test()

# result = Test()
# result = Test
# result = type(Test)
# result = type(2)
# result = type(int)
# result = type("2")
# result = type(str)
# result = test1.show()
# result = test1.number1
# test1.add_attribute()
# result = test1.number2

# print(result)

class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        a = {}

        for name, val in attrs.items():
            if name.startswith("_"):
                a[name] = val
            else:
                a[name.upper()] = val

        return type(class_name, bases, a)
    
class Person(metaclass = Meta):
    x = 5
    y = 10
    _age = 28

    def hello(self):
        print("hello guys")

person1 = Person()

person1.X

result = person1.X
result = person1.Y
result = person1._age

print(result)