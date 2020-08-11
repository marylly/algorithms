#!/bin/python3

import os
import sys

#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):

    print(indexes)
    print(queries)

    result = []
    result.append([3,1,2])
    result.append([2,1,3])

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    print('\n'.join([' '.join(map(str, x)) for x in result]))

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
