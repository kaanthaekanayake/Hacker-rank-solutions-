#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    result = []
    newWord = True
    for c in s:
        if (c.isspace()):
            result.append(c)
            newWord = True
        else:
            if (newWord):
                if(c.isalpha):
                    result.append(c.upper())
                    newWord = False
                else:
                    result.append(c)
                    newWord = False
            else:
                result.append(c)
    
    FullName = "".join(result)
    print(FullName)
    return FullName


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
