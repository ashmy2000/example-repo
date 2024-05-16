# This is known as polymorphism

class Animal():
    def __init__(self, sound):
        self.sound = "AnimalFixedVariable"


class Animal2():
    def __init__(self, sound):
        self.sound = sound


class Animal3():
    def __init__(self):
        self.sound = "Animal2Class"

    def legs(self):
        print("legs from Animal3")

    def body(self):
        print("I am calling from")
        self.legs()

class Dog(Animal3):
    def __init__(self):
        self.sound = "DogOVERRIDE"

    def legs(self):
        print("legs from Dog")

if __name__ == '__main__':
    new_animal = Animal("meoeewww")
    print(new_animal.sound)

    new_animal2 = Animal2("meoww")
    print(new_animal2.sound)

    print("*****************")
    new_animal3 = Animal3()
    print(new_animal3.sound)
    print(new_animal3.legs())
    print(new_animal3.body())
    print("*****************")
    new_dog = Dog()
    print(new_dog.sound)
    print(new_dog.legs())
    print(new_dog.body())
