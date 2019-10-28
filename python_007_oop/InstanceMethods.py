class Course:

    # parameter for constructor
    def __init__(self, name: str, ratings: list):
        self.name: str = name
        self.ratings: list = ratings

    def average_rating(self) -> float:
        return sum(self.ratings) / len(self.ratings)


c1 = Course("Python Bootcamp", [5, 5, 3, 3])
assert c1.name == "Python Bootcamp"
assert c1.ratings == [5, 5, 3, 3]
assert c1.average_rating() == 4
