#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    alice_rank = []
    for i in range(len(alice)):
        append_rank = 1
        j = 0
        while j < len(scores):
            if alice[i] >= scores[j]:
                alice_rank.append(append_rank)
                scores.insert(j, alice[i])
                append_rank = 1
                break
            elif alice[i] < scores[j]:
                k = 0
                while k == 0:
                    j += 1
                    if j >= len(scores):
                        k+= 1
                        append_rank += 1
                        alice_rank.append(append_rank)
                    elif scores[j-1] != scores[j]:
                        k += 1
                        append_rank += 1
    return alice_rank
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
