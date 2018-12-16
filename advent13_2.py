# Advent of Code 2017 13 part 2
# Packet Scanners
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/1/18
#


def build_scanners(filename: str) -> dict:
    "Create a dictionary representing the scanners in the firewall"
    fw = {}
    with open(filename) as f:
        # strip trailing newline off each line
        lines = [line.rstrip('\n') for line in f]
        for l in lines:
            items = l.split()
            fw[int(items[0][0:-1])] = (int(items[1]) - 1) * 2
            print(items[0][0:-1], items[1], "->", (int(items[1]) - 1) * 2)

    return fw

def walk_safely(firewall: dict) -> int:
    "Try to walk across the firewalls safely, returning the needed delay"
    last_scanner = max(firewall)
    safe_run = -1
    delay = 0

    while safe_run == -1 and delay < 100000000:
        scanner_caught = False

        # walk each step of the firewall
        for curr_level in range(last_scanner + 1):
            # is there a scanner at this step?
            if curr_level in firewall:
                factor = firewall[curr_level]
                if (curr_level + delay) % factor == 0:
                    scanner_caught = True
                    break

        if not scanner_caught:
            safe_run = delay
        else:
            delay += 1

    return safe_run


filename = "data/test13.txt"
firewall = build_scanners(filename)
safe_run = walk_safely(firewall)
if safe_run > -1:
    print("The safe walk needed a delay of", safe_run)
else:
    print("There is no safe walk delay")

filename = "data/input13.txt"
firewall = build_scanners(filename)
safe_run = walk_safely(firewall)
if safe_run > -1:
    print("The safe walk needed a delay of", safe_run)
else:
    print("There is no safe walk delay")