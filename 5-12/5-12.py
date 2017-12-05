def escape_plan(input):
    index = count = jump = 0
    while index < len(input):
        jump = input[index]
        input[index] += 1
        index += jump
        count += 1

    return count


def escape_plan2(input):
    index = count = jump = prev_jump = 0
    while index < len(input):
        jump = input[index]
        if prev_jump >= 3:
            input[index] -= 1
        else:
            input[index] += 1
        index += jump
        count += 1
        if index < len(input):
            prev_jump = input[index]

    return count


def test_escape_plan():
    test_input = [0, 3, 0, 1, -3]
    assert escape_plan(test_input) == 5


def test_escape_plan_2():
    test_input = [0, 3, 0, 1, -3]
    assert escape_plan2(test_input) == 10


if __name__ == '__main__':
    input_file = open('input.txt')
    input = []
    for line in input_file.readlines():
        input.append(int(line))

    print(escape_plan(input))

    input_file = open('input.txt')
    input = []
    for line in input_file.readlines():
        input.append(int(line))

    print(escape_plan2(input))
