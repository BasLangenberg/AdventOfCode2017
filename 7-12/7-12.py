class Tower(object):

    tower = {}

    def __init__(self, programs):
        for entry in programs.readlines():
            entry = entry.split()
            programs_above = ''
            for program in entry[3:]:
                programs_above += ' ' + program

            self.tower.update({
                entry[0]: {
                    'name': entry[0],
                    'weight': str(entry[1]).replace('(', '').replace(')', ''),
                    'carry programs': programs_above
                }
            })

    def get_bottom(self):
        found = False
        return 'xxxx'

def test_tower():
    input_file = open('input_test.txt')
    test_tower = Tower(input_file)
    assert test_tower.get_bottom() == 'tknk'
