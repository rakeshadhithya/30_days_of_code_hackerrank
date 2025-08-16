'''
DAY14:
PROBLEM: understand the scope of variables in class and method, use this or self to avoid confusion
LINK: https://www.hackerrank.com/challenges/30-scope/problem?isFullScreen=true
'''

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = -float('inf')
    
	# Add your code here
    def computeDifference(self):
        self.maximumDifference = abs(max(self.__elements) - min(self.__elements))

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)