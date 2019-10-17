start: int = 2
end: int = 20
oddNumber: int = start

if oddNumber % 2 == 0:
    oddNumber += 1

while oddNumber <= end:
    print(oddNumber)
    oddNumber += 2
