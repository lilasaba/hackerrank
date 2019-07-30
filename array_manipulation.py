# vim: tabstop=8 expandtab shiftwidth softtabstop=4

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    out = [0 for i in range(n)]
    maxval = 0
    maxlocal = 0

    for sub in queries:
        a, b, k = sub
        a -= 1
        b -= 1
        out[a] += k
        try:
            out[b+1] -= k
        except IndexError:
            pass
    for item in out:
        maxlocal += item
        if maxlocal > maxval:
            maxval = maxlocal

    return maxval


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

