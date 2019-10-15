# character at
s = "Hello, World!"
chartAt9 = s[9]
assert chartAt9 == "r"

# string length
assert len("Hello World") == 11
assert "Hello World".__len__() == 11

# slicing / substring
s = "Lorem ipsum"
assert s[0:5]   == "Lorem"
assert s[4:]    == "m ipsum"
assert s[:7]    == "Lorem i"
assert s[-3:-1] == "su"
assert s[0:9:2] == "Lrmis"

# reversing a string with slicing
assert s[::-1] == "muspi meroL"

# stripping spaces
s = "      Hello World      "
assert s.strip()  == "Hello World"
assert s.lstrip() == "Hello World      "
assert s.rstrip() == "      Hello World"

# finding a substring
s = "Hello World"
assert s.find("Wo") == 6
assert s.find("o", 5, len(s) - 1) == 7
assert s.find("z") == -1

# counting a substring
s = "Hello World"
assert s.count("o") == 2

# replacing a substring or character
s = "Hello World"
assert s.replace("H", "B") == "Bello World"

# upper(), lower(), title()
s = "Python is awesome"
assert s.upper() == "PYTHON IS AWESOME"
assert s.lower() == "python is awesome"
assert s.title() == "Python Is Awesome"

# string repetition
assert "=" * 10 == "=========="
