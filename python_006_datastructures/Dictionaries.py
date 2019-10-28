# declaring an empty dictionary
d = {}
assert d == {}

# declaring an empty typed dictionary
d: dict = {}
assert d == {}

# declaring an dictionary with values
cities: dict = {"Munich": 1_500_000, "Berlin": 3_000_000}
assert cities == {"Munich": 1_500_000, "Berlin": 3_000_000}

# retrieving item
cities: dict = {"Munich": 1_500_000, "Berlin": 3_000_000}
assert cities["Munich"] == 1_500_000
assert cities["Berlin"] == 3_000_000

# adding an item
cities: dict = {"Munich": 1_500_000, "Berlin": 3_000_000}
cities["Cologne"] = 2_000_000
assert cities == {"Munich": 1_500_000, "Berlin": 3_000_000, "Cologne": 2_000_000}

# removing an item
cities: dict = {"Munich": 1_500_000, "Berlin": 3_000_000}
del(cities["Berlin"])
assert cities == {"Munich": 1_500_000}

# contains / contains not
cities: dict = {"Munich": 1_500_000, "Berlin": 3_000_000}
if "Hamburg" not in cities:
    cities["Hamburg"] = 1_000_000

assert cities == {"Munich": 1_500_000, "Berlin": 3_000_000, "Hamburg": 1_000_000}

# iterating dictionaries
cities: dict = {"Munich": 1_500_000, "Berlin": 3_000_000}
for entry in cities:
    print(entry)  # prints the keys
    print(cities[entry])  # prints the values

for city, citizen in cities.items():
    print(city + " | " + str(citizen))

for key in cities.keys():
    print(key)

for value in cities.values():
    print(value)
