# Class has capital letter at the start
class User:
    # Constructor | Self points to the objects
    def __init__(self):
        self.nickname = "samplename"
        self.city = "samplecity"

    # function in a class is methodd
    def introduce(self):
        print(f"Hello I am, {self.nickname} and I live in {self.city}")

sample_user = User()
sample_user.introduce()