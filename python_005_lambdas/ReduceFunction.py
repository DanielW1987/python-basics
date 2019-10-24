from functools import reduce

lst: list = [5, 10, 15, 20]
result = reduce(lambda x, y: x + y, lst)
assert result == 50
