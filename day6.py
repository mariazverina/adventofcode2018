from collections import Counter
from functools import reduce
import operator

with open(__file__[:-2]+"txt", "r") as f:
    lines = f.readlines()
    lines = list(map(str.strip, lines))

# part 1
class Point(object):
    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(%s,%s)"%(self.x, self.y)

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return abs(dx) + abs(dy)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __repr__(self):
        return str(self)

coords = [Point(*(map(int, s.split(', ')))) for s in lines]
w = max([p.x for p in coords]) + 1
h = max([p.y for p in coords]) + 1

def closest_point(coords, p):
    dists = sorted([(p.distance(q), q) for q in coords])
    if(dists[0][0] < dists[1][0]):
        return dists[0][1]
    return None

raster = [[-1 for y in range(h)] for x in range(w)]
for x in range(w):
    for y in range(h):
        raster[x][y] = closest_point(coords, Point(x,y))


m = reduce(operator.add, raster)
c = Counter(m)

boundary_points = raster[0] + raster[w-1] + [raster[x][0] for x in range(w)] +[raster[x][h-1] for x in range(w)]

for p in boundary_points:
    c.pop(p, None)

print(c.most_common(1))

# part 2

def close_enough(coords, p):
    dists = [p.distance(q) for q in coords]
    return sum(dists) < 10000

raster = [[0 for y in range(h)] for x in range(w)]
for x in range(w):
    for y in range(h):
        raster[x][y] = close_enough(coords, Point(x,y))

m = reduce(operator.add, raster)
print(sum(m))
