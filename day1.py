with open(__file__[:-2]+"txt", "r") as f:
    lines = f.readlines()
    lines = map(str.strip, lines)

# pt 1
freqs = list(map(int, lines))
print(sum(freqs))

# pt 2
visited = set()
freq = 0
i = 0
while freq not in visited:
    visited.add(freq)
    freq += freqs[i]
    i += 1
    i %= len(freqs)

print(freq)
