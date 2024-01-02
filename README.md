# aoc23
 My solutions for the [Advent of Code 2023](https://adventofcode.com/2023) puzzles.

## Running
1. `pip install -r requirements.txt`
2. `python -m aoc23.d<day>`
    * Example: `python -m aoc23.d1`

## Solutions
- [Day 1: Trebuchet?!](#day-1-trebuchet)
- [Day 2: Cube Conundrum](#day-2-cube-conundrum)
- [Day 3: Gear Ratios](#day-3-gear-ratios)
- [Day 4: Scratchcards](#day-4-scratchcards)
- [Day 5: If You Give A Seed A Fertilizer](#day-5-if-you-give-a-seed-a-fertilizer)
- [Day 6: Wait for it](#day-6-wait-for-it)


### Day 1: Trebuchet!?

**Topic: Digit extraction**

Example data:
```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

For part 1, we are asked to extract the first and last digit of each line (in the case of a single digit, the first and last digit are the same). We then concatenate the two digits to form a new number, and return the sum of all these constructed numbers. No real magic here, just plain old Python stdlib `str.isdigit()` for discarding anything non-digitty.

For part two, we are asked to also handle digits that are spelled out (e.g. one, two, three, ...). The approach is almost the same, but we replace the spelled out versions with their corresponding digits before using the same `isdigit()` approach - i.e. replace `one` -> `1`, etc. But there are a few unfortunate cases that require us to change our approach slightly. For example, replacing digits in the string `oneight` will result in `1ight` or `on8`, depending on order of replacement. A quick fix is to "pad" the replacement strings, such that `one` -> `one1one`, etc. This preserves the original characters, and allows us to use `isdigit()` later on.


### Day 2: Cube Conundrum
**Topic: Counting and maxima**

Example data:
```
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
```

For part 1, we are asked to determine which of the games are feasible given a bag of 12 red cubes, 13 green cubes, and 14 blue cubes. If any of the individual rounds of each game (delimited by `;`) exceeds these constraints, the game is infeasible. We are asked to return the sum of game IDs as the answer.

For part 2, we are asked to figure out the fewest number of cubes of each color for every game. To do this, we just need to keep track of a "highscore" for each color.

### Day 3: Gear Ratios
**Topic: Grids and adjacency checks**

Example data:
```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```

For part 1, we are asked to find all numbers that are adjacent to symbols (diagonally counts, too). The result is simply the sum of all such numbers. For this approach, an initial pass of the grid is made to find all symbols and denote their positions. Then, a second pass is made to find all digits using regex and `\d+` to find all contiguous digits. For every regex hit, we try to see if any digits are tracked at any of the adjacent positions. If yes, then we add the digit to the result.

For part 2, we are asked to only consider the `*` symbol and find all occurrences of `*` that are adjacent to two numbers and return the sum of their products. The approach is similar to an "inverse" part 1. An initial pass is made to create a "number map" which maps from position -> number. Then, a second pass is made to find all `*` symbols. For every `*` symbol, we check if the adjacent positions contain numbers. If yes, we multiply the numbers and add the result to the final result.

### Day 4: Scratchcards
**Topic: Sets and set operations**

Example data:
```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```

For part 1, we are playing scratchcards. The first 5 numbers are the winning numbers, and the remaining 8 numbers are the numbers on hand. The score of each card is based on the amount of winning numbers found on hand. 0 numbers = 0 points, 1 number = 1 point, and each number beyond that doubles its resulting value. In other words, given `n` matching numbers, the card score is `2^(n-1)` if `n > 1`, 0 otherwise. Return the sum of all card scores.

For part 2, the rules are changed. Instead of obtaining points, winning scratchcards will award us with additional scratchcards (copies of the existing cards) equal to the number of winning numbers. The copies are of the subsequent cards, i.e. if card 10 has 5 winning numbers, we get one copy each of cards 11, 12, 13, 14, and 15. The approach is modified such that we now maintain a dict of card number -> list of cards. Initially, we have `card number -> [original card]` in the dict. We then start playing the cards *in ascending order*, and start adding copies of the cards to the dict. The dict is updated such that `card number -> [original card, copy 1, copy 2, ...]`. Copies are played along with the originals, and repeat the process until we have no more cards to play. Since the cards can only illicit copies of the subsequent cards, we only have to do a single pass of the cards. The final result is the total amount of scratchcards.


### Day 5: If You Give A Seed A Fertilizer
**Topic: Maps and ranges**

Example data:
```
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
```

For part 1, we are asked to map the "seed" values through a series of maps. The first map is a `seed-to-soil` map, which maps the seed values to soil values. The second map is a `soil-to-fertilizer` map, which maps the soil values to fertilizer values. This process continues for a few steps until we reach `humidity-to-location` (7 mapping steps in total). The lines in each map chunk describe ranges of values. For example, `50 98 2` describes the mapping `[98,100[ -> [50,52[`, Any values outside of the ranges proceed unchanged to the next map. We are asked to return the smallest resulting `location` amongst the input seeds.

The approach here is to first parse the maps as Python `range` objects with a corresponding "offset" value, which is what we should add to the input to correctly map it to the output. The `[98,100[ -> [50,52[` example from earlier has an offset of `-48`, since `50-98=-48`. It should be noted that these are half-open intervals, i.e. `range(100,103)` contains 100, but not 103. We can use the `in` operator when working with ranges, which is convenient. For each seed, we iterate through each of the seven mapping steps, modifying its value as we go along. For 4 input seeds and 7 mapping steps, we need to do 28 lookups in total. The minimum obtained value is returned as the result.

For part 2, we are told that we are not actually given 4 input seeds, but rather 2 entire *ranges* of input seeds. E.g. `79 14 55 13` corresponds to the two ranges `[79,93[` and `[55,68[`. We are still asked to return the smallest obtaiend location value. A naïve approach would be to simply evaluate every input seed in the given ranges. This is fine for the example data, but the real data contains ranges on the order of `O(10^9)`.

The updated approach is to process the seed ranges as python `range` objects, too. We then need to define a function which handles the "chopping up" of ranges. For instance, say we are given the input range `[1,11]` and a mapping step `[6,8], offset +10`. This results in three new ranges - *left*, *overlap* and *right*. (In general, we might end up with fewer than three subranges, if there is insufficient overlap). We need to remember to apply the offset to *overlap*, which just means that we add the offset value to the start and stop values of the range.
```
          input: [1  2  3  4  5  6  7  8   9 10 11]
map (offset +10):       |       [6  7  8]     |
                        |           |         |
                  [1 2 3 4 5]  [16 17 18] [9 10 11]
                     left        overlap    right
```

In python, something like this gets the job done:
```python
def compute_overlap(a: range, b: range) -> tuple[range | None, range | None, range | None]:
    overlap = range(max(a.start, b.start), min(a.stop, b.stop))
    left = range(a.start, overlap.start)
    right = range(overlap.stop, a.stop)

    return left or None, overlap or None, right or None
```

For every mapping step: maintain a queue (just a python list, really) of ranges that need to be processed. For each item in the queue, determine the overlap ranges (i.e. *left*,*overlap*,*right*). If there is an *overlap* range, add offset to the start/stop values and add it to the queue for the *next* mapping step - the potential left/right ranges are added to the queue of the *current* mapping step. If there is no *overlap* range, we just add the unmodified range to the queue for the *next* mapping step.

### Day 6: Wait for it
**Topic: 2nd degree polynomials**


Example data:
```
Time:      7  15   30
Distance:  9  40  200
```
It describes three races. Each race has a time limit (e.g. 7ms, 15ms, 30ms) and a minimum distance to beat (e.g. 9mm, 40mm, 200mm).
We have a toy boat with initial speed of 0 mm/ms. We can "wind up" the toy boat - each whole millisecond spent winding it up, its speed upon release is increased by 1 mm/ms.

For part 1, we are asked to figure out - for every race - how many different durations of "winding up" will beat the minimum distance within the time limit. For example, the first race has a time limit of 7ms. We can spend anywhere from 0ms to 7ms winding up the toy boat. If we spend 3ms winding it up, it will have a speed of 3mm/ms for a duration of 4ms, which means it will travel 12mm (which is > 9, thus beating the minimum distance). For example race 1, holding the button for [2,3,4,5]ms will win the race.

This can be naïvely solved using brute force - for every race, evaluate how far the boat will travel for every duration in the range [0, time_limit]. Denote how many of them beat the minimum distance, and return the product of all such counts.

For part 2, we are told that the numbers actually only describe one race - with a time limit of 71530ms and minimum distance of 940200mm. For the example data, the brute force has to evaluate 71530 winding durations. For the real input data, this is on the order of 10^7, which is too many.

Instead, we should look at the problem differently. The travel duration for the winding duration `x` is computed as `travel distance = (time limit - x) * x`. This can be recognized as a 2nd degree polynomial function, which fortunately has a closed form solution.
Let's rewrite the function as `f(x) = (C-x) * x`, with `C` denoting the time limit. We are interested in finding all `x` such that `f(x) > minimum distance`. To do this, we can simply find the two points where `f(x) = minimum distance`, and we will have obtained the full range of `x` for which the condition holds.

Thus: `f(x) = minimum distance => (C-x) * x = r`. Solving for x: `(C-x) * x = r => C-x) = r/x => C = r/x + x => x^2 - Cx + r = 0`
We can use the quadratic formula with `a = 1, b = -C, c = r` to find the two roots, and we return the absolute difference between the two roots as the result (with some rounding, since the problem deals with integers).
