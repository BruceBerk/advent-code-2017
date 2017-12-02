# Advent of Code 2017 2.1
# Checksum digits
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/02/17
#
"""
The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track,
they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value
and the smallest value; the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8
The first row's largest and smallest values are 9 and 1, and their difference is 8.
The second row's largest and smallest values are 7 and 3, and their difference is 4.
The third row's difference is 6.
In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.
"""

def calcChecksum(filename):
    """Calculate the checksum on the named file"""
    chksum = 0

    with open(filename) as ssheet:
        for row in ssheet:
            cells = row.split()
            print('processing ', cells)
            if len(cells) > 0:
                cellnums = [int(cell) for cell in cells]
                print('converted ', cellnums)
                minval = min(cellnums)
                maxval = max(cellnums)
                print('min is', minval, ' and max is', maxval)
                chksum += (maxval - minval)

    return chksum

fname = 'data/test2.txt'
chksum = calcChecksum(fname)
print('Checksum is ', chksum)

fname = 'data/input2.txt'
chksum = calcChecksum(fname)
print('Checksum is ', chksum)
