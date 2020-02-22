#!/usr/bin/env python
""" partition.py

    Usage:

        ./partition.py [clue] in [num squares] from [range]

        [clue] can be, eg, 150x or 10+ or 4-

        [num squares] is an integer

        [range] is an inclusive integer range, eg, 1-4, 1-6, 3-7
        
    For example:

        ./partition.py 150x in 3 from 1-6

            Prints out all 3-square multiplicative partitions of 150 using the
            numbers 1-6.

    The requirement of the delimiter words "in" and "from" is designed to help
    you remember the order and meaning of the arguments.
"""


# ______________________________________________________________________
# Imports

import sys

from collections import Counter
from functools import reduce
from operator import add, mul


# ______________________________________________________________________
# Functions

def partition_with_value(nums, hi, value, op):

    # This could be cleaner, but for our purposes this will already be fast
    # enough. If this will be performed in a tight loop within a speed-critical
    # method, then we would probably want to optimize this.

    print('Max-repeat  Numbers')

    while True:

        # Check to see if we should print the current value.
        if reduce(op, nums) == value:
            max_repeat = Counter(nums).most_common(1)[0][1]
            print(f' {max_repeat:^9d}  {nums}')

        # Increment, maintaining that `nums` is nondecreasing.
        i = len(nums) - 1
        while i >= 0 and nums[i] == hi:
            i -= 1
        if i == -1:
            break
        nums[i] += 1
        nums = [
                nums[j] if j < i else nums[i]
                for j in range(num_sq)
        ]

def add_partition(clue_num, num_sq, lo, hi):
    partition_with_value([lo] * num_sq, hi, clue_num, add)

def mult_partition(clue_num, num_sq, lo, hi):
    partition_with_value([lo] * num_sq, hi, clue_num, mul)


# ______________________________________________________________________
# Main

if __name__ == '__main__':

    if len(sys.argv) < 6:
        print(__doc__)
        sys.exit()
            
    clue, num_sq, range_str = sys.argv[1], int(sys.argv[3]), sys.argv[5]
    lo, hi = range_str.split('-')
    lo, hi = int(lo), int(hi)

    oper = clue[-1]

    if oper == 'x':
        mult_partition(int(clue[:-1]), num_sq, lo, hi)
    elif oper == '+':
        add_partition(int(clue[:-1]), num_sq, lo, hi)
    else:
        print(f'Error: Didn\'t understand operator "{oper}"')
