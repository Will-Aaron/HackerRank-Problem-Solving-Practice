#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year <= 1917:
        if year % 4 == 0:
            s = '12.09.'
        else:
            s = '13.09.'
    elif year == 1918:
        s = '26.09.'
    elif year >= 1919:
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            s = '12.09.'
        else:
            s = '13.09.'
    return s + str(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
