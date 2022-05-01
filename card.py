class Card:
    """ This class representa a playing card.  
        A card has 2 attributes, value and suit.  value is an int between 1 and 13.  suit is an int between 1 and 4.
        It uses private attributes and property getters and setters.
        Setters have appropriate validation that raise an exception when invalid data is used."""

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    @property
    def value(self):
        return self.value

    @property
    def suit(self):
        return self.suit

    @value.setter
    def value(self, value):
        if isinstance(value, int) and value > 0:  # it's valid for a programmer to call p.id = 10
            self.value = value
        else:  # but invalid to use a non-integer value or a value that's < 0
            raise ValueError(
                f"Id must be a non-zero positive integer. {type(value)}  {value}")  # this error cannot be ignored in the calling code

    @suit.setter
    def suit(self, suit):
        if isinstance(suit, str) and len(suit.strip()) > 0:
            self.suit = suit.strip()
        else:
            raise ValueError(f"Description must a non-empty character string {type(suit)}  {suit}")


    def __str__(self):
        return f'Card( {self.value} of {self.suit})'

    # these lists are used in __str__
    # they are class variables rather than instance variables and are shared by each object of the class
    __values = ["", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "Ten", "Jack", "Queen", "King"]
    __suits = ["", "Clubs", "Diamonds", "Hearts", "Spades" ]

    def __eq__(self, other):
        """ This "magic method" is called when you check the equality of 2 cards.  if card1 == card2 for example.
            2 cards are equal if they're both cards and if their attributes have the same values"""
        if isinstance(other, Card):
            return self.suit == other.suit and self.value == other.value
        else:
            return False