import itertools
import random

#a)
def zero_one_infinite_iterator():
    while True:
        yield from [0, 1]

for i in itertools.islice(zero_one_infinite_iterator(), 10):
    print(i)

#b)
def random_direction_iterator():
    directions = ["N", "E", "S", "W"]
    while True:
        yield random.choice(directions)

for j in itertools.islice(random_direction_iterator(), 10):
    print(j)

#c)
def day_of_week_iterator():
    days_of_week = [0, 1, 2, 3, 4, 5, 6]
    while True:
        yield from itertools.cycle(days_of_week)

for k in itertools.islice(day_of_week_iterator(), 10):
    print(k)