from os import strerror

try:
    stream = open("animal.txt")
    stream.close()
except Exception as e:
    print(strerror(e.errno))