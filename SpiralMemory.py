# SpiralMemory - a class to encapsulate spiral memory storage and operations
#
# Advent Of Code 2017
# Bruce Berkowicz

import math

class SpiralMemory:
    def __init__(self, memory_loc: int) -> None:
        self.memory_loc = memory_loc
        self.box_size = self.size_of_box(memory_loc)
        self.access_point = ((self.box_size - 1) // 2, (self.box_size - 1) // 2)

    def __repr__(self) -> str:
        s = "SpiralMemory for " + str(self.memory_loc) + " locations. "
        s += "Box size is " + str(self.box_size) + " and access point is at " + str(self.access_point)
        return s

    def size_of_box(self, num):
        """Given a number, how big is the box?"""
        s = math.sqrt(num)
        si = int(s)
        if (si * si) < num:
            si += 1

        return si

    def count_steps(self):
        """How many steps from the memory loc to the access point"""
        self.steps = 0

        # special cases
        if self.memory_loc == 1:
            return 0
        elif self.memory_loc == 2 or self.memory_loc == 4:
            return 1
        elif self.memory_loc == 3:
            return 2

        num = self.box_size ** 2

        # is the box size odd or even?
        if (self.box_size % 2) == 0:
            print("the box size is even")
            row = self.box_size - 1
            col = 0
            while num > self.memory_loc and col < self.box_size-1:
                num -= 1
                col += 1

            if num > self.memory_loc:
                while num > self.memory_loc and row > 0:
                    num -= 1
                    row -= 1

            print("   memory loc is at (" + str(row) + "," + str(col) + ")")

            self.steps = abs(self.access_point[0] - row) + abs(self.access_point[1] - col)
        else:
            print("the box size is odd")
            row = 0
            col = self.box_size - 1
            while num > self.memory_loc and col > 0:
                num -= 1
                col -= 1

            if num > self.memory_loc:
                while num > self.memory_loc and row < self.box_size-1:
                    num -= 1
                    row += 1

            print("   memory loc is at (" + str(row) + "," + str(col) + ")")

            self.steps = abs(self.access_point[0] - row) + abs(self.access_point[1] - col)
        return self.steps