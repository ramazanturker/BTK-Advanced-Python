class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person class was created")

    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):
    def __init__(self, name, surname, age, number):
        # Person.__init__(self, name, surname, age)
        super().__init__(name, surname, age)
        self.number = number
        print("student class was created")

    def study(self):
        print(f"{self.name} studying")

    def intro(self):
        print(self.name, self.surname, self.age, self.number)

class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        super().__init__(name, surname, age)
        self.branch = branch
        print("teacher class was created")
    
    def teach(self):
        print(f"{self.name} {self.branch} teaching")

person1 = Person("Mike", "Williams", 38)
person1.intro()

student1 = Student("Dale", "Pete", 12, 678)
student1.intro()
# student1.study()
# print(student1.number)

teacher1 = Teacher("Vince", "Dixon", 23, "Chemistry")
teacher1.intro()
# print(teacher1.branch)
# teacher1.teach()