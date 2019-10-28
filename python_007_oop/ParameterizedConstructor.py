class Course:

    # parameter for constructor
    def __init__(self, name: str, ratings: list):
        self.name: str = name
        self.ratings: list = ratings


c1 = Course("Python Bootcamp", [5, 5, 4, 3])
assert c1.name == "Python Bootcamp"
assert c1.ratings == [5, 5, 4, 3]
