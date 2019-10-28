# the normal way
lst = []
for x in range(1, 11):
    lst.append(x ** 3)

assert lst == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# with list comprehension
lst2 = [x ** 3 for x in range(1, 11)]
assert lst2 == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# even numbers between 1 and 20
evenNumbers = [n for n in range(1, 21) if n % 2 == 0]
assert evenNumbers == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# product of elements in two lists
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
product = [a[i] * b[i] for i in range(0, len(a))]
assert product == [6, 14, 24, 36, 50]

# common elements in a list
a = [2, 4, 6, 8]
b = [1, 2, 3, 4]
common_elements = [element for element in a if element in b]
assert common_elements == [2, 4]
