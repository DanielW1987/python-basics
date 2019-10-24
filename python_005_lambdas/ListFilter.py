# filter a list
lst: list = [10, 2, 33, 45, 89, 2]
lst = list(filter(lambda x: x % 2 == 0, lst)) # filter() returns an iterator
assert lst == [10, 2, 2]
