import unittest
from expects import expect, equal


class PokerKataAcceptance(unittest.TestCase):
    def test_hand_ranking(self):
        hands = []
        hands.append(PokerHand("KS 2H 5C JD TD"))
        hands.append(PokerHand("2C 3C AC 4C 5C"))
        hands.append(PokerHand("4C 8D AC 4S QH"))
        ranked = sorted(hands)
        expect(ranked).to(equal(["2C 3C AC 4C 5C", "4C 8D AC 4S QH", "KS 2H 5C JD TD"]))
