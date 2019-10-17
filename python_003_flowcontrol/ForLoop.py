# Looping a range
for i in range(50, 70):
    print(i)


# break in a loop
numbers: list = [3, 6, 9, 12]
for number in numbers:
    if number == 9:
        break # aborts the loop
        # continue # skips the iteration
    else:
        print(number)
