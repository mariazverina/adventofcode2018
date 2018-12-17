class Scoreboard:
    def __init__(self):
        self.e1 = 0
        self.e2 = 1
        self.scores = [3, 7]

    def tick(self):
        s = self.scores[self.e1] + self.scores[self.e2]
        if s >= 10:
            self.scores.append(1)
        self.scores.append(s % 10)
        self.e1 += 1 + self.scores[self.e1]
        self.e2 += 1 + self.scores[self.e2]
        self.e1 %= len(self.scores)
        self.e2 %= len(self.scores)


    def print(self):
        print(self.scores)

    def check_sum(self, n):
        while(len(self.scores) < n + 10):
            self.tick()
        return ''.join(map(str, self.scores[n:n+10]))


s = Scoreboard()

for i in range(10**8):
    s.tick()

print(s.scores[9:19])

# If the Elves think their skill will improve after making 9 recipes,
#   the scores of the ten recipes after the first nine on the scoreboard would be 5158916779
#   (highlighted in the last line of the diagram).
# After 5 recipes, the scores of the next ten would be 0124515891.
# After 18 recipes, the scores of the next ten would be 9251071085.
# After 2018 recipes, the scores of the next ten would be 5941429882.

print(s.check_sum(9), "check")
print(s.check_sum(5), "check")
print(s.check_sum(18), "check")
print(s.check_sum(2018), "check")
print(s.check_sum(768071))

needle = [5, 9, 4, 1, 4, 2]
for i in range(len(s.scores)):
    if s.scores[i:i + 6] == needle:
        print("found", i)
        break

needle = [7, 6, 8, 0, 7, 1]
for i in range(len(s.scores)):
    if s.scores[i:i+6] == needle:
        print("found", i)
        break


