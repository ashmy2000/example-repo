# reading txt file

try:
    # opens file
    stream = open("animal.txt")
    # print(stream.read(2))
    # print(stream.read(5))
    char = stream.read(1)
    counter = 0
    while char != "":
        counter += 1
        char = stream.read(1)
        char2 = stream.readline(1)
        char3 = stream.readlines(1)
    stream.close()
    print(f"Letters in the txt is: {counter}")
except Exception as e:
    print(e)

# Reading one line at a time speeds up performance.