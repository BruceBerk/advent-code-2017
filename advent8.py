# Advent of Code 2017-8
# Registers
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/28/17
#

"""
You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you
to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's
value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction
without modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth
to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?

Answer: 5946

--- Part Two ---

To be safe, the CPU also needs to know the highest value held in any register during this process so that it can
decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever
held was 10 (in register c after the third instruction was evaluated).

Answer: 6026
"""

def process_line(registers: dict, items: list) -> int:
    """Process the instruction and return the updated value"""
    rval = registers[items[0]]
    amt = int(items[2])
    if items[1].lower() == 'dec':
        rval -= amt
    elif items[1].lower() == 'inc':
        rval += amt

    registers[items[0]] = rval
    return rval


def run_program(filename: str) -> dict:
    """Run the program in the file and return a dictionary of register names and values"""
    registers = {}
    max_temp_val = -999999

    with open(filename) as f:
        # strip trailing newline off each line
        lines = [line.rstrip('\n') for line in f]
        for l in lines:
            items = l.split()
            if len(items) != 7:
                print('** bad line ** -> ', items)
            else:
                if items[0] not in registers:
                    registers[items[0]] = 0

                if items[4] not in registers:
                    registers[items[4]] = 0

                oper = items[5]
                chk_val = int(items[6])
                register_to_check = registers[items[4]]

                if oper == '==' and register_to_check == chk_val:
                    amt = process_line(registers, items)
                    if amt > max_temp_val:
                        max_temp_val = amt
                elif oper == '<' and register_to_check < chk_val:
                    amt = process_line(registers, items)
                    if amt > max_temp_val:
                        max_temp_val = amt
                elif oper == '>' and register_to_check > chk_val:
                    amt = process_line(registers, items)
                    if amt > max_temp_val:
                        max_temp_val = amt
                elif oper == '!=' and register_to_check != chk_val:
                    amt = process_line(registers, items)
                    if amt > max_temp_val:
                        max_temp_val = amt
                elif oper == '<=' and register_to_check <= chk_val:
                    amt = process_line(registers, items)
                    if amt > max_temp_val:
                        max_temp_val = amt
                elif oper == '>=' and register_to_check >= chk_val:
                    amt = process_line(registers, items)
                    if amt > max_temp_val:
                        max_temp_val = amt

    print('The maximum stored value is', max_temp_val)
    return registers


def find_greatest_register(registers: dict) -> int:
    """Check all the registers and return the largest value"""
    max_val = None

    for regname, regval in registers.items():
        #print(regname)
        if max_val == None:
            max_val = regval
        elif regval > max_val:
            max_val = regval

    return max_val

# run the test program, answer should be 1
registers = run_program('data/test8.txt')
max_val = find_greatest_register(registers)
print('The maximum value in a register is', max_val)

# run the real program
registers = run_program('data/input8.txt')
max_val = find_greatest_register(registers)
print('The maximum value in a register is', max_val)
