
class Vehicle():
    def show_power_type(self):
        print("Vehicle")

class Electric_Vehicle(Vehicle):
    def show_power_type(self):
        print("Electric_Vehicle")

class Petrol_Vehicle(Vehicle):
    def show_power_type(self):
        print("Petrol_Vehicle")

class Hybrid_Car(Electric_Vehicle, Petrol_Vehicle):
    pass


if __name__ == '__main__':
    new_car = Hybrid_Car()
    new_car.show_power_type() # first parent in (), if order changed then petrol is evoked


    """ MRO => own def method > own () > parent super class left to right"""