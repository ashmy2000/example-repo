# ASCII
# Code Point, ut creates issue
# Unicode doesn't use code page\\

print(len("Hi there"))
print(len("Hi there"[1]))
print(("Hi there"[1:]))
print(("Hi there"[:5]))
print(("Hi there"[3:5]))

print(ord("a"))
print(ord("A"))
print(chr(97))

# has invinsible new char \n in it
test_string = """Line 1
Line 2"""
print(len(test_string))

# order important - comutitive
# `print(min("asaaaaahmy"))

# Finding a letter on a string
name = "Ashfgthfhassaamy"
print(name.index("s")) # if not there then outputs error message
print(name.find("s"))  # if not there then outputs -1
print(name.find("z", 10, 15))  # looks for "s" inclusive 10th index and exlusive 15th index

print(name.isalnum())
print(name.isalpha())
print(name.isdigit())
print(name.islower())
print(name.isupper())
print(name.isspace()) 

" ".join(["As", "hm", "y"])
# sorted() -> creates a sorted copy
# sort()   -> sorts the original list