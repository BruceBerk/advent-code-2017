# Advent of Code 2017 5.2
# A Maze of Twisty Trampolines, All Alike
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/11/17
#
"""
Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1.
Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit
are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?

Answer is 23948711
"""

def count_jumps(filename):
    """Follow a list of jump instructions determining the number of steps needed to get out"""

    steps = 0
    with open(filename) as jump_file:
        f = jump_file.read()
        jumps = [int(instr) for instr in f.split()]

        idx = 0
        sz = len(jumps)

        while idx >= 0 and idx < sz:
            instr = jumps[idx]
            if instr >= 3:
                jumps[idx] = instr - 1
            else:
                jumps[idx] = instr + 1
            idx += instr
            steps += 1

    return steps

# run the test file - should be 5 steps
steps = count_jumps('data/test5.txt')
print('made it out in', steps, 'steps')

steps = count_jumps('data/input5.txt')
print('made it out in', steps, 'steps')

