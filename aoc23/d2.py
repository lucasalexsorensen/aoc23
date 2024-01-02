from .helpers import load_data

data = load_data(2)

sum = 0
sum_p2 = 0
for line in data.splitlines():
    game, line_bag = line.split(":")
    game = int(game[5:])

    sets = []
    for set in line_bag.split(";"):
        s = [0, 0, 0]
        for draw in set.split(", "):
            count, color = draw.strip().split(" ")
            count = int(count)
            idx = {"red": 0, "green": 1, "blue": 2}[color]
            s[idx] = count
        sets.append(s)

    requirements = [12, 13, 14]

    for s in sets:
        if any([s[i] > requirements[i] for i in range(3)]):
            break
    else:
        sum += game

    max_r = 0
    max_g = 0
    max_b = 0
    for s in sets:
        max_r = max(max_r, s[0])
        max_g = max(max_g, s[1])
        max_b = max(max_b, s[2])

    power = max_r * max_g * max_b
    sum_p2 += power

print("p1", sum)

print("p2", sum_p2)
