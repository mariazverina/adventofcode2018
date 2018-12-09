with open(__file__[:-2]+"txt", "r") as f:
    lines = f.readlines()
    lines = list(map(str.strip, lines))

print(lines)