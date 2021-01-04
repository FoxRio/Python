class Person:
    numberOfPeople = 0
    def __init__(self, name):
        self.name = name


    @classmethod
    def number_of_people(cls):
        return cls.numberOfPeople


    @classmethod
    def add_person(cls):
        cls.numberOfPeople += 1


p1 = Person("Tim")
p2 = Person("Garry")
for i in range(9):
    p1.add_person()

print(Person.number_of_people())


class Math:
    @staticmethod
    def add_five(x):
        return x + 5


print(Math.add_five(10))


