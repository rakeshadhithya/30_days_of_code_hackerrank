'''
DAY11:
PROBLEM: Find maximum hourglass sum in given matrix
LINK: https://www.hackerrank.com/challenges/30-2d-arrays/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#function to sum hourglass elements in 3*3 matrix from given row,col
def hourglass_total(arr, row, col):
    row1total = arr[row][col] + arr[row][col+1] + arr[row][col+2]
    row3total = arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
    middle_element = arr[row+1][col+1]
    return row1total + middle_element + row3total

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    #for each 3*3 in given matrix, update max_hourglass_total
    max_hourglass_total = -float('inf')  #you can take 1st hourglass sum also
    for row in range(len(arr) - 2):
        for col in range(len(arr[0]) - 2):
            max_hourglass_total = max(max_hourglass_total, hourglass_total(arr, row, col))
    print(max_hourglass_total)
    
    
    
    