import re
from math import floor, prod

from .helpers import load_data

lines = load_data(6).splitlines()
time_limits, records = ([int(x) for x in re.split("[ ]+", line)[1:]] for line in lines)


s1 = []
for time_limit, record in zip(time_limits, records):
    n_combinations = 0
    for seconds_to_hold in range(time_limit):
        seconds_to_race = time_limit - seconds_to_hold

        total_distance = seconds_to_race * seconds_to_hold
        if total_distance > record:
            n_combinations += 1

    s1.append(n_combinations)

print("p1", prod(s1))

# now, time limit ~ O(10^7) and record ~ O(10^9)
# thus, brute force is not feasible
time_limit, record = (int("".join(re.split("[ ]+", line)[1:])) for line in lines)

# two equations:
#   y = (C - x) * x, which is a parabola
#   y = r (record)
# set them equal to each other
#   (C - x) * x = r
# solve for x:
#   (C-x) = r/x => C = r/x + x => x^2 - Cx + r = 0
# use quadratic formula to solve: x = (-b +- sqrt(b^2 - 4ac)) / 2a
# we have a = 1, b = -C, c = r

a = 1
b = -time_limit
c = record

solutions = [
    floor((-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)),
    floor((-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)),
]
span = max(solutions) - min(solutions)

print("p2", span)
