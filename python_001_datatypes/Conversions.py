# int() converts a float or a string to an int
s = "5"
f = 3.141

i1 = int(s)
i2 = int(f)

print("conversion to int: ", i1, i2)


# float() converts an int or a string to a float
i = 9
s = "5.4"

f1 = float(i)
f2 = float(s)

print("conversion to float: ", f1, f2)


# str() converts a value to a string
i = 9
f = 3.14
b = False

s1 = str(i)
s2 = str(f)
s3 = str(b)

print("conversion to string: ", s1, s2, s3)


# bin() converts an int to a binary value
i = 846

b = bin(i)

print(b)


# hex() converts an int to a hex value
i = 846

h = hex(i)

print(h)


# oct() converts an int to an octal value
i = 846

o = oct(i)

print(o)
