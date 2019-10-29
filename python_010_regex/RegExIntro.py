import re

text: str = "Take up one idea. One idea at a time"

# searches for a string that starts with 'o' followed by two alphanumerical characters
result = re.search(r'o\w\w', text)
assert result.group() == "one"

# find all substrings that matches the given pattern
find_result: list = re.findall(r'id\w\w', text)
assert find_result == ["idea", "idea"]

# returns true if the given string starts with the given pattern, false otherwise
match_result = re.match(r'T\w\we', text)
assert match_result.group() == "Take"
