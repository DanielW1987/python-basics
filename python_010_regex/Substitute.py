import re

# replacing a given pattern within string with a new string
text: str = "Hello World"
result = re.sub(r'W\w\w\w\w', "You", text)

assert result == "Hello You"
