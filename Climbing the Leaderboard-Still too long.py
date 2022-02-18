#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores_repeatless = []
    alice_rank = []
    for q in scores:
        if q not in scores_repeatless:
            scores_repeatless.append(q)
    print(scores_repeatless)
    for i in range(len(alice)):
        append_rank = 1
        for j in range(len(scores_repeatless)):
            if alice[i] > scores_repeatless[j]:
                alice_rank.append(append_rank)
                append_rank = 1
                scores_repeatless.insert(j, alice[i])
                break
            elif alice[i] == scores_repeatless[j]:
                alice_rank.append(append_rank)
                append_rank = 1
                break
            elif alice[i] < scores_repeatless[j]:
                append_rank += 1
            if j == len(scores_repeatless) - 1:
                alice_rank.append(append_rank)
                scores_repeatless.append(alice[i])
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
