from collections import defaultdict
import re
import time

player_count = 491
high_marble = 71058

with open(__file__[:-2]+"txt", "r") as f:
    lines = f.readlines()
    lines = list(map(str.strip, lines))

games = [tuple(map(int, re.match(r'(\d+) players; last marble is worth (\d+) points.*', line).groups())) for line in lines]
print(games)

# implements windows to optimise for locality of access

class MarbleList:
    WINDOWSIZE = 10000

    def __init__(self, marbles):
        # self.marbles = marbles
        self.windowed = False
        self.window_offset = 0
        self.window = list(marbles)
        self.head = []
        self.tail = []
        self.cached_length = len(self.window)
        # self.shadow = list(marbles)

    def marbles_list(self):
        return self.head + self.window + self.tail

    def marble_at(self, i):
        return self.marbles_list()[i]

    def len(self):
        # if sum(self.shadow) != sum(self.head) + sum(self.window) + sum(self.tail):
        #     exit("fail")
        return self.cached_length

    def make_window(self, i):
        self.windowed = True
        self.window_offset = max(0, i-100)
        window_length = min(len(self.window) - self.window_offset, self.WINDOWSIZE)
        self.head = self.window[:self.window_offset]
        self.tail = self.window[self.window_offset + window_length:]
        self.window = self.window[self.window_offset:self.window_offset + window_length]
        # print("make window", self.window_offset, window_length, len(self.head), len(self.window), len(self.tail), self.len(), len(self.shadow))

    def remake_window(self, i):
        print("remake", self.len(), len(self.window), i)
        self.window = self.head + self.window + self.tail
        # if self.window != self.shadow:
        #     print("remake error")
        self.window_offset = 0
        self.make_window(i)

    def check_window(self, i):
        if not self.windowed and len(self.window) < self.WINDOWSIZE:
            return False
        if not self.windowed:
            self.make_window(i)
        if i < self.window_offset or i >= self.window_offset + len(self.window):
            self.remake_window(i)

    def pop(self, i):
        self.check_window(i)
        # if len(self.window) < 200:
        #     print("", self.window,"\n", self.shadow)
        # r = self.shadow.pop(i)
        q = self.window.pop(i - self.window_offset)
        # if r != q:
        #     print("pop error", i, self.window_offset)
        self.cached_length -= 1
        return q

    def insert(self, i, item):
        self.check_window(i)
        self.window.insert(i - self.window_offset, item)
        self.cached_length += 1
        # self.shadow.insert(i, item)

class Game:
    def __init__(self, player_count, high_marble):
        self.player_count = player_count
        self.high_marble = high_marble
        self.marbles = MarbleList([0])
        self.current_marble = 0
        self.current_player = 0
        self.scores = defaultdict(int)

    def print_board(self):
        print(self)

    def __repr__(self):
        marble_rep = ["{:3} ".format(n) for n in self.marbles.marbles_list()]
        marble_rep[self.current_marble] = "{:3}*".format(self.marbles.marble_at(self.current_marble))
        return "[{:3}]".format(self.current_player + 1) + ''.join(marble_rep)

    def play(self):
        # self.print_board()
        for i in range(1, self.high_marble+1):
            if not i % 10000:
                print("=>", i / 10000, time.time())
            if not i % 23:
                self.current_marble = (self.current_marble - 7) % self.marbles.len()
                m = self.marbles.pop(self.current_marble)
                self.scores[self.current_player] += i + m
            else:  #standard play
                # next point with wrap
                insert_point = self.current_marble + 2
                if insert_point > self.marbles.len():
                    insert_point = 1

                # standard play
                self.marbles.insert(insert_point, i)
                self.current_marble = insert_point
            # self.print_board()

            self.current_player += 1
            self.current_player %= self.player_count
        # print(self.scores)
        return max(self.scores.values())



for p, m in games:
    g = Game(p, m)
    print(p, m, g.play())

# for m in range(2,6):
#     g = Game(491, 10**m)
#     print(p, 10**m, g.play())

# 9 players; last marble is worth 25 points: high score is 32
# 10 players; last marble is worth 1618 points: high score is 8317
# 13 players; last marble is worth 7999 points: high score is 146373
# 17 players; last marble is worth 1104 points: high score is 2764
# 21 players; last marble is worth 6111 points: high score is 54718
# 30 players; last marble is worth 5807 points: high score is 37305
# 491 players; last marble is worth 71058 points
