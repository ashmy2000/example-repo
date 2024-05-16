def return_bigger_num(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError
    if a > b:
        return a
    else:
        return b

# print(return_bigger_num(5,"l"))

def return_reverse(x):
    try:
        print(1/x)
    except:
        print("except")
        raise #  This gives console the name of the error message so ZeroDivisionError: division by zero

return_reverse(1)