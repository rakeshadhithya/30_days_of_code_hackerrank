'''
DAY24:
PROBLEM: delete duplicate elements from the linked list
LINK: https://www.hackerrank.com/challenges/30-linked-list-deletion/problem?isFullScreen=true
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        if head == None:
            return None
        st = set()
        nh = nt = Node(0)
        ptr = head
        while ptr:
            if ptr.data not in st:
                st.add(ptr.data)
                nt.next = ptr
                nt = nt.next
            ptr = ptr.next
        nt.next = None
        return nh.next
'''
1 2 2 3 3 4
          i
set = 1 2 3 4
nh = 0
nt = 0 1 2 3 4
''' 
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 