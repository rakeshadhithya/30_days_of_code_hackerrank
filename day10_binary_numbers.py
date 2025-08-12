'''
DAY10:
PROBLEM: Find maximum 1's in binary equivalent of given integer
LINK: https://www.hackerrank.com/challenges/30-binary-numbers/problem
'''

import math
import os
import random
import re
import sys

#function to covert decimal to binary str
def binary(n):
    #take list to store 0's, 1's
    binary_digits = []
    #while n > 0
    while n > 0:
        #take remainder and divide by 2, append remainder to binary_digits
        remainder = n % 2
        n = n // 2                       #integer division
        binary_digits.append(remainder)
    #reverse the binary_digits & return in str format
    return ''.join([ str(i) for i in reversed(binary_digits)])

def recursive_binary(n):
    #if n < 2 return str of n. combines if n==1 return '1' and n==0 return '0'
    if n < 2:
        return str(n)
    #return ans(n//2) + remainder n % 2
    return recursive_binary(n//2) + str(n%2)
    
if __name__ == '__main__':
    n = int(input().strip())
    #convert to binary str
    binary_str = recursive_binary(n)
    #initial window and it's ans(max)
    left = right = 0
    maximum = 0
    #while right reaches end next
    while right < len(binary_str):
        c = binary_str[right]
        #if 1 move right, update maximum
        if c == '1':
            right += 1
            maximum = max(maximum, right - left)
        #else move left & right to next of right
        else:
            left = right+1
            right += 1
    #return maximum
    print(maximum)
    
