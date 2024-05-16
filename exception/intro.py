# IndentationError = expected an indented block
# Value Error = exception -> not right value
# Syntax error = exceptional error ->

try:
    num = int(input("Enter Num: "))
    print(f"Inverse of {num} is {1/num}", num)
    # raise SyntaxError
except TypeError:
    print("SyntaxError")
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")

"""
BaseException
    Exception   System Exit     KeyboardInterrupt
    Arithmetic              LookupEroor TypeError ValueError
    Zero DivisionalError    IndexError
                            KeyError  




"""


