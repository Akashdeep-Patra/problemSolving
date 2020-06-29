# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
import sys
# sys.setrecursionlimit(10**7)
def helper(a,b,inorder,in_start,in_end,post_start,post_end):
        if in_start>in_end:
            return None
        root_elem=b[post_end]
        index_inorder=inorder[root_elem]
        root=TreeNode(root_elem)
        # print(root_elem)
        root.left=helper(a,b,inorder,in_start,index_inorder-1,post_start,index_inorder-in_start-1+post_start)
        root.right=helper(a,b,inorder,index_inorder+1,in_end,index_inorder-in_start+post_start,post_end-1)
        return root
class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, a, b):
	    inorder=dict()
	    postorder=dict()
	    for i in range(len(a)):
	        inorder[a[i]]=i
	    n=len(a)-1
	    return helper(a,b,inorder,0,n,0,n)


"""

Binary Tree From Inorder And Postorder
Problem Description

Given inorder and postorder traversal of a tree, construct the binary tree.

NOTE: You may assume that duplicates do not exist in the tree.



Problem Constraints
1 <= number of nodes <= 105



Input Format
First argument is an integer array A denoting the inorder traversal of the tree.

Second argument is an integer array B denoting the postorder traversal of the tree.



Output Format
Return the root node of the binary tree.



Example Input
Input 1:

 A = [2, 1, 3]
 B = [2, 3, 1]
Input 2:

 A = [6, 1, 3, 2]
 B = [6, 3, 2, 1]


Example Output
Output 1:

   1
  / \
 2   3
Output 2:

   1  
  / \
 6   2
    /
   3


Example Explanation
Explanation 1:

 Create the binary tree and return the root node of the tree.

"""