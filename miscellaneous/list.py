numbers = []

for i in range(1,11):
    numbers.append(i)

print(f"numbers: {numbers}")

numbers_two = [i for i in range(1, 11)]
print(f"numbers_two: {numbers_two}")

numbers_three = [i for i in range(1, 11) if i % 3 == 0]
print(f"numbers_two: {numbers_three}")

binary = [0 if i % 2 == 0 else 1 for i in range(10)]
print(f"numbers_two: {binary}")

table = [[i for i in range(6)] for j in range(5)]
print(table)
for row in table:
    print(row)
