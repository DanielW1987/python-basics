def do_something():
    print("Hello")
    print("World")


def print_three_times(text: str):
    print((text + "\n") * 3)


def function_with_default_parameter_values(text="Hello", color="red", width="2px"):
    print("text: {}, color: {}, width: {}".format(text, color, width))


do_something()
print_three_times("World")
function_with_default_parameter_values()
function_with_default_parameter_values(color="blue")
