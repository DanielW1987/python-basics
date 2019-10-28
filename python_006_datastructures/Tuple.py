"""
A Tuple is like a list but cannot be modified
A Tuple has all non-modifying methods that List also has
"""
# declaring an empty tuple
t = ()
assert t == ()

# declaring an empty typed tuple
t: tuple = ()
assert t == ()

# declaring a tuple with values
t = (10, 20, 30, 40, 50)
assert t == (10, 20, 30, 40, 50)

# tuple with single value
t = (10,)
assert t == (10,)

# converting from list
lst = [100, 200, 300, 400, 500]
t = tuple(lst)
assert type(t) == tuple
