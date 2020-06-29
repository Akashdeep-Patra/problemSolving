# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def helper(root):
    if(root==None):
        return 0,-1
    left_diameter,left_height=helper(root.left)
    right_diameter,right_height=helper(root.right)
    return max(2+left_height+right_height,left_diameter,right_diameter),1+max(right_height,left_height)
class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, root):
        ans,height=helper(root)
        return ans


"""
Diameter of binary tree
Problem Description

Given a Binary Tree A consisting of N integer nodes, you need to find the diameter of the tree.

The diameter of a tree is the number of edges on the longest path between two nodes in the tree.



Problem Constraints
0 <= N <= 105



Input Format
First and only Argument represents the root of binary tree A.



Output Format
Return an single integer denoting the diameter of the tree.



Example Input
Input 1:

           1
         /   \
        2     3
       / \
      4   5
Input 2:

            1
          /   \
         2     3
        / \     \
       4   5     6


Example Output
Output 1:

 3
Output 2:

 4


Example Explanation
Explanation 1:

 Longest Path in the tree is 4 -> 2 -> 1 -> 3 and the number of edges in this path is 3 so diameter is 3.
Explanation 2:

 Longest Path in the tree is 4 -> 2 -> 1 -> 3 -> 6 and the number of edges in this path is 4 so diameter is 4.

"""