from collections import Counter
import difflib


with open(__file__[:-2]+"txt", "r") as f:
    lines = f.readlines()
    lines = map(str.strip, lines)

lines = list(lines)

print(lines)

# def comp(a, b):
#     pairs = list(zip(a,b))
#     nd = sum([x != y for x, y in pairs])
#     if nd == 1:
#         common = [x if x == y else '' for x,y in pairs]
#         print(''.join(common))
#
#
#
# for i in range(len(lines)):
#     for j in range(len(lines)):
#         if(i<j):
#             comp(lines[i], lines[j])


