# Encapsulation refers to the bundling of data and methods that operate on the data into a single unit or class.
# It hides the internal state of an object and only exposes the necessary functionalities.
class Car():
    def __init__(self, model, colour, initial_speed=0):
        self.model = model
        self.colour = colour
        if initial_speed < 5:
            self.__speed = 0
        else:
            self.__speed = initial_speed

    def speed_up(self):
        self.__speed += 5

    def speed_down(self):
        if self.__speed < 5:
            self.__speed = 0
        else:
            self.__speed -= 5

    def show_speed(self):
        print(f"current speed: {self.__speed}")


my_car = Car('Tesla', 'white', 10)
my_car.show_speed()
my_car.speed_down()
my_car.show_speed()
my_car.speed_down()
my_car.show_speed()
my_car.speed = 50 # doesn't work
my_car.show_speed()