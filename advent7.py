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

--- Part Two ---

The programs explain the situation: they can't get down. Rather, they could get down, if they weren't expending all
of their energy trying to keep the tower balanced. Apparently, one program has the wrong weight, and until it's fixed,
they're stuck here.

For any program holding a disc, each program standing on that disc forms a sub-tower. Each of those sub-towers are
supposed to be the same weight, or the disc itself isn't balanced. The weight of a tower is the sum of the weights of
the programs in that tower.

In the example above, this means that for ugml's disc to be balanced, gyxo, ebii, and jptl must all have the same
weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its disc and all programs above it must each match.
This means that the following sums must all be the same:

ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the other two. Even though the nodes above ugml
are balanced, ugml itself is too heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the towers
balanced. If this change were made, its weight would be 60.

Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower?

Answer 7.2:
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


def check_for_mismatch(hold_child_totals):
    """Check a list of ints for an item that does not match
       Return the amount of discrepancy and the index of the out-of-whack item"""

    ret_vals = None
    mismatch_amount = 0
    match_count = [0 for i in range(len(hold_child_totals))]

    #brute force comparison
    mismatch_found = False
    for i in range(len(hold_child_totals)-1):
        for j in range(i+1, len(hold_child_totals)):
            if hold_child_totals[i] == hold_child_totals[j]:
                match_count[i] += 1
                match_count[j] += 1
            else:
                mismatch_found = True


    if mismatch_found:
        for i in range(len(match_count)):
            if match_count[i] == 0:
                if i == 0:
                    mismatch_amount = hold_child_totals[1] - hold_child_totals[0]
                else:
                    mismatch_amount = hold_child_totals[i-1] - hold_child_totals[i]
                ret_vals = (i, mismatch_amount)
                break

    ### need to return the index of the wrong amount as well as the amount to adjust
    return ret_vals


def find_imbalance(tower, node_name):
    """Visit the sub tower starting at this node and check for an imbalance in the weight
       Using recursion to solve - Yikes"""

    adjust_weight = 0
    total_weight = 0

    print('   visiting node', node_name)
    node = tower[node_name]

    total_weight = node.weight
    if len(node.children) != 0:
        # hold the child totals in a list
        hold_child_totals = []
        for kid_node in node.children:
            (kid_total, kid_adjust) = find_imbalance(tower, kid_node)
            if kid_adjust != 0:
                return (0, kid_adjust)

            total_weight += kid_total
            hold_child_totals.append(kid_total)

        print('         these are the kid totals', hold_child_totals)
        # see if one of the kid totals does not match the others
        mismatch_vals = check_for_mismatch(hold_child_totals)
        if mismatch_vals != None:
            adjust_weight = mismatch_vals[1]
            child_to_be_adjusted = mismatch_vals[0]
            bad_kid_name = node.children[child_to_be_adjusted]
            bad_kid_node = tower[bad_kid_name]
            adjust_weight = bad_kid_node.weight + mismatch_vals[1]

    print('      node', node_name, 'returning weight', total_weight, 'and', adjust_weight, 'adjustment weight')
    return (total_weight, adjust_weight)


filename = 'data/test7.txt'
tower = build_tower(filename)
root = find_root(tower)
print('The root is at', root)

weights = find_imbalance(tower, root)
print('the adjustment weight is', weights[1])

filename = 'data/input7.txt'
tower = build_tower(filename)
root = find_root(tower)
print('The root is at', root)

weights = find_imbalance(tower, root)
print('the adjustment weight is', weights[1])
