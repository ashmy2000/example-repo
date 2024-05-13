class Dog():
    def __init__(self, name, age=6):
        self.__name = name
        self.age = age

    def __str__(self):
        return "__str__ evoked when print(new_dog)"

    def introduce(self):
        print(f"Dog name is {self._Dog__name}, and age is: {self.age}")

new_dog = Dog("tommy")
print(new_dog.age)
# <__main__.Dog object at 0x100a81110>
# indicating that it's an object of class Dog located at memory address 0x100a81110.
print(new_dog._Dog__name)
# __str__ evoked when print(new_dog)
print(new_dog)

print("Coming from methods folder")