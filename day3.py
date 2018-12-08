import re
from collections import Counter


with open(__file__[:-2]+"txt", "r") as f:
    lines = f.readlines()
    lines = map(str.strip, lines)

lines = list(lines)

# part 1
fabric = dict()

for line in lines:
    (n, x, y, w, h) = map(int, re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line).groups())
    for a in range(w):
        for b in range (h):
            p = (x+a, y+b)
            fabric[p] = 'X' if p in fabric else '.'

print(Counter(fabric.values()))

# part 2
def valid(fabric, x, y, w, h):
    for a in range(w):
        for b in range(h):
            p = (x + a, y + b)
            if fabric[p] == 'X':
                return False
    return True

for line in lines:
    (n, x, y, w, h) = map(int, re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line).groups())
    if valid(fabric, x, y, w, h):
        print("valid claim", n)



