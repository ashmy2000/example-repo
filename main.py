import own_modules
import math


def halve_string(input_string):
    half_length = len(input_string) // 2
    print("Full String is:", input_string, ".", "Half the length is:", half_length)
    if len(input_string) % 2 == 0:
        print("even")
        first_half = input_string[:half_length]
        second_half = input_string[half_length:]
        print(first_half, second_half)
    elif len(input_string) % 2 != 0:
        print("odd")
        first_half = input_string[:half_length + 1]
        second_half = input_string[half_length + 1:]
        print(first_half, second_half)
    else:
        print("error")


# Assuming you want to call the function with the string from the module
halve_string(own_modules.input_string)
