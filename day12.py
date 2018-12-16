import re

with open(__file__[:-2]+"txt", "r") as f:
    world = f.readline()
    f.readline()
    lines = f.readlines()
    lines = list(map(str.strip, lines))

state = re.match(r'initial state: ([.#]+)', world).group(1)

class World:
    def __init__(self, world, xform_map, trim=True):
        self.xform = xform_map
        self.state = world
        self.offset = 0
        self.should_trim = trim

    def trim(self):
        chunks = self.state.split('#')
        self.offset += len(chunks[0])
        chunks[0] = ''
        chunks[-1] = ''
        self.state = '#'.join(chunks)

    def evolve(self):
        world = '....' + self.state + '....'
        self.offset -= 4
        chunks = map(lambda x: ''.join(x), zip(world, world[1:], world[2:], world[3:], world[4:]))
        self.state = '..' + ''.join([self.xform[c] for c in chunks]) + '..'
        if self.should_trim:
            self.trim()
        return self.state

    def sum_pot(self):
        pots = zip(self.state, range(self.offset, self.offset + len(self.state) + 1))
        s = [i for (f, i) in pots if f == '#']
        return sum(s)

    def print(self, tag=""):
        print(tag, self.state, self.offset, self.sum_pot())

xform_map = {}
for line in lines:
    m = re.match(r'([.#]+) => ([.#])', line)
    xform_map[m.group(1)] = m.group(2)

print(sorted(xform_map.items()))

# part 1
world = World(state, xform_map)
for i in range(20):
    world.evolve()
    world.print()

print(world.sum_pot())


# part 2
world = World(state, xform_map)

spd = 0

for i in range(120):
    prev = world.sum_pot()
    world.evolve()
    spd = prev - world.sum_pot()
    world.print((i+1, spd))

# after 109 iterations we have a stable pattern which shifts by one pixel every iteration
# this means sum function grows monotonically by 65

# f(120) => 8756
# f(0) = 8756 - 65 * 120 = 956
# f(50b) = 50b * 65 + 956

print(50*10**9*65+956)
