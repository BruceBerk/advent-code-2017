# Advent of Code 2017-10
# Knot Hash
#
# Bruce Berkowicz
# bruceberk@me.com
# 12/29/17
#

"""
--- Day 10: Knot Hash ---

You come across some programs that are trying to implement a software emulation of a hash based on knot-tying. The hash
these programs are implementing isn't very strong, but you decide to help them anyway. You make a mental note to remind
the Elves later not to invent their own cryptographic functions.

This hash function simulates tying a knot in a circle of string with 256 marks on it. Based on the input to be hashed,
the function repeatedly selects a span of string, brings the ends together, and gives the span a half-twist to reverse
the order of the marks within it. After doing this many times, the order of the marks is used to build the resulting
hash.

  4--5   pinch   4  5           4   1
 /    \  5,0,1  / \/ \  twist  / \ / \
3      0  -->  3      0  -->  3   X   0
 \    /         \ /\ /         \ / \ /
  2--1           2  1           2   5
To achieve this, begin with a list of numbers from 0 to 255, a current position which begins at 0 (the first element in
the list), a skip size (which starts at 0), and a sequence of lengths (your puzzle input). Then, for each length:

Reverse the order of that length of elements in the list, starting with the element at the current position.
Move the current position forward by that length plus the skip size.
Increase the skip size by one.
The list is circular; if the current position and the length try to reverse elements beyond the end of the list, the
operation reverses using as many extra elements as it needs from the front of the list. If the current position moves
past the end of the list, it wraps around to the front. Lengths larger than the size of the list are invalid.

Here's an example using a smaller list:

Suppose we instead only had a circular list containing five elements, 0, 1, 2, 3, 4,
and were given input lengths of 3, 4, 1, 5.

The list begins as [0] 1 2 3 4 (where square brackets indicate the current position).
The first length, 3, selects ([0] 1 2) 3 4 (where parentheses indicate the sublist to be reversed).
After reversing that section (0 1 2 into 2 1 0), we get ([2] 1 0) 3 4.
Then, the current position moves forward by the length, 3, plus the skip size, 0: 2 1 0 [3] 4. Finally, the skip size
increases to 1.
The second length, 4, selects a section which wraps: 2 1) 0 ([3] 4.
The sublist 3 4 2 1 is reversed to form 1 2 4 3: 4 3) 0 ([1] 2.
The current position moves forward by the length plus the skip size, a total of 5, causing it not to move because it
wraps around: 4 3 0 [1] 2. The skip size increases to 2.
The third length, 1, selects a sublist of a single element, and so reversing it has no effect.
The current position moves forward by the length (1) plus the skip size (2): 4 [3] 0 1 2. The skip size increases to 3.
The fourth length, 5, selects every element starting with the second: 4) ([3] 0 1 2. Reversing this sublist (3 0 1 2 4
into 4 2 1 0 3) produces: 3) ([4] 2 1 0.
Finally, the current position moves forward by 8: 3 4 2 1 [0]. The skip size increases to 4.
In this example, the first two numbers in the list end up being 3 and 4; to check the process, you can multiply them
together to produce 12.

However, you should instead use the standard list size of 256 (with values 0 to 255) and the sequence of lengths in
your puzzle input. Once this process is complete, what is the result of multiplying the first two numbers in the list?

Answer: 4480
"""

def hash_list(size: int, lengths: list) -> int:
    """Perform successive reverses of sublists on a list and then multiply the first two elements together"""
    product = 0

    # start the list, based on size
    knot_list = []
    for i in range(size):
        knot_list.append(i)

    cur_pos = 0
    skip_size = 0

    print(knot_list)

    for l in lengths:
        left_idx = cur_pos
        right_idx = cur_pos + l - 1
        swap_count = l

        # does the sublist to reverse wrap around?
        if right_idx >= size:
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

    print(knot_list)

    return knot_list[0] * knot_list[1]


def test_hash():
    size = 5
    lengths = [3, 4, 1, 5]

    product = hash_list(size, lengths)
    if product == 12:
        result = "Pass."
    else:
        result = "Fail."

    print(result, "Returned product is", product)


test_hash()

size = 256
with open('data/input10.txt') as f:
    data = f.read().split(',')
    datanums = [int(item) for item in data]
    product = hash_list(size, datanums)
    print('Answer is', product)