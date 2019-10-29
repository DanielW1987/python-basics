import re

# * => Zero or more times
text: str = "Gks"
assert re.match(r'Ge*ks', text)

# + => One or more times
text: str = "Gks"
assert re.match(r'Ge+ks', text) is None

# ? => Once or none
text: str = "Geeks"
assert re.match(r'Ge?ks', text) is None

# {n} => Exactly n times
text: str = "Geeks"
assert re.match(r'Ge{2}ks', text)

# {n, } => Three or more times
text: str = "Geks"
assert re.match(r'Ge{2,}ks', text) is None

# {n, m} => n to m times
text: str = "Geeeks"
assert re.match(r'Ge{1,2}ks', text) is None
