def return_bigger_num(a,b):
    try:
        if a > b:
            return a
        else:
            return b
    except Exception as e:
        print(e)
        #return None

# print(return_bigger_num("s",0))

# for subclass in Exception.__subclasses__():
#     print(subclass.__name__)


try:
    raise Exception("Writing manually")
except Exception as e:
    print(e.args)

try:
    5 < "a"
except Exception as e:
    print(e.args) # ("'<' not supported between instances of 'int' and 'str'",)
