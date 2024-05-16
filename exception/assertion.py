# something in program that's always true, to notify bugs during oding not error handling

def cal(num):
    assert (num != 0), "Got 0"
    return num * num

print(cal(0))