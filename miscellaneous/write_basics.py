try:
    stream = open("animal.txt", "w")
    stream.write("Adding more")
    stream.write("Adding more")
    stream.close()
except Exception as e:
    print(e)