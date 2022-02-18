#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    maxim = 0
    occur = 1
    for i in range(ar_count):
        if ar[i] > maxim:
            maxim = ar[i]
            occur = 1
        elif ar[i] == maxim:
            occur += 1
    return occur

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
