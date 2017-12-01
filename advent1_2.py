# Advent of Code 2017 1.2
# Sum digits in a stream that match the digit halfway around the circular list
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/01/17
#

testCases = { '1212' : 6,
              '1221' : 0,
              '123425' : 4,
              '123123' : 12,
              '12131415' : 4}

def advInput(day):
    """Open the data file for a given day"""
    filename = 'data/input{}.txt'.format(day)
    return open(filename)

def sumMatchingHalfwayDigits(str):
    """Process a sequence of digits composing a sum of those that match their neighbor"""
    print('Summing ', str)

    halfdist = len(str) // 2
    summed = 0
    if len(str) > 0:
        firstDigit = str[0]
        prevDigit = str[-1]
        for x in str:
            if x == prevDigit:
                summed += int(x)
            prevDigit = x

    return summed

for k, v in testCases.items():
    ans = sumMatchingHalfwayDigits(k)
    print('Got back ', ans)
    if ans != v:
        print('   !!! Answer is wrong!')
    else:
        print('   *** Correct!')

f = advInput(1)
s = f.read()

ans = sumMatchingHalfwayDigits(s)

print(ans)