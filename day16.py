import re
import operator

samples = []
with open(__file__[:-2]+"txt", "r") as f:
    line = f.readline().strip()
    while len(line):
        before = tuple(map(int, re.match(r'Before: \[(\d+), (\d+), (\d+), (\d+)\]', line).groups()))
        op = tuple(map(int, f.readline().split()))
        after = tuple(map(int, re.match(r'After:  \[(\d+), (\d+), (\d+), (\d+)\]', f.readline()).groups()))
        f.readline()
        samples.append((before, op, after))
        line = f.readline().strip()

    f.readline() # 2 blank lines before program starts
    lines = f.readlines()
    lines = list(map(str.strip, lines))

# print(lines)

def opr(r, op, f):
    r[op[3]] = f(r[op[1]], r[op[2]])

def opi(r, op, f):
    r[op[3]] = f(r[op[1]], op[2])
    pass

def addr(r, op):
    opr(r, op, operator.add)

def addi(r, op):
    opi(r, op, operator.add)

def mulr(r, op):
    opr(r, op, operator.mul)

def muli(r, op):
    opi(r, op, operator.mul)

def banr(r, op):
    opr(r, op, operator.and_)

def bani(r, op):
    opi(r, op, operator.and_)

def borr(r, op):
    opr(r, op, operator.or_)

def bori(r, op):
    opi(r, op, operator.or_)

def setr(r, op):
    r[op[3]] = r[op[1]]

def seti(r, op):
    r[op[3]] = op[1]

def gtir(r, op):
    r[op[3]] = int(op[1] > r[op[2]])

def gtri(r, op):
    r[op[3]] = int(r[op[1]] > op[2])

def gtrr(r, op):
    r[op[3]] = int(r[op[1]] > r[op[2]])

def eqir(r, op):
    r[op[3]] = int(op[1] == r[op[2]])

def eqri(r, op):
    r[op[3]] = int(r[op[1]] == op[2])

def eqrr(r, op):
    r[op[3]] = int(r[op[1]] == r[op[2]])

def execute(r, op, instr):
    r = list(r)
    instr(r, op)
    return tuple(r)



r = (3,2,1,1)
expected = (3,2,2,1)
op = (9,2,1,2)

opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

# print(samples, len(samples))

n = 0
for r, op, expected in samples:
    matches = sum([execute(r, op, f) == expected for f in opcodes])
    if matches >= 3:
        n += 1


print("{} opcodes have 3+ matches".format(n))



# execute(r, op, mulr)
# execute(r, op, addi)
# execute(r, op, seti)
