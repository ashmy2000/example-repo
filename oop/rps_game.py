import random

class Rock_Paper_Scissors_Game:
    def __init__(self):
        print("--- Rock Paper Scissors Game ----")

    def get_number_of_games(self):
        right = False
        while not right:
            try:
                number_of_games = int(input("How many rounds would you like to play? "))
                right = True
            except ValueError:
                print("Enter an integer value")
        return number_of_games

    def computer_play(self):
        return random.choice(['r', 'p', 's'])

    def play(self):
        num_of_game = self.get_number_of_games()
        for i in range(num_of_game):
            human = input("Enter either 'r', 'p', 's': ").lower()
            while human not in ['r', 'p', 's']:
                print("Invalid input. Enter either 'r', 'p', 's':")
                human = input("Enter either 'r', 'p', 's': ").lower()
            computer = self.computer_play()

            print(f"You: {human} | Computer: {computer}")
            if human == computer:
                print("It's a tie!")
            elif ((human == 'r' and computer == 's') or
                  (human == 'p' and computer == 'r') or
                  (human == 's' and computer == 'p')):
                print("You Win!")
            else:
                print("You Lose!")

if __name__ == '__main__':
    new_game = Rock_Paper_Scissors_Game()
    new_game.play()
