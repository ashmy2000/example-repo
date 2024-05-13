# represents the current module's namespace when it is being run as the main program.
if __name__ == '__main__':
    print(__name__, "File Running")
else:
    print(__name__, "File imported")

input_string = "Ashmy"