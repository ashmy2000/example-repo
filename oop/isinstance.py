import inheritance

if __name__ == '__main__':
    new_vehicle = inheritance.Vehicle(5)
    new_landvehicle = inheritance.LandVehicle(6, 6)

    print(isinstance(new_landvehicle, inheritance.Vehicle))
    print(isinstance(new_vehicle, inheritance.Vehicle))
    print(isinstance(new_vehicle, inheritance.LandVehicle))
    print(isinstance(new_landvehicle, inheritance.Vehicle))
    print("**********************")
    new_locatioon_vehicle = new_vehicle
    print(new_locatioon_vehicle is new_vehicle)
    # If value changes in new_vehicle, it will relfect in new_locatioon_vehicle
    print("**********************")
    first_num = 5
    sec_num = 2
    sec_num += 3
    print(first_num is sec_num)
    print("**********************")
    first_str = "hello"
    sec_str = "hell"
    sec_str += "o"
    # creates new object | 2 sep objects in the memory
    print(first_str is sec_str)
    print(first_str == sec_str)




