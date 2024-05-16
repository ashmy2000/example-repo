# Class has more than one super class | inherited more than one class

class Vehicle():
    def go(self):
        print("Vehicle")

    def same(self):
        print("Vehicle")


class Flyable():
    def fly(self):
        print("Flying")

    def same(self):
        print("Vehicle")


class Airplane(Flyable, Vehicle):
    def fly(self):
        print("Airplane")


if __name__ == '__main__':
    my_plane = Airplane()
    my_plane.go()
    my_plane.fly()
    my_plane.same()  # Vehicle ? -> MRO = (Vehicle, Flyable): has vehicle first so prints that. 1. Looks in object 2. super class left to right 3. Error
    print(Vehicle.__bases__) # object is returned
    print(Airplane.__bases__)  # direct superclass returned
