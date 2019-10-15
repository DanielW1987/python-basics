# declaring an empty set
s = set() # {} is an empty dict
assert s == set()

# declaring an empty set tuple
s: set = set() # {} is an empty dict
assert s == set()

# declaring a set with values
s = {10, 20, 30, 40, 50}
assert s == {10, 20, 30, 40, 50}

# set doesn't allow duplicates
s = {10, 10, 20, 20, 30, 30}
assert s == {10, 20, 30}

# adding an element
s = {10, 20, 30}
s.add(40)
assert s == {10, 20, 30, 40}

# removing an element
s = {10, 20, 30}
s.remove(10)
assert s == {20, 30}

# frozen set
s = {10, 20, 30}
f = frozenset(s) # f is immutable from now on
