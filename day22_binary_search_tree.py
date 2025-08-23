'''
DAY22:
PROBLEM: write a method to find the height(no. of edges) in a bst
LINK: https://www.hackerrank.com/challenges/30-binary-search-trees/problem?isFullScreen=true
'''
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

    def getHeight(self,root):
        #Write your code here
        if root == None:
            #-1 becoz for single node tree height is 0
            return - 1
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       