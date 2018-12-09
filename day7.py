import re
from functools import reduce
import operator

with open(__file__[:-2]+"txt", "r") as f:
    lines = f.readlines()
    lines = list(map(str.strip, lines))

# list of tuples (A, B) meaning A preceds B
deps = [re.match(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.', line).groups() for line in lines]


class Plan:
    def __init__(self, deps, worker_limit=1):
        items = set(reduce(operator.add, deps))
        print(sorted(items), len(items))
        self.deptree = {k: set() for k in items}
        for dep in deps:
            pre, post = dep
            self.add_dep(pre, post)
        self.worker_limit = worker_limit
        self.clock = 0
        self.task_order = ""
        self.executing = {}

    def add_dep(self, pre, post):
        self.deptree[post].add(pre)

    def dep_list(self):
        return sorted(self.deptree.items())

    def p_queue(self):
        return sorted(zip(self.deptree.values(), self.deptree.keys()), key=lambda x:(len(x[0]), x))

    def __bool__(self):
        return bool(self.deptree) or bool(self.executing)

    def start(self, task):
        self.deptree.pop(task)
        self.executing[task] = self.clock + self.task_duration(task)
        self.task_order += task

    def complete(self, task):
        for s in self.deptree.values():
            if task in s:
                s.remove(task)
        self.executing.pop(task)

    def process(self, task):
        self.start(task)
        self.complete(task)


    def next_task(self):
        return self.p_queue()[0][1]

    def log(self, what, label=""):
        print(self.clock, label, what)

    def tick(self):
        # clean up finished tasks
        completed_tasks = [task for task, time in self.executing.items() if time == self.clock]
        self.log(completed_tasks, "completed")

        for t in completed_tasks:
            self.complete(t)

        self.log(self.executing, "exec")

        # schedule new tasks
        ready = self.ready_tasks()
        self.log(ready, "ready")

        while len(self.executing) < self.worker_limit and ready:
            t = ready.pop(0)
            self.start(t)

        self.log(self.executing, "exec")

        if self.executing:
            self.clock = min(self.executing.values())

    def ready_tasks(self):
        q = self.p_queue()
        return [t for d,t in q if not len(d)]

    def task_duration(self, task):
        return ord(task) - ord('A') + 61



plan = Plan(deps)

# print(deps)
# print(plan.dep_list())

# part 1
while plan:
    print("q", plan.p_queue())
    task = plan.next_task()
    plan.process(task)
    print("popped", task, "\n", plan.dep_list())

print(plan.task_order)

# part 2
plan = Plan(deps, 5)

while plan:
    plan.tick()



