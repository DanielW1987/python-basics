# How often can you divide a number by 2?
def count_division_by_two(number: int):
    counter: int = 0
    temp_result: int = number
    while temp_result % 2 == 0:
        counter += 1
        temp_result = int(temp_result / 2)

    return counter


theNumber: int = int(input("Enter your number: "))
print("The number {} can be divided {} times by 2".format(theNumber, count_division_by_two(theNumber)))
