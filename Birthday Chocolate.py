#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    summation = sum(s[q] for q in range(m))
    if summation == d:
        count +=1
    for k in range(n-m):
        summation = summation - s[k] + s[k+m]
        if summation == d:
            count +=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
