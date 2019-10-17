# read string from console
stringValue = input("Enter anything: ")
print(stringValue)

# read int from console
intValue = int(input("Enter an int value: "))
print(intValue)

# read multiple inputs
lst = [int(x) for x in input("Enter three numbers separated by comma: ").split(",", 3)]
print(lst)
