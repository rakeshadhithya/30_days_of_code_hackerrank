'''
DAY22:
PROBLEM: implement binary tree level order traversal
LINK: https://www.hackerrank.com/challenges/30-binary-trees/problem?isFullScreen=true
'''

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
        
    
    def levelOrder(self,root):
        #write your code here
        import queue
        #create queue, add root
        q = queue.Queue()
        q.put(root)
        #while q not empty, pop process(print with space) if not null add childs
        while not q.empty():
            node = q.get()
            print(node.data, end=' ')
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

'''
      3
   2     5
1       4  7

queue = 
stout = 3 2 5 1 4 7
'''
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
