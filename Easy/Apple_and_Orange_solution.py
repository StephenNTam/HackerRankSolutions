#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    numa=0
    numb=0
    apples = [x+a for x in apples]
    oranges = [x+b for x in oranges]

    for i in apples:
        if i >= s and i <= t:
            numa+=1

    for i in oranges:
        if i >= s and i <= t:
            numb+=1
    
    print(numa)
    print(numb)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
