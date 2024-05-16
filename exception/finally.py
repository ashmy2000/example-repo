# else and finally not dependent. finally should be after else.

try:
    value = int(input("Enter Value"))
    print(value / 2)
except:
    print("except")
else:
    print("ELSE")
finally:
    print("finally")

# even if except is ran, finally is also printed whereas else won't be printed
