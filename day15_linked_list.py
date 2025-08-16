'''
DAY15:
PROBLEM: add a element at the end of given linked list head
LINK: https://www.hackerrank.com/challenges/30-linked-list/problem?isFullScreen=true
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        #if head is None return new node
        if head == None:
            return Node(data)
        #move ptr from head to last node
        ptr = head
        while ptr.next != None:
            ptr = ptr.next
        #change next of last node, return head
        ptr.next = Node(data)
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  