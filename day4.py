import re

with open(__file__[:-2]+"txt", "r") as f:
    lines = f.readlines()
    lines = map(str.strip, lines)

lines = sorted(lines)

# part 1
guard = 0
start = -1
sleep_time = {}
sleep_map = {}
for line in lines:
    m = re.match(r'\[1518-\d\d-\d\d \d\d:\d\d] Guard #(\d+) begins shift', line)
    if m:
        g = m.group(1)
        continue
    m = re.match(r'\[1518-\d\d-\d\d \d\d:(\d\d)] falls asleep', line)
    if m:
        start = int(m.group(1))
    m = re.match(r'\[1518-\d\d-\d\d \d\d:(\d\d)] wakes up', line)
    if m:
        end = int(m.group(1))
        if g in sleep_time:
            sleep_time[g] += end - start
        else:
            sleep_time[g] = end - start
        if not g in sleep_map:
            sleep_map[g] = {}
        for i in range(start, end):
            if i in sleep_map[g]:
                sleep_map[g][i] += 1
            else:
                sleep_map[g][i] = 1


def sleepy_minute(g, mins):
    invmap = zip(mins.values(), mins.keys())
    return sorted(invmap, reverse=True)[0]


inverse = zip(sleep_time.values(), sleep_time.keys())
sleepy = sorted(inverse, reverse=True)[0][1]
# invmap = zip(sleep_map[sleepy].values(), sleep_map[sleepy].keys())
# sleepy_minute = sorted(invmap, reverse=True)[0][1]
sm = sleepy_minute(sleepy, sleep_map[sleepy])
print(sleepy, sm, int(sleepy)*sm[1])

# part 2
sleepiest_minutes = [(sleepy_minute(k,v), k) for k,v in sleep_map.items()]
(freq, mm), g = (sorted(sleepiest_minutes)[-1])
print(int(g) * mm)




