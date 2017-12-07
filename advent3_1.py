# Advent of Code 2017 3.1
# Spiral memory
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/04/17
#
"""
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while
spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the
location of the only access port for this memory system) by programs that can only move up, down, left, or right.
They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in your puzzle input all the way to the
access port?

265149 => 438
"""
import math
import SpiralMemory

def sizeOfBox(num):
    """Given a number, how big is the box?"""
    s = math.sqrt(num)
    si = int(s)
    if (si * si) < num:
        si += 1

    return si

def countSpiralSteps(num):
    """Determine the number of steps to reach the access port in the spiral memory"""
    steps = 0
    print('Counting for', num)

    # special cases
    if num == 1:
        return 0
    elif num == 2:
        return 1
    elif num == 3:
        return 2

    # how big is the box?
    boxsize = sizeOfBox(num)
    print('box size is', boxsize)

    # if the box size is an even number, it ends in the upper left
    # odd number, it ends in the lower right
    if (num % 2) == 0:
        endrow = 0
        endcol = 0
        print('the end is upper left')
    else:
        endrow = boxsize - 1
        endcol = boxsize - 1
        print('the end is lower right')

    return steps

datList = [1, 2, 3, 4, 12, 23, 1024, 265149, 37, 38, 39, 43, 44, 45, 47, 49]
for dat in datList:
    sm = SpiralMemory.SpiralMemory(dat)
    print(sm)

    steps = sm.count_steps()
    print('*** Number of steps is', steps)