MOD_FACTOR = 2147483647
GEN_A_MULTIPLIER = 16807
GEN_B_MULTIPLIER = 48271

ITER_COUNT = 40000000

def next_a_val(in_val: int) -> int:
    return (in_val * GEN_A_MULTIPLIER) % MOD_FACTOR


def next_b_val(in_val: int) -> int:
    return (in_val * GEN_B_MULTIPLIER) % MOD_FACTOR


def count_gen_matches(a_val: int, b_val: int) -> int:
    """for 40,000,000 iterations generate new a and b values
       then compare the low 16 bits to see if they match
       Return the number of matching iterations"""

    match_count = 0

    for idx in range(ITER_COUNT):
        # generate the next values
        a_val = next_a_val(a_val)
        b_val = next_b_val(b_val)

        # get the rightmost 16 bits of each number
        match_a = a_val % 65536
        match_b = b_val % 65536

        # if they match, increment the counter
        if match_a == match_b:
            match_count += 1

    return match_count


test_a = 65
test_b = 8921

for idx in range(5):
    test_a = next_a_val(test_a)

    test_b = next_b_val(test_b)

    print(test_a, "   ", test_b)

test_match_count = count_gen_matches(test_a, test_b)
print('Test match count is', test_match_count)

real_a = 277
real_b = 349

match_count = count_gen_matches(real_a, real_b)
print('Match count is', match_count)

