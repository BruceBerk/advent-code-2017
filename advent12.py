# Advent of Code 2017-12
# Hex Grid
#
# Bruce Berkowicz
# bruceberk@me.com
# 1/7/18
#

"""
--- Day 12: Digital Plumber ---

Walking along the memory banks of the stream, you find a small village that is experiencing a little confusion: some
programs can't communicate with each other.

Programs in this village communicate using a fixed system of pipes. Messages are passed between programs using these
pipes, but most programs aren't connected to each other directly. Instead, programs pass messages between each other
until the message reaches the intended recipient.

For some reason, though, some of these messages aren't ever reaching their intended recipient, and the programs suspect
that some pipes are missing. They would like you to investigate.

You walk through the village and record the ID of each program and the IDs with which it can communicate directly (your
puzzle input). Each program has one or more programs with which it can communicate, and these pipes are bidirectional;
if 8 says it can communicate with 11, then 11 will say it can communicate with 8.

You need to figure out how many programs are in the group that contains program ID 0.

For example, suppose you go door-to-door like a travelling salesman and record the following list:

0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
In this example, the following programs are in the group that contains program ID 0:

Program 0 by definition.
Program 2, directly connected to program 0.
Program 3 via program 2.
Program 4 via program 2.
Program 5 via programs 6, then 4, then 2.
Program 6 via programs 4, then 2.
Therefore, a total of 6 programs are in this group; all but program 1, which has a pipe that connects it to itself.

How many programs are in the group that contains program ID 0?

Answer: 128

"""
import re

def process_file(filename: str) -> dict:
    """Read the input file into a dictionary. Each value in the dict is the list of programs that connect"""

    pipes = {}
    with open(filename) as f:
        # strip trailing newline off each line
        lines = [line.rstrip('\n') for line in f]
        for l in lines:
            # get rid of the connector and commas - still need to strip leading and trailing blanks
            tokens = re.split(',|\<\-\>', l)
            items = [tok.strip() for tok in tokens]
            print(items)
            pipes[items[0]] = items[1:]

    return pipes


def count_zero_connections(pipes: dict) -> int:
    """Walk the graph and count how many pipes connect to pipe 0"""
    zconnect = set()

    to_visit = set()
    have_visited = set()

    # start at pipe 0
    to_visit.add('0')
    while len(to_visit) > 0:
        node = to_visit.pop()
        # make sure we have not visited this node before
        if node not in have_visited:
            # keep track of the nodes we have already visited
            have_visited.add(node)

            # this counts as a connection to 0
            zconnect.add(node)

            # the children of this node may need to be visited
            for child in pipes[node]:
                to_visit.add(child)

    return len(zconnect)


pipes = process_file('data/test12.txt')
for k, v in pipes.items():
    print('Node', k, 'has connections to', v)

zcount = count_zero_connections(pipes)
print('I count', zcount, 'connections')

pipes = process_file('data/input12.txt')
zcount = count_zero_connections(pipes)
print('I count', zcount, 'connections')
