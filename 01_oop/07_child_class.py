class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person class was created")

    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):
    pass

class Teacher(Person):
    pass

person1 = Person("Mike", "Williams", 38)
person1.intro()

student1 = Student("Dale", "Pete", 12)
student1.intro()

teacher1 = Teacher("Vince", "Dixon", 23)
teacher1.intro()