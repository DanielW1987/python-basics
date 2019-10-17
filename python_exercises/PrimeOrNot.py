number: int = int(input("Enter an integer value for prime check: "))
prime: bool = True

for i in range(2, (number // 2)):
    if number % i == 0:
        prime = False
        break

if prime:
    print("{} is a prime number!".format(number))
else:
    print("{} is not a prime number!".format(number))
