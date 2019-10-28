class Programmer:

    def __init__(self, name: str):
        self.name: str = name
        self.salary = 0
        self.technologies = []

    def get_name(self):
        return self.name

    def set_salary(self, salary: int):
        self.salary: int = salary

    def get_salary(self):
        return self.salary

    def set_technologies(self, technologies: list):
        self.technologies: list = technologies

    def get_technologies(self):
        return self.technologies


p1 = Programmer("John Doe")
p1.set_salary(60000)
p1.set_technologies(["Java", "Groovy", "Python"])

assert p1.get_name() == "John Doe"
assert p1.get_salary() == 60000
assert p1.get_technologies() == ["Java", "Groovy", "Python"]
