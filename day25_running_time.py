'''
DAY22:
PROBLEM: find prime num or not within sqrt(n) complexity
LINK: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem?isFullScreen=true
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
    
n = int(input())
for i in range(n):
    num = int(input())
    if is_prime(num):
        print('Prime')
    else:
        print('Not prime')
