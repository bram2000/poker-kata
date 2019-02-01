import unittest
from poker import CardFace, CardSuit, Card, Hand, Trick
from expects import expect, equal, be_true, be_above


class CardTests(unittest.TestCase):
    def test_repr(self):
        card = Card(CardFace.Two, CardSuit.Diamonds)
        expect(str(card)).to(equal("2♦︎"))

    def test_gt(self):
        hicard = Card(CardFace.King, CardSuit.Hearts)
        locard = Card(CardFace.Two, CardSuit.Hearts)
        expect(hicard).to(be_above(locard))

    def test_eq(self):
        card = Card(CardFace.Ace, CardSuit.Clubs)
        samecard = Card(CardFace.Ace, CardSuit.Clubs)
        expect(card).to(equal(samecard))


# Do we really need a Hand class?
class HandTests(unittest.TestCase):
    pass


class RankHandTests(unittest.TestCase):
    def test_hi_card(self):
        # Given
        hand = Hand([
            Card(CardFace.Two, CardSuit.Clubs),
            Card(CardFace.Four, CardSuit.Spades),
            Card(CardFace.Five, CardSuit.Clubs),
            Card(CardFace.Six, CardSuit.Clubs),
            Card(CardFace.Seven, CardSuit.Clubs),
        ])

        # When
        hand_rank = hand.rank
        expected = Trick.HiCard

        # Then
        expect(hand_rank).to(equal(expected))

    def test_pair(self):
        # Given
        hand = [
            Card(CardFace.Two, CardSuit.Clubs),
            Card(CardFace.Four, CardSuit.Spades),
            Card(CardFace.Five, CardSuit.Clubs),
            Card(CardFace.Six, CardSuit.Clubs),
            Card(CardFace.Six, CardSuit.Hearts),
        ]

    def test_two_pair(self):
        # Given
        hand = Hand([
            Card(CardFace.Two, CardSuit.Clubs),
            Card(CardFace.Five, CardSuit.Spades),
            Card(CardFace.Five, CardSuit.Clubs),
            Card(CardFace.Six, CardSuit.Clubs),
            Card(CardFace.Six, CardSuit.Hearts),
        ])

        # When
        hand_rank = hand.rank
        expected = Trick.TwoPair

        # Then
        expect(hand_rank).to(equal(expected))

    def test_three_of_a_kind(self):
        # Given
        hand = Hand([
            Card(CardFace.Two, CardSuit.Clubs),
            Card(CardFace.Five, CardSuit.Spades),
            Card(CardFace.Five, CardSuit.Clubs),
            Card(CardFace.Five, CardSuit.Hearts),
            Card(CardFace.Six, CardSuit.Hearts),
        ])

        # When
        hand_rank = hand.rank
        expected = Trick.ThreeOfAKind

        # Then
        expect(hand_rank).to(equal(expected))

    def test_full_house(self):
        # Given
        hand = Hand([
            Card(CardFace.Two, CardSuit.Clubs),
            Card(CardFace.Five, CardSuit.Spades),
            Card(CardFace.Five, CardSuit.Clubs),
            Card(CardFace.Five, CardSuit.Hearts),
            Card(CardFace.Two, CardSuit.Hearts),
        ])

        # When
        hand_rank = hand.rank
        expected = Trick.FullHouse

        # Then
        expect(hand_rank).to(equal(expected))

    def test_flush(self):
        # Given
        hand = Hand([
            Card(CardFace.Queen, CardSuit.Clubs),
            Card(CardFace.Five, CardSuit.Clubs),
            Card(CardFace.Six, CardSuit.Clubs),
            Card(CardFace.Jack, CardSuit.Clubs),
            Card(CardFace.Two, CardSuit.Clubs),
        ])

        # When
        hand_rank = hand.rank
        expected = Trick.Flush

        # Then
        expect(hand_rank).to(equal(expected))
