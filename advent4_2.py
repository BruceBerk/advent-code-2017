# Advent of Code 2017 4.2
# High Entropy Passphrase
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/11/17
#
"""
For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words
that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any
other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
Under this new system policy, how many passphrases are valid?

Answer is 167
"""

def is_valid(line):
    """Split the passphrase into indivual words and use a set to weed out any duplicates"""
    # sort each word in the phrase to check for anagrams
    word_list = [sorted(word) for word in line.split()]
    init_word_count = len(word_list)

    # a set to hold the words
    non_dup_words = set()

    # the above list comprehension made a list of lists (individual letters) - put it back together again
    for word in word_list:
        item = ''.join(word)
        non_dup_words.add(item)

    non_dup_count = len(non_dup_words)

    return (init_word_count == non_dup_count)

test_list = ['abcde fghij', 'abcde xyz ecdab', 'a ab abc abd abf abj', 'iiii oiii ooii oooi oooo', 'oiii ioii iioi iiio']
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
