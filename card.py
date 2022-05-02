class Card:
    """ This class representa a playing card.  
        A card has 2 attributes, value and suit.  value is an int between 1 and 13.  suit is an int between 1 and 4.
        It uses private attributes and property getters and setters.
        Setters have appropriate validation that raise an exception when invalid data is used."""

    def __init__(self, value = 0, suit = 0):
        self.__value = value
        self.__suit = suit

    @property
    def value(self):
        return self.__value

    @property
    def suit(self):
        return self.__suit

    @value.setter
    def value(self, value):
        if isinstance(value, int) and value > 0:
            self.__value = value
        else:
            raise ValueError(
                f"Value must be a integer. {type(value)}  {value}")

    @suit.setter
    def suit(self, suit):
        if isinstance(suit, int) and suit > 0:
            self.__suit = suit
        else:
            raise ValueError(f"Must be an int {type(suit)}  {suit}")


    def __str__(self):
        __values = ["", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "Ten", "Jack", "Queen", "King"]
        __suits = ["", "Clubs", "Hearts", "Diamonds", "Spades"]
        return f'Card( {self.__value} of {self.__suit})'


    def __eq__(self, other):
        """ This "magic method" is called when you check the equality of 2 cards.  if card1 == card2 for example.
            2 cards are equal if they're both cards and if their attributes have the same values"""
        if isinstance(other, Card):
            return self.suit == other.suit and self.value == other.value
        else:
            return False