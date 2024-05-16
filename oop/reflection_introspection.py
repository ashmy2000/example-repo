# Different types of operations
# Introspection = is the ability of a program to check the type of an object on its properties at runtime
# Reflection = Ability to change the prop or methods of an objects at runtime

# Importing this from the method folder from the same root folder
from methods import Dog


def empty_string(user_object):
    # Introspection
    for prop_name in user_object.__dict__.keys():
        # Reflection
        prop_value = getattr(user_object, prop_name)
        if isinstance(prop_value, str):
            setattr(user_object, prop_name, '')

if __name__ == '__main__':
    new_Dog2 = Dog("Tommy", 7)
    print(new_Dog2.introduce())
    empty_string(new_Dog2)
    print(new_Dog2.introduce())
    # new thing