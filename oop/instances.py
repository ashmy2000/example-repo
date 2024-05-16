# Abstraction focuses on the essential features of an object while hiding the irrelevant details.
# It simplifies complex systems by modeling only the necessary aspects, making it easier to understand and manage.
class Dog():
    def __init__(self, name, age):
        self.__name = name
        self.age = age

if __name__ == '__main__':
    # new object
    my_pet = Dog("Teddy", 2)
    # added property - 2 from constructor and added one manually later {'name': 'Teddy', 'age': 2, 'colour': 'brown'}
    my_pet.colour = "brown"
    # checking instances variable for given object
    print(my_pet.__dict__)

    # when you add __ private varbale it changes it to _className__varibale Name -> name mangling
    # {'_Dog__name': 'Teddy', 'age': 2, 'colour': 'brown'}

    # access a property outise the class, it's private. Someone can still access mangled name,
    # __ is a warning -> shouldn't be changed
    # mangling won't work if you add new __ after.
    print(my_pet._Dog__name)