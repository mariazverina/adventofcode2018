from collections import defaultdict
import re
player_count = 491
high_marble = 71058

with open(__file__[:-2]+"txt", "r") as f:
    lines = f.readlines()
    lines = list(map(str.strip, lines))

games = [tuple(map(int, re.match(r'(\d+) players; last marble is worth (\d+) points.*', line).groups())) for line in lines]
print(games)

class Game:
    def __init__(self, player_count, high_marble):
        self.player_count = player_count
        self.high_marble = high_marble
        self.marbles = [0]
        self.current_marble = 0
        self.current_player = 0
        self.scores = defaultdict(int)

    def print_board(self):
        print(self)

    def __repr__(self):
        marble_rep = ["{:3} ".format(n) for n in self.marbles]
        marble_rep[self.current_marble] = "{:3}*".format(self.marbles[self.current_marble])
        return "[{:3}]".format(self.current_player + 1) + ''.join(marble_rep)

    def play(self):
        # self.print_board()
        for i in range(1, self.high_marble+1):
            if not i % 23:
                self.current_marble = (self.current_marble - 7) % len(self.marbles)
                m = self.marbles.pop(self.current_marble)
                self.scores[self.current_player] += i + m
            else:  #standard play
                # next point with wrap
                insert_point = self.current_marble + 2
                if insert_point > len(self.marbles):
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

# 9 players; last marble is worth 25 points: high score is 32
# 10 players; last marble is worth 1618 points: high score is 8317
# 13 players; last marble is worth 7999 points: high score is 146373
# 17 players; last marble is worth 1104 points: high score is 2764
# 21 players; last marble is worth 6111 points: high score is 54718
# 30 players; last marble is worth 5807 points: high score is 37305
# 491 players; last marble is worth 71058 points
