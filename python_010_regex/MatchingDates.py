import re

text: str = "Today is 2020-1-1. It's new year!"
result = re.findall(r'\d{4}-\d{1,2}-\d{1,2}', text)

assert result == ["2020-1-1"]
