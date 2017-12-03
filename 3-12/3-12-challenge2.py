# DOES NOT WORK
class SpiralMemory(object):
    spiral = [[1]]
    count = 1
    location = [1, 1]

    def __init__(self, end_location):
        # We are always calculating a full iteration
        while end_location > self.count:
            self.spiral.insert(0, list())
            self.spiral.append(list())

            self.spiral[len(self.spiral)-2].append(self.count)

            outer = len(self.spiral) - 3

            while outer > -1:
                self.update_location('U')
                self.count = self.get_new_count()
                self.spiral[outer].append(self.count)
                outer -= 1

            while len(self.spiral[0]) < len(self.spiral):
                self.update_location('L')
                self.count = self.get_new_count()
                self.spiral[0].insert(0, self.count)

            inner = 1
            while inner < len(self.spiral):
                self.update_location('D')
                self.count = self.get_new_count()
                self.spiral[inner].insert(0, self.count)
                inner += 1

            while len(self.spiral[len(self.spiral) - 1]) < len(self.spiral):
                self.update_location('R')
                self.count = self.get_new_count()
                self.spiral[len(self.spiral) - 1].append(self.count)

    def get_new_count(self):
        new_count = 0
        for x_loc in range(self.location[1]-1, self.location[1]+2):
            if x_loc > -1:
                for y_loc in range(self.location[0]-1, self.location[0]+2):
                    if y_loc > -1:
                        try:
                            new_count += self.spiral[y_loc][x_loc]
                        except IndexError:
                            pass

        return new_count

    def update_location(self, direction):
        if direction == 'U':
            self.location[0] -= 1
        elif direction == 'L':
            self.location[1] -= 1
        elif direction == 'D':
            self.location[0] += 1
        elif direction == 'R':
            self.location[1] += 1

    def get_number(self):
        rownum = 0
        for row in self.spiral:
            if self.location in row:
                try:
                    return row[row.index(self.location) + 1]
                except IndexError:
                    return self.spiral[rownum+1][0]

            rownum += 1


# This only tests if the retrieval is ok
def test_bigger_1():
    sm = SpiralMemory(747)
    assert sm.get_number() == 796

#This is a 'real' test which checks all functionality
def test_bigger_2():
    sm1 = SpiralMemory(747)
    assert sm1.get_number() == 796

if __name__ == '__main__':
    sm = SpiralMemory(361527)
    print(sm.get_number())
