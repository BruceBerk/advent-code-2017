# Advent of Code 2017 2.2
# Checksum digits
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/02/17
#
"""
It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is,
where the result of the division operation is a whole number. They would like you to find those numbers on each line,
divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5
In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
In the second row, the two numbers are 9 and 3; the result is 3.
In the third row, the result is 2.
In this example, the sum of the results would be 4 + 3 + 2 = 9.
"""

def calcChecksum(filename):
    """Calculate the checksum on the named file"""
    chksum = 0

    with open(filename) as ssheet:
        for row in ssheet:
            cells = row.split()
            print('processing ', cells)
            if len(cells) > 0:
                # convert the char numbers to ints
                cellnums = [int(cell) for cell in cells]
                print('converted ', cellnums)
                # sort the nums high to low
                divnums = sorted(cellnums, reverse=True)
                print('sorted', divnums)

                # process the list, pulling potential numerators off the front
                while len(divnums) >= 2:
                    numerator = divnums.pop(0)
                    print('checking', numerator, ' remaining list is', divnums)

                    foundDivisor = 0
                    for divisor in divnums:
                        if numerator % divisor == 0:
                            foundDivisor = divisor
                            print('+++ found divisor', foundDivisor)
                            break

                    if foundDivisor != 0:
                        chksum += (numerator // foundDivisor)
                        break

    return chksum

fname = 'data/test2-2.txt'
chksum = calcChecksum(fname)
print('Checksum is ', chksum)

fname = 'data/input2.txt'
chksum = calcChecksum(fname)
print('Checksum is ', chksum)
