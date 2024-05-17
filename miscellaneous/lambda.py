
def sum(a, b):
    return a + b


var = lambda a, b: a + b

# print(sum(5, 3))
# print(var(5, 3))


def apply_func(elements, func):
    for element in elements:
        print(func(element))


# my_func = lambda x: x * x
# apply_func([1, 2, 3, 4, 5], my_func)
# apply_func([1, 2, 3, 4, 5], lambda x: x * x)

lambda_func = lambda i: i * 3
lists = [1, 2, 3, 4, 5]
map_result = map(lambda_func, lists)
print(list(map_result))
print(list(map(lambda i: i * 3, [1, 2, 3, 4, 5])))
print(list(filter(lambda i: i % 2 == 0, [1, 2, 3, 4, 5])))


emails = [
    "ashmy2000@hotmail.com",
    "as as as",
    "abi20@gmail.com",
    "sfsfsfsf"
]

print(list(filter(lambda x: "@" and "com" in x, emails)))
