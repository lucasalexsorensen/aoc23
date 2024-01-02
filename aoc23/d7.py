from collections import Counter
from enum import IntEnum

from .helpers import load_data

strengths = "23456789TJQKA"


class HandTypes(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


def get_type_rank(hand: str, jokers_wildcard=False) -> int:
    results = []
    for char_to_replace in "23456789TZQKA":
        c = Counter(hand.replace("J", char_to_replace if jokers_wildcard else "J"))
        counts = tuple(sorted(c.values(), reverse=True))
        if counts == (5,):
            results.append(HandTypes.FIVE_OF_A_KIND)
        if counts == (4, 1):
            results.append(HandTypes.FOUR_OF_A_KIND)
        if counts == (3, 2):
            results.append(HandTypes.FULL_HOUSE)
        if counts == (3, 1, 1):
            results.append(HandTypes.THREE_OF_A_KIND)
        if counts == (2, 2, 1):
            results.append(HandTypes.TWO_PAIR)
        if counts == (2, 1, 1, 1):
            results.append(HandTypes.ONE_PAIR)
        else:
            results.append(HandTypes.HIGH_CARD)
    return max(results)


hands: list[tuple[str, str, int]] = []
for line in load_data(7).splitlines():
    hand, bid = line.split(" ")
    hands.append((hand, int(bid), get_type_rank(hand), [strengths.index(s) for s in hand]))

sorted_hands = sorted(hands, key=lambda x: (x[2], *x[3]))
s = 0
for rank, (_, bid, *_) in enumerate(sorted_hands):
    s += bid * (rank + 1)
print("p1", s)


new_strengths = "J23456789TQKA"
hands: list[tuple[str, str, int]] = []
for line in load_data(7).splitlines():
    hand, bid = line.split(" ")
    hands.append(
        (
            hand,
            int(bid),
            get_type_rank(hand, jokers_wildcard=True),
            [new_strengths.index(s) for s in hand],
        )
    )
sorted_hands = sorted(hands, key=lambda x: (x[2], *x[3]))
s = 0
for rank, (_, bid, *_) in enumerate(sorted_hands):
    s += bid * (rank + 1)
print("p2", s)
