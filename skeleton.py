with open(__file__[:-2]+"txt", "r") as f:
    lines = f.readlines()
    lines = map(str.strip, lines)

print(list(lines))