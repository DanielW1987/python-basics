from typing import TextIO

a, b = [int(x) for x in input("Enter two numbers: ").split()]

f: TextIO = open("myfile.txt", "w")
try:
    result = a / b
    f.write("{} / {} = {}".format(a, b, result))
except ZeroDivisionError as exception:
    print("0 is not allowed as second number!")
    print(exception)
else:
    # else can be used for logic that should be executed only if no exception is thrown
    print("You have entered a non-zero value")
finally:
    f.close()
