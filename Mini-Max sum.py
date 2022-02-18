#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    maxim = sum(arr) - arr[0]
    mini = sum(arr) - arr[-1]
    print('{} {}'.format(mini, maxim))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
