# Instance variable for each object but class variable only belongs to that class
class Dog2:
    __counter = 0  # -> one copy of that class so will be the same for each object

    def __init__(self, name, age):
        # instance variable
        self.__name = name
        self.age = age
        # class variable
        Dog2.__counter += 1


if __name__ == '__main__':
    my_pet2 = Dog2("Teddy", 5)
    print(my_pet2.__dict__)  # doesn't show class variable
    # to see class variable 2 ways
    # print(my_pet2.counter)
    # print(Dog2.counter)
    print(my_pet2._Dog2__counter)
    print(Dog2._Dog2__counter)

    # mangled counter -> '_Dog2__counter': 1,
    print(Dog2.__dict__)
    print(Dog2.__name__)
    print(type(my_pet2).__name__)

    print(__name__)
