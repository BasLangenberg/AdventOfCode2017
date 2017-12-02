def calculate_checksum(spreadsheet):
    total = 0
    for line in spreadsheet.readlines():
        min = 10000000000000000000000000000 # looks like enough. ;-)
        max = 0
        for number in line.split(' '):
            if int(number) > max:
                max = int(number)
            if int(number) < min:
                min = int(number)

        total += max - min

    return total


def calculate_checksum_2(spreadsheet):
    total = 0
    for line in spreadsheet.readlines():
        for number in line.rstrip('\n').split(' '):
            for number2 in line.rstrip('\n').split(' '):
                if float(number) != float(number2):
                    if float(number) % float(number2) == 0:
                        total += int(number) / int(number2)

    return total


def test_day2_solution():
    sh = open('input_test.txt')
    assert calculate_checksum(sh) == 18


def test_day2_challenge2():
    sh = open('input_challenge_2.txt')
    assert calculate_checksum_2(sh) == 9


if __name__ == '__main__':
    sh = open('input.txt')
    print(calculate_checksum(sh))
    sh = open('input.txt')
    print(calculate_checksum_2(sh))
