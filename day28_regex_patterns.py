'''
DAY27:
PROBLEM: find firstname, email pairs whose gmail ending with @gmail.com and sort based on firstname
LINK: https://www.hackerrank.com/challenges/30-regex-patterns/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    
    emails = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        
        emails.append((firstName, emailID))
    
    ans = []
    for fn, e in emails:
        if e.endswith('@gmail.com'):
            ans.append(fn)
    for x in sorted(ans):
        print(x)
    
