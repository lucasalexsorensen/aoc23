import re
from collections import defaultdict

from .helpers import load_data

data = load_data(4).splitlines()

s1 = 0
for line in data:
    line = line.split(": ")[1]
    winning_chunk, my_chunk = line.split("|")

    winning_numbers = {int(x) for x in winning_chunk.split(" ") if x}
    my_numbers = {int(x) for x in my_chunk.split(" ") if x}

    n = len(my_numbers & winning_numbers)
    if n > 0:
        s1 += 2 ** (n - 1)

print("p1", s1)

cards = defaultdict(list)

for line in data:
    card_chunk, line = line.split(": ")
    winning_chunk, my_chunk = line.split("|")

    card_no = int(re.search(r"\d+", card_chunk).group(0))

    winning_numbers = {int(x) for x in winning_chunk.split(" ") if x}
    my_numbers = {int(x) for x in my_chunk.split(" ") if x}

    cards[card_no] += [(winning_numbers, my_numbers)]


for card_no in cards:
    for winning_numbers, my_numbers in cards[card_no]:
        score = len(my_numbers & winning_numbers)

        for i in range(card_no + 1, card_no + score + 1):
            # cards[i] += [cards[i][0]]
            cards[i].append(cards[i][0])


s2 = sum(len(cards) for cards in cards.values())
print("p2", s2)
