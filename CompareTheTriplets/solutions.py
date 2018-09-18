#!/bin/python

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    
    p1 = 0
    p2 = 0
    
    if len(a) == len(b):
        for ele_a, ele_b in zip(a,b):
            if ele_a > ele_b:
                p1 += 1
            elif ele_a < ele_b:
                p2 += 1
    
    return [p1,p2]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
