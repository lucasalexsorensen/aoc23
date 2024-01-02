from .helpers import load_data

data = load_data(1)

sum = 0
for line in data.splitlines():
    digits = list(char for char in line if char.isdigit())
    d1, d2 = digits[0], digits[-1]
    sum += int(d1 + d2)
print("p1", sum)


T = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
    "zero": "zero0zero",
}


sum = 0
for line in data.splitlines():
    for p, r in T.items():
        line = line.replace(p, r)
    digits = list(char for char in line if char.isdigit())
    d1, d2 = digits[0], digits[-1]
    sum += int(d1 + d2)
print("p2", sum)
