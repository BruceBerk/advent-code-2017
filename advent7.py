# Advent of Code 2017 7
# Recursive Circus
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/12/17
#
"""
Wandering further through the circuits of the computer, you come upon a tower of programs that have gotten themselves
into a bit of trouble. A recursive algorithm has gotten out of hand, and now they're balanced precariously in a large
tower.

One program at the bottom supports the entire tower. It's holding a large disc, and on the disc are balanced several
more sub-towers. At the bottom of these sub-towers, standing on the bottom disc, are other programs, each holding
their own disc, and so on. At the very tops of these sub-sub-sub-...-towers, many programs stand simply keeping the
disc below them balanced but with no disc of their own.

You offer to help, but first you need to understand the structure of these towers. You ask each program to yell out
their name, their weight, and (if they're holding a disc) the names of the programs immediately above them balancing
on that disc. You write this information down (your puzzle input). Unfortunately, in their panic, they don't do this
in an orderly fashion; by the time you're done, you're not sure which program gave which information.

For example, if your list is the following:

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
...then you would be able to recreate the structure of the towers that looks like this:

                gyxo
              /
         ugml - ebii
       /      \
      |         jptl
      |
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |
      |         ktlj
       \      /
         fwft - cntj
              \
                xhth
In this example, tknk is at the bottom of the tower (the bottom program), and is holding up ugml, padx, and fwft.
Those programs are, in turn, holding up other programs; in this example, none of those programs are holding up any
other programs, and are all the tops of their own towers. (The actual tower balancing in front of you is much larger.)

Before you're ready to help them, you need to make sure your information is correct. What is the name of the bottom
program?

Answer 7.1: ykpsek

"""


class ProgNode:
    """A class representing a program in the tower"""

    def __init__(self, name: str, weight: int=0, children: list=[]) -> None:
        self.name = name
        self.weight = weight
        self.children = children
        self.parent = None

    def __repr__(self) -> str:
        return self.name + ' (' + str(self.weight) + ') ' + str(self.children) + ' ' + str(self.parent)


def build_tower(filename: str) -> dict:
    """Build the tower dictionary structure from a given file"""
    tower = {}

    with open(filename) as f:
        # strip trailing newline off each line
        lines = [line.rstrip('\n') for line in f]
        for l in lines:
            items = l.split()
            name = items[0]
            weight = int(items[1][1:-1])

            # are the any children noted in the file?
            kids = []
            if len(items) > 3:
                kids = [item.rstrip(',') for item in items[3:]]

            # add node to the dictionary tower
            prog = ProgNode(name, weight, kids)
            tower[name] = prog

            print(items)

    # visit each node of the tower and designate which progs have parents
    for k, node in tower.items():
        for kid in node.children:
            kidnode = tower[kid]
            kidnode.parent = k

    print(tower)
    return tower


def find_root(tower: dict) -> str:
    """Find the root node of the tower and return its name"""
    name = 'unknown'

    # pick a node from the tower
    for k in tower:
        print(k)
        root_found = False
        while not root_found:
            node = tower[k]
            print('at', node)
            # if the node doesn't have a parent - we are done. Otherwise we have to visit the parent node
            if node.parent == None:
                name = k
                root_found = True
            else:
                k = node.parent

        break

    return name

filename = 'data/test7.txt'
tower = build_tower(filename)
print('The root is at', find_root(tower))

filename = 'data/input7.txt'
tower = build_tower(filename)
print('The root is at', find_root(tower))
