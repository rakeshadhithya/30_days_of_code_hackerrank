'''
DAY20:
PROBLEM: implement bubble sort
LINK: https://www.hackerrank.com/challenges/30-sorting/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    totalswaps = 0
    #traverse through all array elements
    for i in range(n):
        currswaps = 0
        #last i elements are already in place
        for j in range(n-i-1):
            #if elements in decresing order, swap
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                currswaps += 1
        totalswaps += currswaps
        #stop when currswaps are zero, means sorted
        if currswaps == 0:
            print(f'Array is sorted in {totalswaps} swaps.')
            print(f'First Element: {a[0]}')
            print(f'Last Element: {a[-1]}')
            break
