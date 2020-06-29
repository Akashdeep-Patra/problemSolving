# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
from collections import deque
class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def zigzagLevelOrder(self, root):
	    q=deque()
	    ans=[]
	    flag=1
	    q.append(root)
	    while(q):
	        collector=deque()
	        temp_q=q
	        q=deque()
	        while(temp_q):
	            temp=temp_q.pop()
	            if(temp==None):
	                continue
	            if(flag==1):
	                collector.append(temp.val)
	            else:
	                collector.appendleft(temp.val)
	            q.appendleft(temp.left)
	            q.appendleft(temp.right)
            # if(flag==1 and collector):
            #     ans.append(collector[:])
            # elif(flag==-1 and collector):
            #     ans.append(collector[::-1])
            if(collector):
                ans.append(collector)
            flag*=-1
        return ans
"""
ZigZag Level Order Traversal BT
Problem Description

Given a binary tree, return the zigzag level order traversal of its nodes values. (ie, from left to right, then right to left for the next level and alternate between).



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
   [20, 9],
   [15, 7]
 ]
Output 2:

 [ 
   [1]
   [2, 6]
   [3]
 ]


Example Explanation
Explanation 1:

 Return the 2D array. Each row denotes the zigzag traversal of each level.


"""