class Dog():
    latin = "Canis"
    def __init__(self, colour = "brown"):
        self.colour = colour
        Dog.latin += colour


class X:
    def __init__(self):
        pass



if __name__ == '__main__':
    # first = Dog()
    # print(first.latin)
    # print(first.colour)
    # second = Dog("red")
    # print(second.latin)
    # print(second.colour)
    # third = Dog("white")
    # print(second.latin)
    # print(third.colour)

    x = X("myobject")
