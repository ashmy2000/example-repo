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
names = ["Suvi", "Aleks", "Elle", "test2", "tes3"]
string = ("suviellealeks")

# print(random.choice(number))
# print(random.choice(names))
# print(random.choice(string))

# for i in names:
#     print("choice", random.choice(i))

print(random.sample(names, 3))
random.choice(names)


def generate_tickets(ticket_count, max_number):
    #  5, it will generate 5 unique random integers between 0 and 9 inclusively.
    tickets = random.sample(range(max_number), ticket_count)
    # ticket [7, 9, 5, 8, 0]
    winning_ticket = random.choice(tickets)
    # ([5, 8, 2, 7, 6], 5)
    return tickets, winning_ticket

# Test the function
result = generate_tickets(2,20)
print(result)

