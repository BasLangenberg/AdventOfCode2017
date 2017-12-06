def count_redistributes(input):
    count = 0
    banks = []
    while input not in banks:
        banks.append(list(input))
        max_value = max(input)
        redistributee = input.index(max_value)
        input[redistributee] = 0
        while max_value > 0:
            redistributee = redistributee + 1 if redistributee + 1 < len(input) else 0
            input[redistributee] += 1
            max_value -= 1
        count += 1

    return count


def count_redistributes_second_run(input):
    count = 0
    banks = []
    while input not in banks:
        banks.append(list(input))
        max_value = max(input)
        redistributee = input.index(max_value)
        input[redistributee] = 0
        while max_value > 0:
            redistributee = redistributee + 1 if redistributee + 1 < len(input) else 0
            input[redistributee] += 1
            max_value -= 1

    banks2 = []
    while input not in banks2:
        banks2.append(list(input))
        max_value = max(input)
        redistributee = input.index(max_value)
        input[redistributee] = 0
        while max_value > 0:
            redistributee = redistributee + 1 if redistributee + 1 < len(input) else 0
            input[redistributee] += 1
            max_value -= 1
        count += 1

    return count


def test_redistribute():
    banks = [0, 2, 7, 0]
    assert count_redistributes(banks) == 5


def test_redistribute_2():
    banks = [0, 2, 7, 0]
    assert count_redistributes_second_run(banks) == 4


if __name__ == '__main__':
    input = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
    print(count_redistributes(input))
    input = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
    print(count_redistributes_second_run(input))
