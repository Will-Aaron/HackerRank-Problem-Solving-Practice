#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #paper_total = 0
    #target_paper = 0
    #turns_front = 0
    #turns_back = 0
    if n%2 == 0:
        paper_total = n / 2
        if p%2 == 0:
            target_paper = p / 2
            turns_front = target_paper
            turns_back = paper_total - target_paper
            return int(min(turns_front, turns_back))
        if p%2 == 1:
            target_paper = (p+1) / 2
            turns_front = target_paper - 1
            turns_back = abs(paper_total - target_paper + 1)
            return int(min(turns_front, turns_back))
    if n%2 == 1:
        paper_total = (n+1) / 2
        if p%2 == 0:
            target_paper = p / 2
            turns_front = target_paper
            turns_back = abs(paper_total - target_paper - 1)
            return int(min(turns_front, turns_back))
        if p%2 == 1:
            target_paper = (p+1) / 2
            turns_front = target_paper - 1
            turns_back = paper_total - target_paper
            return int(min(turns_front, turns_back))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
