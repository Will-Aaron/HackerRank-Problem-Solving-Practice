#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == 'PM':
        if int(s[:2]) != 12:
            hour = int(s[:2]) + 12
            w = str(hour) + s[2:-2]
            return w
        else:
            w = s[:-2]
            return w
    elif s[-2:] == 'AM':
        if int(s[:2]) == 12:
            w = '00' + s[2:-2]
            return w
        w = s[:-2]
        return w

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
