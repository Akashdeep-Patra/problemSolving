# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys
sys.setrecursionlimit(10**7)
import math as m
from collections import deque
def helper(mem,level):
    if(level not in mem or len(mem[level])==0):
        return 
    # print(level)
    # print(mem,level)
    x=mem[level].popleft()
    if(x==-1):
        return 
    root=TreeNode(x)
    root.left=helper(mem,level+1)
    root.right=helper(mem,level+1)
    return root
class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def solve(self, a):
        q=deque()
        i=1
        ans=TreeNode(a[0])
        q.append(ans)
        while(q and i<len(a)):
            root=q.pop()
            if(a[i]==-1):
                root.left=None
            else:
                root.left=TreeNode(a[i])
                q.appendleft(root.left)
            i+=1
            if(a[i]==-1):
                root.right=None
            else:
                root.right=TreeNode(a[i])
                q.appendleft(root.right)
            i+=1
        return ans
            
        
        

"""

Deserialize Binary Tree
Problem Description

Given an integer array A denoting the Level Order Traversal of the Binary Tree.

You have to Deserialize the given Traversal in the Binary Tree and return the root of the Binary Tree.

NOTE:

In the array, the NULL/None child is denoted by -1.
For more clarification check the Example Input.


Problem Constraints
1 <= number of nodes <= 105

-1 <= A[i] <= 105



Input Format
Only argument is an integer array A denoting the Level Order Traversal of the Binary Tree.



Output Format
Return the root node of the Binary Tree.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
Input 2:

 A = [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1]


Example Output
Output 1:

           1
         /   \
        2     3
       / \
      4   5
Output 2:

            1
          /   \
         2     3
        / \ .   \
       4   5 .   6


Example Explanation
Explanation 1:

 Each element of the array denotes the value of the node. If the val is -1 then it is the NULL/None child.
 Since 3, 4 and 5 each has both NULL child we had represented that using -1.
Explanation 2:

 Each element of the array denotes the value of the node. If the val is -1 then it is the NULL/None child.
 Since 3 has left child as NULL while 4 and 5 each has both NULL child.

"""