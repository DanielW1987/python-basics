number: int = int(input("Enter an integer value below 100: "))

for number in range(number, 100):
    if number % 10 == 0:
        continue
    else:
        print(number)
