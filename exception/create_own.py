class AnimalValueError(ValueError):
    print("AnimalValueError")

def produce_animal_sound(animal_type):
    if animal_type == "dog":
        print("Woof, woof")
    elif animal_type == "cat":
        print("meow, meow")
    else:
        raise AnimalValueError()


# produce_animal_sound("d")

try:
    raise Exception(2)
except Exception as e:
    print(len(e.args))