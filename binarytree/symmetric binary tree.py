# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
def helper(a,b):
    if((a==None and b!=None) or (a!=None and b==None)):
        return False
    elif(a==b):
        return True
    return a.val==b.val and helper(a.left,b.right) and helper(a.right,b.left)
class Solution:
	# @param A : root node of tree
	# @return an integer
	def isSymmetric(self, root):
	    if(root==None):
	        return 1
	    return 1 if helper(root.left,root.right) else 0


"""
Symmetric Binary Tree
Problem Description

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).



Problem Constraints
1 <= number of nodes <= 105



Input Format
First and only argument is the root node of the binary tree.



Output Format
Return 0 / 1 ( 0 for false, 1 for true ).



Example Input
Input 1:

    1
   / \
  2   2
 / \ / \
3  4 4  3
Input 2:

    1
   / \
  2   2
   \   \
   3    3


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 The above binary tree is symmetric. 
Explanation 2:

The above binary tree is not symmetric.


"""