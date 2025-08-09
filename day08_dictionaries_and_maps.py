'''
DAY8:
PROBLEM: Dictionaries and Maps 
LINK: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?isFullScreen=true
'''

n = int(input())
dictionary = {}
for i in range(n):
    entry = input().split()
    dictionary[entry[0]] = entry[1]
#reads unknown number of inputs
while(True):
    try:
        name = input()
        if name in dictionary:
            print(f'{name}={dictionary[name]}')
        else:
            print('Not found')
    except EOFError:
        break

