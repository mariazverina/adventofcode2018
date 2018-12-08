from collections import Counter
import string

with open(__file__[:-2]+"txt", "r") as f:
    polymer = f.readline()

# part 1
def matches(c1, c2):
    if c1 is None:
        return False
    c1,c2 = sorted([c1,c2])
    return c1.isupper() and c2.islower() and c1.lower() == c2

def munch(polymer):
    xform = '-'
    prev = polymer[0]
    for i in range(1, len(polymer)):
        c = polymer[i]
        if matches(prev, c):
            prev = xform[-1]
            xform = xform[:-1]
            continue
        xform += prev
        prev = c
    xform = xform[1:] + prev
    return xform

def react(polymer):
    while(len(polymer)):
        xform = munch(polymer)
        if xform == polymer:
            break
        polymer = xform
    return polymer

# print(polymer,repr(munch(polymer)))
# part 1
xform = react(polymer)
print(len(xform))

# part 2
results = []
for c in string.ascii_lowercase:
    x2 = xform.replace(c,'').replace(c.upper(),'')
    x3 = react(x2)
    r = (len(x3), c)
    results.append(r)

print(min(results))



