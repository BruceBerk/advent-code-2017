# Advent of Code 2017 6.2
# Memory Reallocation
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/12/17
#
"""
Out of curiosity, the debugger would also like to know the size of the loop: starting from a state that has already
been seen, how many block redistribution cycles must be performed before that same state is seen again?

In the example above, 2 4 1 2 is seen again after four cycles, and so the answer in that example would be 4.

How many cycles are in the infinite loop that arises from the configuration in your puzzle input?
Answer 8038
"""

def find_max(cells):
    """Return the index of the cell in the list with the highest value"""
    chk_val = -1
    ret_idx = -1

    for idx in range(len(cells)):
        if cells[idx] > chk_val:
            chk_val = cells[idx]
            ret_idx = idx

    return ret_idx

def realloc(filename):
    """Reallocate memory cells until a pattern is duplicated"""

    with open(filename) as fil:
        cycle_count = 0

        # use a dictionary to track patterns we have seen
        patterns_seen = {}

        buf = fil.read()
        cells = [int(c) for c in buf.split()]
        print('starting with', cells)

        pattern = ''.join([str(a)+'-' for a in cells])
        print('pattern is', pattern)

        sz = len(cells)

        while pattern not in patterns_seen:
            patterns_seen[pattern] = cycle_count

            # which cell is highest?
            idx = find_max(cells)
            ##print('highest cell is at index', idx)

            # how much to allocate?
            amt = cells[idx]
            cells[idx] = 0

            # allocate the amount into the other cells
            while amt > 0:
                # next cell, wrap around if necessary
                idx += 1
                if idx == sz:
                    idx = 0
                cells[idx] += 1
                amt -= 1

            # generate the new pattern
            ##print('allocated to', cells)
            pattern = ''.join([str(a)+'-' for a in cells])
            print('pattern is', pattern)
            cycle_count += 1

        # we have broken out with a match
        # compare the cycle count of the match with the original
        diff_cycles = cycle_count - patterns_seen[pattern]

    return diff_cycles

# test data - should be 5
cycles = realloc('data/test6.txt')
print('It took', cycles, 'to match')

cycles = realloc('data/input6.txt')
print('It took', cycles, 'to match')
