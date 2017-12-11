# Advent of Code 2017 4.1
# High Entropy Passphrase
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/11/17
#
"""
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password.
A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

Answer is 477
"""

def is_valid(line):
    """Split the passphrase into indivual words and use a set to weed out any duplicates"""
    word_list = line.split()
    init_word_count = len(word_list)

    # a set to hold the words
    non_dup_words = set(word_list)
    non_dup_count = len(non_dup_words)

    return (init_word_count == non_dup_count)

test_list = ['aa bb cc dd ee', 'aa bb cc dd aa', 'aa bb cc dd aaa']
print('Testing...')
for item in test_list:
    ret = is_valid(item)
    print('Passphrase is', item, '   valid flag is', ret)

good_count = 0
line_count = 0
filename = 'data/input4.txt'
with open(filename) as phrases:
    for phrase in phrases:
        line_count += 1
        if is_valid(phrase):
            good_count += 1

print('I read', line_count, ' lines and', good_count, ' contained valid passphrases')
