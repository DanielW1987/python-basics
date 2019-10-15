# declaring a range from zero to five
r = range(5)
assert r == range(5)

# declaring a typed range from zero to five
r: range = range(0, 5)
assert r == range(5)

# looping
for item in range(1, 10):
    print(item)

# looping with steps
for item in range(100, 95, -1):
    print(item)
