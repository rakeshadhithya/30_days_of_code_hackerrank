'''
DAY06:
PROBLEM: Review LOOPS 
LINK: https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

for t in range(n):
    str = input()
    even = ''
    odd = ''
    for i in range(0, len(str)):
        if i % 2 == 0:
            even += str[i]
        else:
            odd += str[i]
    print(even, odd)
