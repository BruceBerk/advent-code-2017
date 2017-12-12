# Advent of Code 2017 6.1
# Memory Reallocation
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/11/17
#
"""
A debugger program here is having an issue: it is trying to repair a memory reallocation routine, but it keeps getting
stuck in an infinite loop.

In this area, there are sixteen memory banks; each memory bank can hold any number of blocks. The goal of the
reallocation routine is to balance the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the memory bank with the most blocks (ties won
by the lowest-numbered memory bank) and redistributes those blocks among the banks. To do this, it removes all of the
blocks from the selected bank, then moves to the next (by index) memory bank and inserts one of the blocks. It
continues doing this until it runs out of blocks; if it reaches the last memory bank, it wraps around to the first one.

The debugger would like to know how many redistributions can be done before a blocks-in-banks configuration is
produced that has been seen before.

For example, imagine a scenario with only four memory banks:

The banks start with 0, 2, 7, and 0 blocks. The third bank has the most blocks, so it is chosen for redistribution.
Starting with the next bank (the fourth bank) and then continuing to the first bank, the second bank, and so on, the
7 blocks are spread out over the memory banks. The fourth, first, and second banks get two blocks each, and the third
bank gets one back. The final result looks like this: 2 4 1 2.
Next, the second bank is chosen because it contains the most blocks (four). Because there are four memory banks, each
gets one block. The result is: 3 1 2 3.
Now, there is a tie between the first and fourth memory banks, both of which have three blocks. The first bank wins
the tie, and its three blocks are distributed evenly over the other three banks, leaving it with none: 0 2 3 4.
The fourth bank is chosen, and its four blocks are distributed such that each of the four banks receives one: 1 3 4 1.
The third bank is chosen, and the same thing happens: 2 4 1 2.
At this point, we've reached a state we've seen before: 2 4 1 2 was already seen. The infinite loop is detected after
the fifth block redistribution cycle, and so the answer in this example is 5.

Given the initial block counts in your puzzle input, how many redistribution cycles must be completed before a
configuration is produced that has been seen before?

Answer 12841
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
            patterns_seen[pattern] = 1

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

    return cycle_count

# test data - should be 5
cycles = realloc('data/test6.txt')
print('It took', cycles, 'to match')

cycles = realloc('data/input6.txt')
print('It took', cycles, 'to match')
