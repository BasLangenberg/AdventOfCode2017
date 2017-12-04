def get_correct_passphrase_count(input_file):
    count = 0
    for line in input_file.readlines():
        words = line.split()
        subcount = 0
        for word in words:
            if not words.count(word) == 1:
                subcount += 1j
        if subcount == 0:
            count += 1

    return count


def get_correct_anagram_count(input_file):
    count = 0
    for line in input_file.readlines():
        valid = True
        found = dict()
        for word in line.split():
            sort_word = ''.join(sorted(word))
            if sort_word in found:
                valid = False
            else:
                found[sort_word] = 1

        if valid:
            count += 1

    return count


def test_passphrase():
    input_file = open('input_test.txt')
    assert get_correct_passphrase_count(input_file) == 2


def test_passphrase_anagram():
    input_file = open('input_test_2.txt')
    assert get_correct_anagram_count(input_file) == 3


if __name__ == '__main__':
    input_file = open('input.txt')
    print(get_correct_passphrase_count(input_file))
    input_file = open('input.txt')
    print(get_correct_anagram_count(input_file))

