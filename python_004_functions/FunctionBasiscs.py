# void method with no arguments
def do_something():
    print("Hello")
    print("World")


# void method with argument
def print_three_times(text: str):
    print((text + "\n") * 3)


# void method with arguments and default values
def function_with_default_parameter_values(text="Hello", color="red", width="2px"):
    print("text: {}, color: {}, width: {}".format(text, color, width))


# method with return
def calculate_average(values: list):
    sum_of_values: int = 0
    for value in values:
        sum_of_values += value

    return sum_of_values / len(values)


# method with multiple returns
def calculate(value1: int, value2: int):
    addition_result: int = value1 + value2
    subtraction_result: int = value1 - value2
    multiplication_result: int = value1 * value2
    division_result: float = value1 / value2

    return addition_result, subtraction_result, multiplication_result, division_result


do_something()
print_three_times("World")
function_with_default_parameter_values()
function_with_default_parameter_values(color="blue") # keyword arguments can be used for any method with arguments
print(calculate_average([10, 20, 30, 40, 50]))

result: tuple = calculate(10, 5)
print(result)
