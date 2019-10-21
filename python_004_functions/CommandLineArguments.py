import sys

arg_list = sys.argv

for argument in arg_list:
    print(argument)

print("Script name is '{}'".format(arg_list[0]))
print("Length of arguments: {}".format(len(arg_list)))
