# Advent of Code 2017-11
# Hex Grid
#
# Bruce Berkowicz
# bruceberk@me.com
# 1/6/18
#

"""
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in
distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast,
southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
You have the path the child process took. Starting where he started, you need to determine the fewest number of steps
required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw).

Answer: 794

--- Part Two ---

How many steps away is the furthest he ever got from his starting position?

Answer: 1524

"""

def print_hex_path(path: dict) -> None:
    """Print out the path dictionary"""
    for k in sorted(path):
        print(k, 'has', path[k], 'steps')

def replace_with_hypotenuse(path: dict) -> dict:
    """Replace steps that are angular with the hypotenuse"""
    prime_dirs = ['ne', 'se', 's', 'sw', 'nw', 'n']
    ang_dirs = ['s', 'sw', 'nw', 'n', 'ne', 'se']
    repl_dirs = ['se', 's', 'sw', 'nw', 'n', 'ne']

    reduction = False
    for i in range(len(prime_dirs)):
        if path[prime_dirs[i]] > 0 and path[ang_dirs[i]] > 0:
            if path[prime_dirs[i]] < path[ang_dirs[i]]:
                amt_cancelling = path[prime_dirs[i]]
            else:
                amt_cancelling = path[ang_dirs[i]]
            path[prime_dirs[i]] -= amt_cancelling
            path[ang_dirs[i]] -= amt_cancelling
            path[repl_dirs[i]] += amt_cancelling
            reduction = True

    return (path, reduction)


def look_for_opposite_steps(path: dict) -> dict:
    """Steps in opposite directions cancel each other out"""
    prime_dirs = ['n', 'ne', 'se']
    opp_dirs = ['s', 'sw', 'nw']

    reduction = False
    for i in range(len(prime_dirs)):
        if path[prime_dirs[i]] > 0 and path[opp_dirs[i]] > 0:
            if path[prime_dirs[i]] < path[opp_dirs[i]]:
                amt_cancelling = path[prime_dirs[i]]
            else:
                amt_cancelling = path[opp_dirs[i]]
            path[prime_dirs[i]] -= amt_cancelling
            path[opp_dirs[i]] -= amt_cancelling
            reduction = True

    return (path, reduction)


def pare_path(path: dict) -> int:
    """Pare the path down and count the steps"""
    hold_path = path

    reduce1 = True
    reduce2 = True
    while reduce1 or reduce2:
        hold_path, reduce1 = replace_with_hypotenuse(hold_path)

        hold_path, reduce2 = look_for_opposite_steps(hold_path)

    # wrap things up - how many steps are left?
    sum_steps = 0
    for k in hold_path:
        sum_steps += hold_path[k]

    return sum_steps


def walk_hex_and_find_longest(filename: str) -> int:
    """Walk the grid and at each step, calculate the path and return the longest path"""
    max_steps = 0
    path = {'ne': 0, 'se': 0, 's': 0, 'sw': 0, 'nw': 0, 'n': 0}

    with open(filename) as f:
        dat = f.read()
        steps = dat.split(',')

        for next_step in steps:
            path[next_step] += 1
            try_path = path
            steps = pare_path(try_path)
            if steps > max_steps:
                max_steps = steps

    return max_steps


def walk_hex_grid(filename: str) -> int:
    """Walk the hex grid path represented by the file and return the minimum number of steps needed to reach dest"""
    path = {'ne': 0, 'se': 0, 's': 0, 'sw': 0, 'nw': 0, 'n': 0}

    with open(filename) as f:
        dat = f.read()
        steps = dat.split(',')

        for next_step in steps:
            path[next_step] += 1

    print_hex_path(path)

    sum_steps = pare_path(path)

    return sum_steps

testdata = ['data/test11-1.txt', 3, 'data/test11-2.txt', 0, 'data/test11-3.txt', 2, 'data/test11-4.txt', 3]

for i in range(0, len(testdata), 2):
    print('Processing', testdata[i], 'expected steps =', testdata[i+1])
    steps = walk_hex_grid(testdata[i])
    if steps == testdata[i+1]:
        result = '   Pass:'
    else:
        result = '   Fail:'
    print(result, 'got back', steps, 'steps')

steps = walk_hex_grid('data/input11.txt')
print('Got back', steps, 'steps')

max_steps = walk_hex_and_find_longest('data/input11.txt')
print('Farthest path is', max_steps, 'steps')
