def greet(text):
    def print_greet():
        print(text)
    return print_greet

hello = greet("hi")
hello()


def mulitple_closure(x):
    def multiple(y):
        return x * y
    return multiple


multi_5 = mulitple_closure(5)
multi_15 = mulitple_closure(15)
print(multi_5(10))
print(multi_15(10))
