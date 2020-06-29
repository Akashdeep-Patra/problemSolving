# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def helper(root,flag):
    if(root==None):
        return 0
    return root.val*flag+helper(root.left,flag*-1)+helper(root.right,flag*-1)
class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, root):
        return helper(root,1)


"""
bookmark-empty
Odd and Even Levels
Problem Description

Given a binary tree of integers. Find the difference between the sum of nodes at odd level and sum of nodes at even level.

NOTE: Consider the level of root node as 1.



Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 109



Input Format
First and only argument is a root node of the binary tree, A



Output Format
Return an integer denoting the difference between the sum of nodes at odd level and sum of nodes at even level.



Example Input
Input 1:

        1
      /   \
     2     3
    / \   / \
   4   5 6   7
  /
 8 
Input 2:

        1
       / \
      2   10
       \
        4


Example Output
Output 1:

 10
Output 2:

 -7


Example Explanation
Explanation 1:

 Sum of nodes at odd level = 23
 Sum of ndoes at even level = 13
Explanation 2:

 Sum of nodes at odd level = 5
 Sum of ndoes at even level = 12
"""