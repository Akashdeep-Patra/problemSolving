# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
def helper(root,ans,level):
    if(root==None):
        return 
    ans[level].append(root.val)
    helper(root.left,ans,level+1)
    helper(root.right,ans,level+1)
def get_height(root):
    if(root==None):
        return 0
    return 1+max(get_height(root.left),get_height(root.right))
class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def levelOrder(self, root):
	    ans=[[0] for i in range(1) for j in range(get_height(root)) ]
	    helper(root,ans,0)
	    for i in range(len(ans)):
	        ans[i]=ans[i][1:]
        return ans
"""
Level Order
Problem Description

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).



Problem Constraints
1 <= number of nodes <= 105



Input Format
First and only argument is root node of the binary tree, A.



Output Format
Return a 2D integer array denoting the zigzag level order traversal of the given binary tree.



Example Input
Input 1:

    3
   / \
  9  20
    /  \
   15   7
Input 2:

   1
  / \
 6   2
    /
   3


Example Output
Output 1:

 [
   [3],
   [9, 20],
   [15, 7]
 ]
Output 2:

 [ 
   [1]
   [6, 2]
   [3]
 ]


Example Explanation
Explanation 1:

 Return the 2D array. Each row denotes the traversal of each level.

"""