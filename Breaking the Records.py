#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mini, maxim = scores[0], scores[0]
    mini_count, maxim_count = 0, 0
    for i in range(n):
        if i != 0:
            if scores[i] < mini:
                mini = scores[i]
                mini_count += 1
            elif scores[i] > maxim:
                maxim = scores[i]
                maxim_count += 1
    return [maxim_count, mini_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
