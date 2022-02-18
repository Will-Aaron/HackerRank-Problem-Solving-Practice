#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    height, num_valley = 0, 0
    for ch in s:
        if ch == 'U':
            height += 1
        elif ch == 'D':
            height -= 1
            if height == -1:
                num_valley += 1
    return num_valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
