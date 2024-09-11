txt = 'aga aga aga aga'
print(txt.rfind('aga'))
# searches from left to right and returns the lowest index.
txt2 = 'aga aga aga aga'
print(txt2.find('aga', 5))
# searches from right to left and returns the highest index.
txt4 = 'aga aga aga aga'
print(txt4.rfind('aga', 5))

inpt = ['a', 'b', 'c', 'd']
print(list(map(lambda a: a+a, inpt)))

# trying to access a.d will result in an AttributeError because d does not exist as an attribute of the instance a.
class A:
    b = 'b'
def __init__(self):
    self.c = 'c'
    d = self.c
a = A()
# print(a.d)


class Hamster():
    def __init__(self, teeth_length):
        self.__teeth_length = teeth_length
ham = Hamster(5)
# print(ham.__teeth_length) -> Code will raise error
print(ham._Hamster__teeth_length)

inpt = ['Adam', 'Mary', 'Kate']
res1 = ''.join(list(map(lambda x: x + '-', inpt)))
print(res1)

inpt2 = ['Adam', 'Mary', 'Kate']
res2 = list(map(lambda x: x + '-', inpt2))
print(res2)

inpt3 = ['Adam', 'Mary', 'Kate']
res3 = '-'.join(inpt3)
print(res3)



print(len("\\\\"))

import math
print(math.ceil(3.0) + math.floor(4.9) + 3)

class Art():
    masterpiece = 'John'
    def __init__(self):
        self.name = 'One'
print(len(Art().__dict__))


class A:
    b = 1
    def __init__(self):
        self.c = 0
print(hasattr(A(), 'c'))



# will show a list of all entities available in the random module
import random
print(dir(random))


"""
Creates a bytearray of length 10 with all elements initialized to 0.
Accesses the first element of the bytearray, which is 0.
Converts this element to an integer (which is redundant because it is already an integer).
Wraps this integer in a list [0].
Applies a lambda function that adds 5 to each element in the list.
Converts the result to a list and prints it.
"""
print(list(map(lambda x: x + 5, [int(bytearray(10)[0])])))

print([['i' for i in range(1, 2)] for j in range(2)])
print([['*' for i in range(1)] for j in range(2)])
print(['*' for i in range(6)])
