# Advent of Code 2017 14 part 1
# Disk Defragmentation
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/1/18
#


def hexify(knot_list: list) -> str:
    """Convert a list of numbers into the hex representation"""
    retstr = ""
    for i in range(len(knot_list)):
        ch = '{:02x}'.format(knot_list[i])
        retstr += ch

    return retstr


def get_ascii_codes(keystr: str) -> list:
    """Convert a string of bytes to a list of ascii codes"""
    retlist = []
    for ch in keystr:
        retlist.append(ord(ch))

    return retlist


def multi_hash_list(size: int, keystr: str, count: int) -> list:
    """knot hash a list multiple times"""

    # convert keystr to a list of lengths
    lengths = get_ascii_codes(keystr)

    # add the special bytes
    lengths.append(17)
    lengths.append(31)
    lengths.append(73)
    lengths.append(47)
    lengths.append(23)

    # start the list, based on size
    knot_list = []
    for i in range(size):
        knot_list.append(i)

    cur_pos = 0
    skip_size = 0

    for i in range(count):
        for l in lengths:
            left_idx = cur_pos
            right_idx = cur_pos + l - 1
            swap_count = l

            # does the sublist to reverse wrap around?
            while left_idx >= size:
                left_idx -= size

            while right_idx >= size:
                right_idx -= size

            while swap_count > 1:
                # swap the left and right items
                knot_list[left_idx], knot_list[right_idx] = knot_list[right_idx], knot_list[left_idx]

                # increment the left pointer
                left_idx += 1

                # did the left pointer go past the end?
                if left_idx >= size:
                    left_idx = 0

                # decrement the right pointer
                right_idx -= 1
                # did the right pointer go past the beginning?
                if right_idx < 0:
                    right_idx = size - 1

                # update the swap count
                swap_count -= 2

            cur_pos += (l + skip_size)
            if cur_pos >= size:
                cur_pos -= size

            skip_size += 1

    return knot_list


def dense_hash_xor(knot_list: list) -> list:
    """Convert the sparse hash list into a dense one using XOR"""
    dense_list = []

    sum = knot_list[0]
    for i in range(1, len(knot_list)):
        if i % 16 == 0:
            dense_list.append(sum)
            sum = 0

        sum = sum ^ knot_list[i]

    dense_list.append(sum)
    return dense_list


def count_used_bits(disk_rows: list) -> int:
    sum_bits = 0

    for row in disk_rows:
        print(row)

        for ch in row:
            if ch == '1' or ch == '2' or ch == '4' or ch == '8':
                sum_bits += 1
            elif ch == '3' or ch == '5' or ch == '6' or ch == '9' or ch == 'a' or ch == 'c':
                sum_bits += 2
            elif ch == '7' or ch == 'b' or ch == 'd' or ch == 'e':
                sum_bits += 3
            elif ch == 'f':
                sum_bits += 4

    return sum_bits


def count_regions(disk_rows: list) -> int:
    """Count the regions designated by '1's in the 128x128 grid"""

    region_count = 0

    # convert the disk rows to a long string of binary digits
    defrag_str = ''

    for row in disk_rows:
        # bin function prepends '0b' onto the binary string
        bstr = bin(int(row, 16))[2:]

        # leading zeroes are not shown so we have to add them
        while len(bstr) < 128:
            bstr = '0' + bstr

        print(bstr)

        # append each binary string to the work string
        defrag_str += bstr

    print(defrag_str)

    # can't modify strings so work with a list
    defrag_l = list(defrag_str)

    # walk the list looking for a '1'
    for idx in range(len(defrag_l)):
        if defrag_l[idx] == '1':
            # track the locations of adjacent 1 bits
            hot_list = []
            defrag_l[idx] = 'A'
            region_count += 1

            # check the east and south compass points for '1's
            # look east if we are not at the right edge
            if (idx % 128) != 127:
                if defrag_l[idx + 1] == '1':
                    hot_list.append(idx + 1)

            # look south if we are not at the bottom edge
            if idx < (127 * 128):
                if defrag_l[idx + 128] == '1':
                    hot_list.append(idx + 128)

            while len(hot_list) > 0:
                # take the last spot to visit off the list
                new_idx = hot_list.pop()

                # mark this spot as visited
                defrag_l[new_idx] = 'A'

                # check all four compass directions for '1's
                # look east if we are not at the right edge
                if (new_idx % 128) != 127:
                    if defrag_l[new_idx + 1] == '1':
                        hot_list.append(new_idx + 1)

                # look south if we are not at the bottom edge
                if new_idx < (127 * 128):
                    if defrag_l[new_idx + 128] == '1':
                        hot_list.append(new_idx + 128)

                # look north if we are not at the top edge
                if new_idx > 127:
                    if defrag_l[new_idx - 128] == '1':
                        hot_list.append(new_idx - 128)

                # look west if we are not at the left edge
                if (new_idx % 128) != 0:
                    if defrag_l[new_idx - 1] == '1':
                        hot_list.append(new_idx - 1)

    return region_count


def disk_defrag(data_str: str) -> list:
    disk_rows = []

    for row in range(128):
        keystr = data_str + '-' + str(row)
        my_list = multi_hash_list(256, keystr, 64)
        disk_rows.append(hexify(dense_hash_xor(my_list)))

    print(disk_rows)

    used_bits = count_used_bits(disk_rows)
    print('Used bits count is', used_bits)

    return disk_rows


test_data = 'flqrgnkx'
test_rows = disk_defrag(test_data)

actual_data = 'uugsqrei'
disk_rows = disk_defrag(actual_data)

test_count = count_regions(test_rows)
print('Test data region count is', test_count)

disk_count = count_regions(disk_rows)
print('Real data region count is', disk_count)
