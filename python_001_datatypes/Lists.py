# declaring an empty list
emptyList = []
assert emptyList.__len__() == 0

# declaring a list with type
emptyList: list = []
assert emptyList.__len__() == 0

# declaring a list
products = ["Apple", "Bananas", "Oranges"]
assert products == ["Apple", "Bananas", "Oranges"]

# declaring a list of any type
anyDataType = [1, 3.14, True, "Hello"]
assert anyDataType == [1, 3.14, True, "Hello"]

# adding an item
products = ["Apple", "Bananas", "Oranges"]
products.append("Cherry")
assert products == ["Apple", "Bananas", "Oranges", "Cherry"]

# removing an item by value
products = ["Apple", "Bananas", "Oranges", "Cherry"]
products.remove("Bananas")
assert products == ["Apple", "Oranges", "Cherry"]

# removing an item by index
products = ["Apple", "Bananas", "Oranges", "Cherry"]
del(products[1])
assert products == ["Apple", "Oranges", "Cherry"]

# retrieving items
products = ["Apple", "Bananas", "Oranges", "Cherry"]
assert products[0]   == "Apple"  # first element
assert products[-1]  == "Cherry" # last element
assert products[1:3] == ["Bananas", "Oranges"]

# size of list
products = ["Apple", "Bananas", "Oranges", "Cherry"]
assert len(products) == 4
assert products.__len__() == 4

# clearing a list
products = ["Apple", "Bananas", "Oranges", "Cherry"]
products.clear()
assert products == []

# max() / min()
products = ["Apple", "Bananas", "Oranges", "Cherry"]
assert max(products) == "Oranges"
assert min(products) == "Apple"

# inserting an element
products = ["Apple", "Bananas", "Oranges", "Cherry"]
products.insert(1, "Papaya")
assert products == ["Apple", "Papaya", "Bananas", "Oranges", "Cherry"]

# sorting
products = ["Apple", "Bananas", "Oranges", "Cherry"]
products.sort()
assert products == ["Apple", "Bananas", "Cherry", "Oranges"]
products.sort(reverse=True)
assert products == ["Oranges", "Cherry", "Bananas", "Apple"]

# list repetition
products = ["Apple", "Bananas", "Oranges", "Cherry"]
assert products * 2 == ["Apple", "Bananas", "Oranges", "Cherry", "Apple", "Bananas", "Oranges", "Cherry"]

# string to list
sentence = "I'm a sentence of a few words."
wordList = sentence.split(" ")
assert wordList == ["I'm", "a", "sentence", "of", "a", "few", "words."]

# list to string
wordList = ["I'm", "a", "sentence", "of", "a", "few", "words."]
sentence = " ".join(wordList)
assert sentence == "I'm a sentence of a few words."

# printing and iterating a list
products = ["Apple", "Bananas", "Oranges", "Cherry"]
print(products)
for item in products:
    print(item)
