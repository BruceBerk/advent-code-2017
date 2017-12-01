# Advent of Code 2017 1.1
# Sum consectutive digits in a stream that match their successor
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/01/17
#

testCases = { '1234' : 0,
              '1122' : 3,
              '1111' : 4,
              '91212129' : 9}

def advInput(day):
    """Open the data file for a given day"""
    filename = 'data/input{}.txt'.format(day)
    return open(filename)

def sumMatchingDigits(str):
    """Process a sequence of digits composing a sum of those that match their neighbor"""
    print('Summing ', str)

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
    ans = sumMatchingDigits(k)
    print('Got back ', ans)
    if ans != v:
        print('   !!! Answer is wrong!')
    else:
        print('   *** Correct!')

f = advInput(1)
s = f.read()

ans = sumMatchingDigits(s)

print(ans)