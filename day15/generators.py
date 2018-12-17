MOD_FACTOR = 2147483647
GEN_A_MULTIPLIER = 16807
GEN_B_MULTIPLIER = 48271

ITER_COUNT = 40000000

# Part 2 - only send values that are multiples
A_SEND = 4
B_SEND = 8

# Part 2 - new iteration count
PART2_ITER_COUNT = 5000000


class Generator:
    """A class to generate numbers"""
    def __init__(self, start_v: int, m: int, r: int):
        self.val = start_v
        self.multiplier = m
        self.remainder = r

    def next_val(self) -> int:
        self.val = (self.val * self.multiplier) % self.remainder
        return self.val


def next_a_val(in_val: int) -> int:
    return (in_val * GEN_A_MULTIPLIER) % MOD_FACTOR


def next_b_val(in_val: int) -> int:
    return (in_val * GEN_B_MULTIPLIER) % MOD_FACTOR


def count_gen_matches(a_val: int, b_val: int) -> int:
    """for 40,000,000 iterations generate new a and b values
       then compare the low 16 bits to see if they match
       Return the number of matching iterations"""

    print('Getting match count...')
    match_count = 0

    gen_a = Generator(a_val, GEN_A_MULTIPLIER, MOD_FACTOR)
    gen_b = Generator(b_val, GEN_B_MULTIPLIER, MOD_FACTOR)

    for idx in range(ITER_COUNT):
        # generate the next values
        a_num = gen_a.next_val()
        b_num = gen_b.next_val()

        # get the rightmost 16 bits of each number
        match_a = a_num % 65536
        match_b = b_num % 65536

        # if they match, increment the counter
        if match_a == match_b:
            match_count += 1

    return match_count


test_a = 65
test_b = 8921

test_gen_a = Generator(test_a, GEN_A_MULTIPLIER, MOD_FACTOR)
test_gen_b = Generator(test_b, GEN_B_MULTIPLIER, MOD_FACTOR)

for idx in range(5):
    num_a = test_gen_a.next_val()
    num_b = test_gen_b.next_val()

    print(num_a, "   ", num_b)

test_match_count = count_gen_matches(test_a, test_b)
print('Test match count is', test_match_count)

real_a = 277
real_b = 349

match_count = count_gen_matches(real_a, real_b)
print('Match count is', match_count)

