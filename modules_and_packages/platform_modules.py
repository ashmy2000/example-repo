import platform

print(platform.platform())  # prints the platform information
print(platform.platform(True, True))  # prints the detailed platform information
print(platform.machine())  # prints the machine type
print(platform.processor())  # prints the processor information
print(platform.system())  # prints the system/OS name
print(platform.python_implementation())  # prints the Python implementation (e.g., CPython, Jython)
print(platform.python_version_tuple())  # prints the Python version as a tuple (major, minor, micro)
