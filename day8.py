with open(__file__[:-2]+"txt", "r") as f:
    line = f.readline()

stream = iter(map(int, line.split()))


class Node:
    def __init__(self, parent=None):
        self.children = []
        self.metadata = []
        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0

    def add_node(self, n):
        self.children.append(n)

    def add_meta(self, m):
        self.metadata.append(m)

    def __repr__(self):
        desc = ["\t" * self.depth + "Node - meta = " + str(self.metadata) + "V: " + str(self.value())] + [repr(c) for c in self.children]
        return "\n".join(desc)

    def check_sum(self):
        return sum(self.metadata) + sum([c.check_sum() for c in self.children])

    def value(self):
        if not self.children:
            return sum(self.metadata)

        v = 0
        for i in self.metadata:
            if i < 1 or i > len(self.children):
                continue
            v += self.children[i-1].value()
        return v


def read_node(stream, parent=None):
    n = Node(parent)
    node_count = next(stream)
    meta_count = next(stream)
    for _ in range(node_count):
        n.add_node(read_node(stream, n))
    for _ in range(meta_count):
        n.add_meta(next(stream))
    return n


tree = read_node(stream)
print(tree)
print(tree.check_sum())
print(tree.value())

