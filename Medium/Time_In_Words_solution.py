#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    d=[
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine", 
        "ten", "eleven", "twelve", "thirteen", 
        "fourteen", "fifteen", "sixteen", "seventeen", 
        "eighteen", "nineteen", "twenty", "twenty one", 
        "twenty two", "twenty three", "twenty four", 
        "twenty five", "twenty six", "twenty seven", 
        "twenty eight", "twenty nine"
    ]
    
    if m == 0:
        return("{} o' clock".format(d[h]))
    elif m == 15:
        return("quarter past {}".format(d[h]))
    elif m == 30:
        return("half past {}".format(d[h]))
    elif m == 45 and h == 12:
        return("quarter to {}".format(d[1]))
    elif m == 45:
        return("quarter to {}".format(d[h+1]))
    elif m < 30:
        if m == 1:
            return("{} minute past {}".format(d[m],d[h]))
        else:
            return("{} minutes past {}".format(d[m],d[h]))
    elif m > 30 and h==12:
        if m == 1:
            return("{} minute to {}".format(d[60-m],d[1]))
        else:
            return("{} minutes to {}".format(d[60-m],d[1]))
    elif m > 30:
        if m == 1:
            return("{} minute to {}".format(d[60-m],d[h+1]))
        else:
            return("{} minutes to {}".format(d[60-m],d[h+1]))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
