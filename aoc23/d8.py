import math
from itertools import cycle

from .helpers import load_data

lines = load_data(8, test=False).splitlines()

sequence = cycle(lines[0])

nodes = {line[:3]: (line[7:10], line[12:15]) for line in lines[2:]}

c = 0
x = "AAA"
while True:
    if x == "ZZZ":
        break
    d = next(sequence)
    if d == "L":
        x = nodes[x][0]
    elif d == "R":
        x = nodes[x][1]
    c += 1

print("p1", c)


X = [n for n in nodes.keys() if n.endswith("A")]
lengths = []
for x in X:
    c = 0
    while True:
        if x.endswith("Z"):
            break
        d = next(sequence)
        x = nodes[x][0] if d == "L" else nodes[x][1]
        c += 1

    lengths.append(c)

print("p2", math.lcm(*lengths))
