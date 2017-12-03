class SpiralMemory(object):
    spiral = [[1]]
    count = 1
    location = 1

    steps = 0

    def __init__(self, end_location):
        self.location = end_location
        # We are always calculating a full iteration
        while end_location > self.count:
            self.spiral.insert(0, list())
            self.spiral.append(list())

            self.spiral[len(self.spiral)-2].append(self.count+1)
            self.count += 1

            outer = len(self.spiral) - 3

            while outer > -1:
                self.count += 1
                self.spiral[outer].append(self.count)
                outer -= 1

            while len(self.spiral[0]) < len(self.spiral):
                self.count += 1
                self.spiral[0].insert(0, self.count)

            inner = 1
            while inner < len(self.spiral):
                self.count += 1
                self.spiral[inner].insert(0, self.count)
                inner += 1

            while len(self.spiral[len(self.spiral) - 1]) < len(self.spiral):
                self.count += 1
                self.spiral[len(self.spiral) - 1].append(self.count)

    def _get_row(self, number):
        row_number = 0
        for row in self.spiral:
            if number in row:
                return row_number
            else:
                row_number += 1

    def get_steps(self):
        if self.count == 1:
            return 0
        else:
            sy = self._get_row(self.location)
            ey = self._get_row(1)
            sx = self.spiral[sy].index(self.location)
            ex = self.spiral[ey].index(1)

            return abs(ex - sx) + abs(ey - sy)


def test_spiral_memory_1():
    sm = SpiralMemory(1)
    assert sm.get_steps() == 0

def test_spiral_memory_2():
    sm = SpiralMemory(12)
    assert sm.get_steps() == 3

def test_spiral_memory_3():
    sm = SpiralMemory(23)
    assert sm.get_steps() == 2

def test_spiral_memory_4():
    sm = SpiralMemory(1024)
    assert sm.get_steps() == 17

if __name__ == '__main__':
    sm = SpiralMemory(361527)
    print(sm.get_steps())
