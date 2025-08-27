'''
DAY26:
PROBLEM: find library fine 
LINK: https://www.hackerrank.com/challenges/30-nested-logic/problem?isFullScreen=true
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
#after year, 1000 fine
#same year, after month, 500 x number of months late
#same month, 15 x number of days late
#on or before date, 0 fine
return_date = list(map(int, input().split()))
due_date = list(map(int, input().split()))

#after year
if return_date[2] > due_date[2]:
    print(10000)
#same year
elif return_date[2] == due_date[2]:
    #after month
    if return_date[1] > due_date[1]:
        print(500 * (return_date[1] - due_date[1]))
    #same month after day
    elif return_date[1] == due_date[1] and return_date[0] > due_date[0]:
        print(15 * (return_date[0] - due_date[0]))
    #same month before day
    else:
        print(0)
#before year
else:
    print(0)
        
        
        
