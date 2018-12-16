import re

with open(__file__[:-2]+"txt", "r") as f:
    world = f.readline()
    f.readline()
    lines = f.readlines()
    lines = list(map(str.strip, lines))

world = re.match(r'initial state: ([.#]+)', world).group(1)


def evolve(world, xform_map):
    chunks = map(lambda x: ''.join(x), zip(world, world[1:], world[2:], world[3:], world[4:]))
    return '..' +''.join([xform_map[c] for c in chunks]) + '..'

def sum_pot(world, offset):
    pots = zip(world, range(offset, offset + len(world) + 1))
    return sum([i for (f,i) in pots if f == '#'])

xform_map = {}
for line in lines:
    m = re.match(r'([.#]+) => ([.#])', line)
    xform_map[m.group(1)] = m.group(2)

offset = -50
pad = "." * 100
world = pad + world + pad

print(sorted(xform_map.items()))


for i in range(20):
    world = evolve(world, xform_map)


print(world)
print(sum_pot(world, offset))

for i in range(100000):
    world = evolve(world, xform_map)
    # print(world[50:])

print(world)