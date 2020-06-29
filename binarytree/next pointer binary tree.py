
# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
def getNext(root):
    while(root):
        if(root.left):
            return root.left
        if(root.right):
            return root.right
        root=root.next
    return None
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        top=root
        while(top!=None):
            temp=top
            while(temp!=None):
                if(temp.left):
                    if(temp.right):
                        temp.left.next=temp.right
                    else:
                        temp.left.next=getNext(temp.next)
                if(temp.right):
                    temp.right.next=getNext(temp.next)
                temp=temp.next
            top=top.left
        return root
                
        

"""
Next Pointer Binary Tree
Problem Description

Given a binary tree,

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Assume perfect binary tree and try to solve this in constant extra space.



Problem Constraints
1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format
First and only argument is head of the binary tree A.



Output Format
Return the head of the binary tree after the changes are made.



Example Input
Input 1:

 
     1
    /  \
   2    3
Input 2:

 
        1
       /  \
      2    5
     / \  / \
    3  4  6  7


Example Output
Output 1:

 
        1 -> NULL
       /  \
      2 -> 3 -> NULL
Output 2:

 
         1 -> NULL
       /  \
      2 -> 5 -> NULL
     / \  / \
    3->4->6->7 -> NULL


Example Explanation
Explanation 1:

Next pointers are set as given in the output.
Explanation 2:

Next pointers are set as given in the output.
"""