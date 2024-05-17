import sys
# sees what entered in console
for line in sys.stdin:
    if line.rstrip() == "q":
        break
    print(line)
print("you pressed q so break")


# stdout
sys.stdout.write("hello")
