#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
#this is all wrong
def pickingNumbers(a):
    subarray_lengths = []
    for i in range(len(a)):
        subarray_lengths.append(a.count(a[i]) + a.count(a[i]+1))
    return max(subarray_lengths)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
