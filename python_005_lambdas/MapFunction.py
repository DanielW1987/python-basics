lst: list = [5, 10, 15, 20]
lst = list(map(lambda x: x * 2, lst))
assert lst == [10, 20, 30, 40]
