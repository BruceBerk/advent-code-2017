# Advent of Code 2017 3.2
# Spiral memory accumulator
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/09/17
#
"""
As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the
same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?

Your puzzle input is still 265149.
Answer is 266330

"""

def box_sum(box, i, j):
    """Sum the 8 adjacent squares for a given box location"""
    accum = 0
    box_side = len(box)

    row = i - 1
    while row <= (i+1):
        col = j - 1
        while col <= (j+1):
            if row != i or col != j:
                if row >= 0 and row < box_side and col >= 0 and col < box_side:
                    accum += box[row][col]

            col += 1

        row += 1

    return accum

def spiral_accumulator(limit):
    """Build up the spiral memory, accumulating values until we pass the limit. Return the passed value"""
    accum = 0
    mem_size = 2

    # Start with a 2x2 memory block
    m = [[0 for i in range(mem_size)] for j in range(mem_size)]
    m[0][0] = 4
    m[0][1] = 2
    m[1][0] = 1
    m[1][1] = 1

    while accum == 0:
        # increase to the next bigger box
        mem_size += 2
        n = [[0 for i in range(mem_size)] for j in range(mem_size)]

        # copy the original box
        for i in range(mem_size-2):
            for j in range(mem_size-2):
                n[i+1][j+1] = m[i][j]

        # fill in the border squares
        m = n

        # down the left side
        for r in range(1, mem_size):
            amt = box_sum(m, r, 0)
            m[r][0] = amt
            if amt > limit:
                accum = amt
                break

        # across the bottom
        if accum == 0:
            for c in range(mem_size):
                amt = box_sum(m, mem_size-1, c)
                m[mem_size-1][c] = amt
                if amt > limit:
                    accum = amt
                    break

        # up the right side
        if accum == 0:
            for r in range(mem_size-1, -1, -1):
                amt = box_sum(m, r, mem_size-1)
                m[r][mem_size-1] = amt
                if amt > limit:
                    accum = amt
                    break

        # back across the top
        if accum == 0:
            for c in range(mem_size-1, -1, -1):
                amt = box_sum(m, 0, c)
                m[0][c] = amt
                if amt > limit:
                    accum = amt
                    break

    print('   mem_size is', mem_size)
    return accum

my_input = 265149

# ans should be 59
amt = spiral_accumulator(58)
print('ans for 58 is', amt, '   -> 59')

# ans should be 880
amt = spiral_accumulator(807)
print('ans for 807 is', amt, '   -> 880')

# ans should be 6155
amt = spiral_accumulator(6000)
print('ans for 6000 is', amt, '   -> 6155')

amt = spiral_accumulator(my_input)
print('ans for', my_input, 'is', amt)