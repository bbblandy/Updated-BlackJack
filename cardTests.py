from card import *

def testConstructor():
    c = Card(1, 1)
    print(f"Testing constructor with parameters.  Expect Ace of CLubs {c}")


def testPropertyGetters():
    c = Card(1, 1)
    print(f"Testing property getters.  Expect individual attributes for card Ace of Clubs")
    print(f"Number: {c.value}, Suit: {c.suit}, {c}")


def testPropertySetters():
    c = Card(1, 1)
    c.value = 3
    c.suit = 2
    print(f"Testing property setters.  Expect individual attributes for card Ace of Clubs to change to 3 of Hearts. {c}")


def testPropertySettersWithValidation():
    c = Card(1,1)
    try:
        c.suit = 'Hearts'
    except ValueError as vErr:
        print("An exception was thrown setting code to an str")
        print(vErr)
    try:
        c.value = '10'
    except ValueError as vErr:
        print("An exception was thrown setting First Name to an str")
        print(vErr)

def testEncapsulation():
    c = Card(1,1)
    try:
        print(c.suit)
        c.suit = 1
        print(c.suit)
        print (c.__suit)
        c.__suit = 1
        print (c.__suit)
    except AttributeError as attErr:
        print("An attribute error was throws in test Encapsulation")
        print(attErr)
    try:
        print(c.value)
        c.suit = 1
        print(c.value)
        print(c.__value)
        c.__value = 1
        print(c.__value)
    except AttributeError as attErr:
        print("An attribute error was throws in test Encapsulation")
        print(attErr)