from card import *

def testConstructor():
    c = Card(1, 'Spades')
    print(f"Testing constructor with parameters.  Expect card 1 | Spades {c}")


def testPropertyGetters():
    c = Card(1, 'Spades')
    print(f"Testing property getters.  Expect individual attributes for card 1 | Spades")
    print(f"Number: {c.value}, Suit: {c.suit}, {c}")


def testPropertySetters():
    c = Card(1, 'Hearts')
    c.value = 3
    c.suit = 'Diamond'
    print(f"Testing property setters.  Expect individual attributes for card 1|Hearts to change to 3|Diamonds. {c}")