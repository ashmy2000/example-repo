import random
# if you have a Python file named game.py and both the Card and Deck classes are defined within this file,
# they are in the same module. You can then reference the Card class directly from the Deck class as Card(suit, value)
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def present(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        # hearts, ace | hearts 2 | hearts 3.... then diamond
        for suit in suits:
            for value in values:
                # refers specifically to the Card class defined within the same module or namespace where the Deck
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def count_remaining(self):
        return len(self.cards)

    def get_remaining(self):
        return [x.present() for x in self.cards]

# Example usage:
deck = Deck()
print(deck.get_remaining())    # Output: List of all 52 cards
deck.shuffle()
print(deck.get_remaining())    # Output: List of all 52 cards
print(deck.count_remaining())  # Output: 52
print(deck.get_remaining())    # Output: List of all 52 cards
print(deck.deal().present())   # Output: A random card present() value
print(deck.count_remaining())  # Output: 51, one card has been dealt

