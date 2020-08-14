#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    cycles = 1
    tree_height = 1

    for cycle in range(0, n):
        if cycles == 4:
            cycles = 1

        if cycles == 2:
            tree_height = tree_height * 2 + 1
        else:
            tree_height = tree_height + 1

        cycles = cycles + 1

    if n > 4:
        tree_height = tree_height - 1
        
    return tree_height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
