# Advent of Code 2017 1.1
# Sum consectutive digits in a stream that match their successor
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/01/17
#

def advInput(day):
    """Open the data file for a given day"""
    filename = 'data/input{}.txt'.format(day)
    return open(filename)

def sumMatchingDigits(str):
    """Process a sequence of digits composing a sum of those that match their neighbor"""
    summed = 0
    if len(str) > 0:
        firstDigit = str[0]

    return summed

f = advInput(1)
s = f.read()

print(s)

teststr = '1122'
ans = sumMatchingDigits(teststr)

print(ans)