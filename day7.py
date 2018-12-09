import re
from functools import reduce
import operator

with open(__file__[:-2]+"txt", "r") as f:
    lines = f.readlines()
    lines = list(map(str.strip, lines))

# list of tuples (A, B) meaning A preceds B
deps = [re.match(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.', line).groups() for line in lines]


class Plan:
    def __init__(self, deps):
        items = set(reduce(operator.add, deps))
        print(sorted(items), len(items))
        self.deptree = {k: set() for k in items}
        for dep in deps:
            pre, post = dep
            self.add_dep(pre, post)

    def add_dep(self, pre, post):
        self.deptree[post].add(pre)

    def dep_list(self):
        return sorted(self.deptree.items())

    def p_queue(self):
        return sorted(zip(self.deptree.values(), self.deptree.keys()), key=lambda x:(len(x[0]), x))

    def __bool__(self):
        return bool(self.deptree)

    def process(self, hipri):
        self.deptree.pop(hipri)
        for s in self.deptree.values():
            if hipri in s:
                s.remove(hipri)

    def next_task(self):
        return self.p_queue()[0][1]


plan = Plan(deps)

# print(deps)
# print(plan.dep_list())


path = ''
while plan:
    # print("q", plan.p_queue())
    task = plan.next_task()
    plan.process(task)
    # print("popped", task, "\n", plan.dep_list())
    path += task


print(path)



