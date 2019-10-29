import re

# splitting a string at digits
text: str = "Lorem ipsum 12 sit amet, 45 consetetur 6 sadipscing elitr, 7 sed diam"
result = re.split(r'\d+', text)

assert result == ["Lorem ipsum ", " sit amet, ", " consetetur ", " sadipscing elitr, ", " sed diam"]
