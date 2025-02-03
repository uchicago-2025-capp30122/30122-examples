from datetime import date


class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def age(self):
        today = date.today()
        # calculate age
        age = (
            today.year
            - self.birth_date.year
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )
        return int(age)

    def __str__(self):
        return f"{self.name} is {self.age()}"


# this class inherits from Person
#   a Student is-a Person
class Student(Person):
    def __init__(self, name, birth_date):
        # this call to super() calls Person.__init__
        super().__init__(name, birth_date)
        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course] = grade


# this class inherits from Student
#   an Alum is-a Student, which is in turn a Person
class Alum(Student):
    def __init__(self, name, birth_date, graduation_year):
        # this call to super() calls Student.__init__
        super().__init__(name, birth_date)
        self.graduation_year = graduation_year

    def add_grade(self, course, grade):
        # this method is overriden and will not call Student.add_grade
        raise Exception("can't add grades to alumni")

    def __str__(self):
        return f"{self.name} ({self.graduation_year}) is {self.age()}"


# first example
p = Person("Paul", birth_date=date(1960, 10, 10))
s = Student("Sarah", birth_date=date(2000, 4, 1))
a = Alum("Akbar", birth_date=date(1990, 8, 12), graduation_year=2023)

print(p, type(p))
print(s, type(s))
print(a, type(a))


# second example
p = Person("Paul", birth_date=date(1960, 10, 10))
s = Student("Sarah", birth_date=date(2000, 4, 1))
a = Alum("Akbar", birth_date=date(1990, 8, 12), graduation_year=2023)

types = [Person, Student, Alum]
for t in types:
    if isinstance(p, t):
        print(p.name, "is a", t.__name__)
    if isinstance(s, t):
        print(s.name, "is a", t.__name__)
    if isinstance(a, t):
        print(a.name, "is a", t.__name__)
