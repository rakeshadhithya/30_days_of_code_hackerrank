'''
DAY5:
PROBLEM: Review LOOPS 
LINK: https://www.hackerrank.com/challenges/30-arrays/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    for i in range(1, len(arr)+1):
        print(arr[-i], end=' ')
