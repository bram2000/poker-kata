import itertools
from enum import Enum, IntEnum


class CardSuit(Enum):
    Clubs = object()
    Spades = object()
    Hearts = object()
    Diamonds = object()


class CardFace(IntEnum):
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14


class Trick(IntEnum):
    HiCard = 1
    Pair = 2
    TwoPair = 3
    ThreeOfAKind = 4
    FullHouse = 5
    Straight = 6
    Flush = 7
    FourOfAKind = 8
    StraightFlush = 9


class Hand:
    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError
        self.cards = sorted(cards)
        self.groups = [len(list(v)) for _, v in itertools.groupby(self.cards)]
        self.groups = list(filter(lambda v: v > 1, self.groups))
        print(f"groups: {self.groups}")

    def has_groups_of(self, size):
        print(f"groups: {self.groups} size: {size} match: {self.groups == size}")
        return self.groups == size

    @property
    def rank(self):
        if self.
        if self.has_groups_of([2, 3]):
            print("JB here")
            trick = Trick.FullHouse
        elif self.has_groups_of([3]):
            trick = Trick.ThreeOfAKind
        elif self.has_groups_of([2, 2]):
            trick = Trick.TwoPair
        elif self.has_groups_of([2]):
            trick = Trick.Pair
        else:
            trick = Trick.HiCard

        return trick

# class Rank(tuple):
#     def __new__(cls, trick, face):
#         assert isinstance(trick, Trick)
#         assert isinstance(face, CardFace) or (
#             isinstance(face, tuple) and all([isinstance(f, CardFace) for f in face])
#         )
#         return tuple.__new__(Rank, (trick, face))


class Card(tuple):
    def __new__(cls, face, suit):
        assert isinstance(face, CardFace)
        assert isinstance(suit, CardSuit)
        return tuple.__new__(Card, (face, suit))

    @property
    def face(self):
        return self[0]

    @property
    def suit(self):
        return self[1]

    def __eq__(self, other):
        return self.face == other.face

    def __gt__(self, other):
        return self.face > other.face

    def __lt__(self, other):
        return self.face < other.face

    def __repr__(self):
        symbols = {
            CardSuit.Clubs: "♣︎",
            CardSuit.Spades: "♠︎",
            CardSuit.Hearts: "♥︎",
            CardSuit.Diamonds: "♦︎",
        }
        return f"{self[0].value}{symbols[self[1]]}"
