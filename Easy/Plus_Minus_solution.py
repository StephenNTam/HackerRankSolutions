#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import *
# Complete the plusMinus function below.
def plusMinus(arr):
    d={1:0,-1:0,0:0}
    for i in arr:
        if i > 0:
            d[1] += 1
        elif i < 0:
            d[-1] += 1
        else:
            d[0] += 1
    x=Decimal(d[1])
    y=Decimal(d[-1])
    z=Decimal(d[0])
    x=round(x/len(arr),5)
    y=round(y/len(arr),5)
    z=round(z/len(arr),5)
    print(x)
    print(y)
    print(z)

    
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
