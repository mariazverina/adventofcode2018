import unittest


class Grid(object):
    def __init__(self, serial):
        self.serial = serial
        self.cache = {}
        self.cells = [[self.pval(x,y) for x in range(1, 301)] for y in range(1, 301)]

    def power(self, x, y):
        return self.cells[y-1][x-1]

    def pval(self, x, y):
        rack_id = x + 10
        p = (rack_id * y + self.serial) * rack_id
        return (p % 1000) // 100 - 5

    def sub_sum(self, x, y, w, h):
        CHUNK = 4
        if (x, y, w, h) in self.cache:
            return self.cache[(x, y, w, h)]
        if h > CHUNK:
            self.cache[(x, y, w, h)] = self.sub_sum(x, y, w, CHUNK) + self.sub_sum(x, y+CHUNK, w, h-CHUNK)
            return self.cache[(x, y, w, h)]
        if w > CHUNK:
            self.cache[(x, y, w, h)] = self.sub_sum(x, y, CHUNK, h) + self.sub_sum(x+CHUNK, y, w-CHUNK, h)
            return self.cache[(x, y, w, h)]

        ps = [self.power(x + xx, y + yy) for yy in range(h) for xx in range(w)]
        s = sum(ps)
        self.cache[(x, y, w, h)] = s
        return s


    def square_power(self, left, top, size = 3):
        return self.sub_sum(left, top, size, size)


    def max_square(self, size = 3):
        return self.max_square_with_power(size)[1]

    def max_square_with_power(self, size):
        sp = [(self.square_power(x, y, size), (x, y), size) for x in range(301 - size) for y in range(301 - size)]
        print("size =", size, max(sp))
        return max(sp)

    def max_square_any(self):
        s = sorted([self.max_square_with_power(i) + tuple([i]) for i in range(3, 20)]) # heuristic of 20 as expected value of large squares tends to be negative
        print(s)
        return s[-1]

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

    def test_max_square_any(self):
        # For grid serial number 18, the largest total square (with a total power of 113) is 16x16 and has a top-left corner of 90,269, so its identifier is 90,269,16.
        # For grid serial number 42, the largest total square (with a total power of 119) is 12x12 and has a top-left corner of 232,251, so its identifier is 232,251,12.
        self.assertEqual(Grid(18).max_square_any(), ( 90,269,16))
        self.assertEqual(Grid(42).max_square_any(), (232,251,12))

# if __name__ == '__main__':
print(Grid(7857).max_square())

print(Grid(18).square_power(33, 45, 29))
print(Grid(18).square_power(90, 269, 16))
# print(Grid(18).max_square_any())
print(Grid(7857).max_square_any())

# unittest.main()


