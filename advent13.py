# Advent of Code 2017 13
# Packet Scanners
#
# Bruce Berkowicz
# bruceberk@me.com
# 01/25/18
#
"""
You need to cross a vast firewall. The firewall consists of several layers, each with a security scanner that moves
back and forth across the layer. To succeed, you must not be detected by a scanner.

By studying the firewall briefly, you are able to record (in your puzzle input) the depth of each layer and the range
of the scanning area for the scanner within it, written as depth: range. Each layer has a thickness of exactly 1. A
layer at depth 0 begins immediately inside the firewall; a layer at depth 1 would start immediately after that.

For example, suppose you've recorded the following:

0: 3
1: 2
4: 4
6: 4
This means that there is a layer immediately inside the firewall (with range 3), a second layer immediately after that
(with range 2), a third layer which begins at depth 4 (with range 4), and a fourth layer which begins at depth 6 (also
with range 4). Visually, it might look like this:

 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]
Within each layer, a security scanner moves back and forth within its range. Each security scanner starts at the top
and moves down until it reaches the bottom, then moves up until it reaches the top, and repeats. A security scanner
takes one picosecond to move one step. Drawing scanners as S, the first few picoseconds look like this:


Picosecond 0:
 0   1   2   3   4   5   6
[S] [S] ... ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

Picosecond 1:
 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

Picosecond 2:
 0   1   2   3   4   5   6
[ ] [S] ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]

Picosecond 3:
 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]
Your plan is to hitch a ride on a packet about to move through the firewall. The packet will travel along the top of
each layer, and it moves at one layer per picosecond. Each picosecond, the packet moves one layer forward (its first
move takes it into layer 0), and then the scanners move one step. If there is a scanner at the top of the layer as your
packet enters it, you are caught. (If a scanner moves into the top of its layer while you are there, you are not
caught: it doesn't have time to notice you before you leave.) If you were to do this in the configuration above,
marking your current position with parentheses, your passage through the firewall would look like this:

Initial state:
 0   1   2   3   4   5   6
[S] [S] ... ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

Picosecond 0:
 0   1   2   3   4   5   6
(S) [S] ... ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
( ) [ ] ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 1:
 0   1   2   3   4   5   6
[ ] ( ) ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] (S) ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]


Picosecond 2:
 0   1   2   3   4   5   6
[ ] [S] (.) ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] (.) ... [ ] ... [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]


Picosecond 3:
 0   1   2   3   4   5   6
[ ] [ ] ... (.) [ ] ... [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]

 0   1   2   3   4   5   6
[S] [S] ... (.) [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[ ]             [S]     [S]
                [ ]     [ ]


Picosecond 4:
 0   1   2   3   4   5   6
[S] [S] ... ... ( ) ... [ ]
[ ] [ ]         [ ]     [ ]
[ ]             [S]     [S]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] ... ... ( ) ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 5:
 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] (.) [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [S] ... ... [S] (.) [S]
[ ] [ ]         [ ]     [ ]
[S]             [ ]     [ ]
                [ ]     [ ]


Picosecond 6:
 0   1   2   3   4   5   6
[ ] [S] ... ... [S] ... (S)
[ ] [ ]         [ ]     [ ]
[S]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... ( )
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]
In this situation, you are caught in layers 0 and 6, because your packet entered the layer when its scanner was at the
top when you entered it. You are not caught in layer 1, since the scanner moved into the top of the layer once you were
already there.

The severity of getting caught on a layer is equal to its depth multiplied by its range. (Ignore layers in which you do
not get caught.) The severity of the whole trip is the sum of these values. In the example above, the trip severity is
0*3 + 6*4 = 24.

Given the details of the firewall you've recorded, if you leave immediately, what is the severity of your whole trip?

Answer: 2164
"""

class Scanner:
    """A class representing a scanner"""
    def __init__(self, depth: int, range: int) -> None:
        self.depth = depth
        self.range = range
        self.locat = 0
        self.direc = 1

    def advance(self) -> None:
        """Advance the scanner to the next location"""
        self.locat = self.locat + self.direc

        # Test if we went beyond an edge, if so direction inverts
        if self.direc == 1:
            if self.locat == self.range:
                self.locat = self.locat - 2
                self.direc = -1
        else:
            if self.locat == -1:
                self.locat = 1
                self.direc = 1

    def severity(self) -> int:
        return self.depth * self.range

    def is_scanner_at_top(self) -> bool:
        if self.locat == 0:
            return True
        else:
            return False




def build_scanners(filename: str) -> dict:
    "Create a dictionary representing the scanners in the firewall"
    fw = {}
    with open(filename) as f:
        # strip trailing newline off each line
        lines = [line.rstrip('\n') for line in f]
        for l in lines:
            items = l.split()
            #print(items[0][0:-1], items[1])
            fw[int(items[0][0:-1])] = Scanner(int(items[0][0:-1]), int(items[1]))

    return fw


def walk_firewall(firewall: dict, delay: int) -> int:
    sev_score = 0
    last_scanner = max(firewall)

    # delay for a given number of picoseconds
    for x in range(delay):
        for k, v in sorted(firewall.items()):
            v.advance()

    for curr_level in range(last_scanner+1):
        # are we caught by a scanner at this level?
        if curr_level in firewall:
            scanner = firewall[curr_level]
            if scanner.is_scanner_at_top():
                sev_score += scanner.severity()

        # advance all upcoming scanners
        for k, v in sorted(firewall.items()):
            if k >= curr_level:
                v.advance()

    return sev_score

def safe_walk(firewall: dict, delay: int) -> bool:
    last_scanner = max(firewall)

    # delay for given number of picoseconds
    for x in range(delay):
        for k, v in sorted(firewall.items()):
            v.advance()

    for curr_level in range(last_scanner+1):
        # are we caught by a scanner at this level?
        if curr_level in firewall:
            scanner = firewall[curr_level]
            if scanner.is_scanner_at_top():
                return False

        # advance all upcoming scanners
        for k, v in sorted(firewall.items()):
            if k >= curr_level:
                v.advance()

    return True


filename = "data/test13.txt"
firewall = build_scanners(filename)

delay = 0
sev_score = -1
while sev_score != 0:
    run_firewall = firewall
    sev_score = walk_firewall(run_firewall, delay)
    print("Delay:", delay, " - sev score is", sev_score)
    if sev_score != 0:
        delay += 1

print('Test severity score is', sev_score, 'was expecting 24')

filename = "data/input13.txt"
firewall = build_scanners(filename)
sev_score = walk_firewall(firewall, 0)
print('Severity score is', sev_score)


filename = "data/test13.txt"
firewall = build_scanners(filename)

delay = 0
found_safe = False

while not found_safe and delay < 32000:
    run_firewall = build_scanners(filename)
    found_safe = safe_walk(run_firewall, delay)
    if found_safe:
        print("Delay:", delay, " was a safe walk")
    else:
        print("Delay:", delay, " was NOT a safe walk")
    delay += 1


filename = "data/input13.txt"
firewall = build_scanners(filename)

delay = 18500
found_safe = False

while not found_safe and delay < 32000:
    run_firewall = build_scanners(filename)
    found_safe = safe_walk(run_firewall, delay)
    if found_safe:
        print("Delay:", delay, " was a safe walk")
    else:
        print("Delay:", delay, " was NOT a safe walk")
    delay += 1
