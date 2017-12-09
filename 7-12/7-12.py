class Tower(object):

    tower = {}
    bottom = ''

    def __init__(self, programs):
        for entry in programs.readlines():
            entry = entry.split()
            programs_above = ''
            for program in entry[3:]:
                if len(programs_above) == 0:
                    programs_above += program
                else:
                    programs_above += ' ' + program

            self.tower.update({
                entry[0]: {
                    'name': entry[0],
                    'weight': str(entry[1]).replace('(', '').replace(')', ''),
                    'carry programs': programs_above
                }
            })

    def get_bottom(self):
        to_check = list()
        for program in self.tower:
            if len(self.tower[program]['carry programs']) > 1:
                to_check.append(program)

        winners = list(to_check)
        for program in to_check:
            for carry in self.tower[program]['carry programs'].split():
                if ',' in carry:
                    carry = str(carry).replace(',', '')

                if carry in winners:
                    winners.remove(carry)

        if len(winners) == 1:
            self.bottom = winners[0]
            return winners[0]
        else:
            raise ValueError

    def get_balance(self, tower_name):
        balance = 0
        if len(self.tower[tower_name]['carry programs']) != 0:
            for programs in self.tower[tower_name]['carry programs'].split():
                if ',' in programs:
                    programs = str(programs).replace(',', '')

                balance += self.get_balance(programs)

        balance += int(self.tower[tower_name]['weight'])

        return balance


def test_tower():
    input_file = open('input_test.txt')
    test_tower = Tower(input_file)
    assert test_tower.get_bottom() == 'tknk'
    for program in test_tower.tower[test_tower.bottom]['carry programs'].replace(',', '').split():
        print('Tower: ' + program + ' Balance: ' + str(test_tower.get_balance(program)))


if __name__ == '__main__':
    input_file = open('input.txt')
    tower = Tower(input_file)
    print(tower.get_bottom())
    #for program in tower.tower[tower.bottom]['carry programs'].replace(',', '').split():
    #    print('Tower: ' + program + ' Balance: ' + str(tower.get_balance(program)))
    #for program in tower.tower['hqxdyv']['carry programs'].replace(',', '').split():
    #    print('Tower: ' + program + ' Balance: ' + str(tower.get_balance(program)))
    for program in tower.tower['apktiv']['carry programs'].replace(',', '').split():
        print('Tower: ' + program + ' Balance: ' + str(tower.get_balance(program)))
    for program in tower.tower['obxrn']['carry programs'].replace(',', '').split():
         print('Tower: ' + program + ' Balance: ' + str(tower.get_balance(program)))
    print(tower.tower['obxrn'])
