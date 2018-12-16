import unittest


class Grid(object):
    def __init__(self, serial):
        self.serial = serial
        self.cells = [[self.pval(x,y) for x in range(1, 301)] for y in range(1, 301)]

    def power(self, x, y):
        return self.cells[y-1][x-1]

    def pval(self, x, y):
        rack_id = x + 10
        p = (rack_id * y + self.serial) * rack_id
        return (p % 1000) // 100 - 5

    def square_power(self, left, top):
        ps = [self.power(left + x, top + y) for y in range(3) for x in range(3)]
        return sum(ps)

    def max_square(self):
        sp = [(self.square_power(x, y), (x, y)) for x in range(298) for y in range(298)]
        return max(sp)[1]

class GridTests(unittest.TestCase):

    def test_pval(self):
        self.assertEqual(Grid(8).pval(3,5), 4)

    def test_power(self):
        # Fuel cell at  122,79, grid serial number 57: power level -5.
        # Fuel cell at 217,196, grid serial number 39: power level  0.
        # Fuel cell at 101,153, grid serial number 71: power level  4.

        self.assertEqual(Grid(57).power(122,  79), -5)
        self.assertEqual(Grid(39).power(217, 196),  0)
        self.assertEqual(Grid(71).power(101, 153),  4)

    def test_square_power(self):
        self.assertEqual(Grid(18).square_power(33,45), 29)


    def test_max_square(self):
        self.assertEqual(Grid(18).max_square(), (33, 45))
        self.assertEqual(Grid(42).max_square(), (21, 61))

# if __name__ == '__main__':
print(Grid(7857).max_square())

unittest.main()


