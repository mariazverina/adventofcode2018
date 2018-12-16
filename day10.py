import re
from functools import reduce
from collections import defaultdict
import operator
with open(__file__[:-2]+"txt", "r") as f:
    lines = f.readlines()
    lines = list(map(str.strip, lines))

stars = [tuple(map(int, re.match(r'position=< *(\-?\d+), *(\-?\d+)> velocity=< *(\-?\d+), *(\-?\d+)>', line).groups())) for line in lines]


def hdist(stars):
    s = sorted(stars)
    return s[-1][0] - s[0][0]

def vdist(stars):
    s = sorted(map(lambda x:x[1], stars))
    return s[-1] - s[0]


def min_pattern(stars):
    mindx = 9999999
    mindy = 9999999
    t = 0

    while True:
        stars = [(x+vx, y+vy, vx, vy) for x, y, vx, vy in stars]
        v = vdist(stars)
        h = hdist(stars)
        if mindy < v:
            print("miny at", t)
        else:
            mindy = v
        if mindx < h:
            print("minx at", t)
        else:
            mindx = h
        if v > mindy and h > mindx:
            break
        t += 1
    print(min(stars), max(stars))

    return t

# print(stars, t)
# min_pattern(stars)

# pattern is smallest at t = 10559. Hence writing will emerge around this time


def print_stars(stars, t):
    print('='*60)
    stars = [(x + t * vx, y + t * vy, vx, vy) for x, y, vx, vy in stars]

    minx = min(map(lambda x:x[0], stars))
    miny = min(map(lambda x:x[1], stars))
    maxx = max(map(lambda x:x[0], stars))
    maxy = max(map(lambda x:x[1], stars))

    raster = defaultdict(lambda: " ")
    for x, y, _, _ in stars:
        raster[(x,y)] = '#'

    # width = maxx - minx + 1
    # height = maxy - miny + 1

    bitmap = [[raster[(x,y)] for x in range(minx, maxx+1)] for y in range(miny, maxy+1)]
    print('\n'.join([''.join(line) for line in bitmap]))

    print("t =", t, "  bounds =", minx, miny, maxx, maxy)


# part 1 & 2
# NBHEZHCJ
print_stars(stars, min_pattern(stars))

