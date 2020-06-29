# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
from collections import deque
from collections import defaultdict
def helper(root,mem,index,level):
    if(root==None):
        return
    
    mem[index].append([level,root.val])
    helper(root.left,mem,index+1,level+1)
    helper(root.right,mem,index-1,level+1)
    
class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def verticalOrderTraversal(self, root):
	   # width,root_pos=get_width(root)
	    mem=defaultdict(deque)
	    helper(root,mem,0,0)
	    ans=[]
	    for key in sorted(mem.keys(),reverse=True):
	        row=mem[key]
	        row=sorted(row,key=lambda x:x[0])
	        row=[x[1] for x in row] 
	        ans.append(row)
	   # print(mem)
	    return ans
	        


"""
Vertical Order traversal
Problem Description

Given a binary tree, return a 2-D array with vertical order traversal of it. Go through the example and image for more details.


NOTE: If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.



Problem Constraints
1 <= number of nodes <= 105



Input Format
First and only arument is a pointer to the root node of binary tree, A.



Output Format
Return a 2D array denoting the vertical order traversal of tree as shown.



Example Input
Input 1:

      6
    /   \
   3     7
  / \     \
 2   5     9
Input 2:

      1
    /   \
   3     7
  /       \
 2         9


Example Output
Output 1:

 [
    [2],
    [3],
    [6, 5],
    [7],
    [9]
 ]
Output 2:

 [
    [2],
    [3],
    [1],
    [7],
    [9]
 ]


Example Explanation
Explanation 1:

 First row represent the verical line 1 and so on.
"""