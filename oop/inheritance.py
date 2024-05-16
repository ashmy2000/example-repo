# Inheritance = one class/object is based on another class/object

# Vehicle <- LandVehicle <- Car | Motorcycle
# LandVehicle and Vehicle are superclass of Car
# Car is subclass of LandVehicle

class Vehicle:
    class_message = "Message from Vehicle Class"

    def __init__(self, speed):
        self.speed = speed

    def super_speed_more(self):
        print("Activated from Vehicle")
        self.speed += 5


class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        # Vehicle.__init__(self, speed)
        super().__init__(speed)
        # self.speed = speed
        self.wheel_count = wheel_count
        print(Vehicle.class_message)

    def speed_up(self):
        self.speed += 5


class Car(LandVehicle):
    def super_speed(self):
        print("Activated from LandVehicle")
        super().speed_up()


if __name__ == '__main__':
    # Is Car a subclass of Vehicle?
    print(isinstance(Vehicle, LandVehicle))
    print(isinstance(LandVehicle, Vehicle))
    print(isinstance(Car, Vehicle))
    print("**********************")
    print(issubclass(Car, Vehicle))
    print(issubclass(Car, LandVehicle))
    print(issubclass(Car, Car))
    print(issubclass(Vehicle, Vehicle))
    # prints print statement
    my_car = Car(5, 4)
    print(my_car.__dict__)
    print(my_car.class_message)
    print("**********************")
    fast_Car = Car(10, 4)
    print(fast_Car.__dict__)
    print(fast_Car.super_speed_more())
    print(fast_Car.__dict__)
    print(fast_Car.super_speed())
    print(fast_Car.__dict__)
