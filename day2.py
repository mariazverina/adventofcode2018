from collections import Counter
import difflib


with open(__file__[:-2]+"txt", "r") as f:
    lines = f.readlines()
    lines = map(str.strip, lines)

lines = list(lines)

def freq_to_letter(s):
    c = Counter(s)
    ci = {v: k for k, v in c.items()}
    return ci

# part 1
ci = list(map(freq_to_letter, lines))
threes = sum(map(lambda x:3 in x, ci))
twos   = sum(map(lambda x:2 in x, ci))
print(threes * twos)

# part 2
def comp(a, b):
    pairs = list(zip(a,b))
    nd = sum([x != y for x, y in pairs])
    if nd == 1:
        common = [x if x == y else '' for x,y in pairs]
        print(''.join(common))



for i in range(len(lines)):
    for j in range(len(lines)):
        if(i<j):
            comp(lines[i], lines[j])


