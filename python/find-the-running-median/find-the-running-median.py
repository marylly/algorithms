#!/bin/python3

import os
import sys
import math
import bisect

#
# Complete the runningMedian function below.
#
def runningMedian(a):
    running_medians = []
    current_position_array = []
    array_len = 0
    for integer in range(0, len(a)):
        bisect.insort(current_position_array, a[integer])
        array_len = array_len + 1
        array_middle_index = 0
        array_middle_index = math.floor(array_len/2)
        if array_len == 1:
            running_medians.append(a[integer])
        elif array_len % 2 == 0:
            running_medians.append((current_position_array[array_middle_index-1] + current_position_array[array_middle_index]) / 2)
        else:
            running_medians.append(current_position_array[array_middle_index])

    return list(map(float,running_medians))   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
