import re
from functools import reduce
import operator

with open(__file__[:-2]+"txt", "r") as f:
    lines = f.readlines()
    lines = list(map(str.strip, lines))

# list of tuples (A, B) meaning A preceds B
deps = [re.match(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.', line).groups() for line in lines]

items = set(reduce(operator.add, deps))
print(sorted(items), len(items))

deptree = {k : set() for k in items}

for dep in deps:
    pre, post = dep
    deptree[post].add(pre)

print(deps)
print(sorted(deptree.items()))

class Plan:
    def __init__(self):
        pass



path = ''
while deptree:
    q  = sorted(zip(deptree.values(), deptree.keys()), key=lambda x:(len(x[0]), x))
    hipri = q[0][1]
    print("q", q)
    deptree.pop(hipri)
    for s in deptree.values():
        if hipri in s:
            s.remove(hipri)
    print("popped", hipri, "\n", sorted(deptree.items()))
    path += hipri


print(path)



