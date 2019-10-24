# Generators are functions that return a sequence of values


# create a custom generator
def custom_generator(x, y):
    while x < y:
        yield x
        x *= 2


result = custom_generator(1, 100)
for i in result:
    print(i)
