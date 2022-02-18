#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    alice_ranks = []
    scores_norep = [scores[0]]
    for i in range(1,len(scores)):
        if scores[i] != scores_norep[-1]:
            scores_norep.append(scores[i])
    for alice_entry in alice:
        low = 0
        high = len(scores_norep) - 1
        while high >= low:
            mid = (high + low) // 2
            if scores_norep[mid] > alice_entry:
                low = mid + 1
            elif scores_norep[mid] < alice_entry:
                high = mid - 1
            else:
                alice_ranks.append(mid + 1)
                break
        if low == mid + 1:
            alice_ranks.append(mid + 2)
        elif high == mid - 1:
            alice_ranks.append(mid + 1)
    return alice_ranks
            
    
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
