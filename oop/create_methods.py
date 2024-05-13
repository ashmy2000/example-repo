# Classes and Objects: Classes are blueprints for creating objects. Objects are instances of classes that
# encapsulate data (attributes) and behaviors (methods).
class User2:
    # Constructor | Self points to the objects
    def __init__(self, name, city):
        self.nickname = "name"
        self.city = "city"

    # function in a class is methodd
    def introduce(self):
        print(f"Hello I am, {self.nickname} and I live in {self.city}")

sample_user = User2("name", "city")
sample_user.introduce()
print(sample_user.city)