#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_hitcount = 0
    orange_hitcount = 0
    for i in range(m):
        if s <= (apples[i] + a) <= t:
            apple_hitcount +=1
    for k in range(n):
        if s <= (oranges[k] + b) <= t:
            orange_hitcount += 1
    print(apple_hitcount)
    print(orange_hitcount)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
