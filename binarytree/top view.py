# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque
def helper(root,index,level,mem):
    if(root==None):
        return 
    if index not in mem:
        mem[index]=[level,root.val]
    else:
        if level<mem[index][0]:
            mem[index]=[level,root.val]
    helper(root.left,index-1,level+1,mem)
    helper(root.right,index+1,level+1,mem)
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, root):
        mem=dict()
        helper(root,0,0,mem)
        return [x[1] for x in mem.values()]
        

"""
TOP VIEW
Problem Description

Given a binary tree of integers denoted by root A. Return an array of integers representing the top view of the Binary tree.

Right view of a Binary Tree is a set of nodes visible when the tree is visited from top.

Return the nodes in any order.



Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format
First and only argument is head of the binary tree A.



Output Format
Return an array, representing the top view of the binary tree.



Example Input
Input 1:

 
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 
Input 2:

 
            1
           /  \
          2    3
           \
            4
             \
              5


Example Output
Output 1:

 [1, 2, 4, 8, 3, 7]
Output 2:

 [1, 2, 3]


Example Explanation
Explanation 1:

Top view is described.
Explanation 2:

Top view is described.


"""