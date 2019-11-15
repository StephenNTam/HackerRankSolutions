#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if 'PM' in s:
        pm = int(s[0:2])
        if pm == 12:
            pm = 12
        else:
            pm+=12
        return str(pm) + s[2:-2]
    else:
        am = int(s[0:2])
        if am == 12:
            am = "00"
            return str(am) + s[2:-2]
        return s[0:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
