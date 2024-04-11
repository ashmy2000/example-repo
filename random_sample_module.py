# Random Module - psedo random -> start with seed (starting value) then goes into an algorithm. Seed uses timestamp
# to get different one each time

# RANDOM | SEED | SAMPLE | CHOICE
import random
# changes seed using timestamp, so when ran again - values change
#random.seed(0) # now refresh, you'll still get the same value each time
# print(random.random())
# print(random.random())
# print(random.random())

number = [1, 2, 3, 4, 5]
names = ["Suvi", "Aleks", "Elle"]
string = ("suviellealeks")

# print(random.choice(number))
# print(random.choice(names))
# print(random.choice(string))

# for i in names:
#     print("choice", random.choice(i))

print(random.sample(names, 3))
random.choice(names)
