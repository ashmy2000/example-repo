import math

# for name in dir(math):
#     print(name, end="\t")

# PCAP -> ceil() | floor() | trunc()
# ceil() -> Round up, nearest int, not less than itself
print(math.ceil(3.1))
print(math.ceil(3.5))
print(math.ceil(3.9))
print(math.ceil(3.0))
print(math.ceil(-5.4))

# floor() -> Round down, nearest int, not less than itself
print(math.floor(3.1))
print(math.floor(3.5))
print(math.floor(3.9))
print(math.floor(3.0))
print(math.floor(-5.4))

# trunc() -> number at the start before .
print(math.trunc(3.1))
print(math.trunc(3.5))
print(math.trunc(3.9))
print(math.trunc(3.0))
print(math.trunc(-5.4))

# factorial() -> 3! = 3 x 2 x 1
print(math.factorial(3))
print(math.factorial(4))
print(math.factorial(6))
print(math.factorial(12))
print(math.factorial(8))

# sqrt() ->
print(math.sqrt(64))
print(math.sqrt(100))

# hypot () -> Longest side in triangle FLOAT added more comments
print(math.hypot(64,63))
print(math.hypot(4,6))