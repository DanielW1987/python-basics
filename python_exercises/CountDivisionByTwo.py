# How often can you divide a number by 2?
originalNumber: int = 120
counter: int = 0
tempResult: int = originalNumber
while tempResult % 2 == 0:
    counter += 1
    tempResult = int(tempResult / 2)

print("The number {} can be divided {} times by 2".format(originalNumber, counter))
