class Student:

    major = "Computer Science"
    count: int = 0

    def __init__(self, roll_number: int, name: str):
        self.roll_number = roll_number
        self.name = name
        Student.count += 1

    @staticmethod
    def display_object_count():
        print(Student.count)


s1 = Student(1, "John")
s2 = Student(2, "Bill")

assert s1.major == "Computer Science"
assert s2.major == "Computer Science"
assert Student.major == "Computer Science"
assert Student.count == 2

Student.display_object_count()