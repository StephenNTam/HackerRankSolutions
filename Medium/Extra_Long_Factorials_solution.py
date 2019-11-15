#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if n == 0:
        return 0
    result=1
    for i in range(1,n+1):
        result *= i
    print(result)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
