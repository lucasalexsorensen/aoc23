import re
from itertools import product

from .helpers import load_data

grid = []

for line in load_data(3).splitlines():
    grid.append(line.strip())


symbols = {}

number_map = {}

for i, row in enumerate(grid):
    for m in re.finditer(r"[^\d.]", row):
        symbols[(i, m.start())] = m.group(0)

s1 = 0
for i, row in enumerate(grid):
    for num in re.finditer(r"\d+", row):
        rows_to_check = range(i - 1, i + 2)
        cols_to_check = range(num.start() - 1, num.end() + 1)
        for r, c in product(rows_to_check, cols_to_check):
            if (r, c) in symbols:
                s1 += int(num.group())
                for cc in range(num.start(), num.end()):
                    number_map[(i, cc)] = int(num.group())
                break
print("p1:", s1)

star_symbols = {k: v for k, v in symbols.items() if v == "*"}


s2 = 0
for r, c in star_symbols.keys():
    nums = [
        number_map.get((rr, cc)) for rr, cc in product(range(r - 1, r + 2), range(c - 1, c + 2))
    ]
    nums = list(set(filter(bool, nums)))
    if len(nums) == 2:
        s2 += nums[0] * nums[1]

print("p2", s2)
