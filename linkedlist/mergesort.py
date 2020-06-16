# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None
import sys
sys.setrecursionlimit(10**7)
def merge(root1,root2):
    if(root1==None):
        return root2
    if(root2==None):
        return root1
    if(root1.val<root2.val):
        root1.next=merge(root1.next,root2)
        return root1
    root2.next=merge(root1,root2.next)
    return root2
class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def sortList(self, root):
	    if(root==None or root.next==None):
	        return root
	    slow=root
	    fast=root
	    while(fast!=None and fast.next!=None and fast.next.next!=None):
	        slow=slow.next
	        fast=fast.next.next
	    temp=slow.next
	    slow.next=None
	    firstHalf=self.sortList(root)
	    secondHalf=self.sortList(temp)
	    return merge(firstHalf,secondHalf)
	        


"""
Sort List
Problem Description

Sort a linked list, A in O(n log n) time using constant space complexity.



Problem Constraints
0 <= |A| = 105



Input Format
The first and the only arugment of input contains a pointer to the head of the linked list, A.



Output Format
Return a pointer to the head of the sorted linked list.



Example Input
Input 1:

A = [3, 4, 2, 8]
Input 2:

A = [1]


Example Output
Output 1:

[2, 3, 4, 8]
Output 2:

[1]


Example Explanation
Explanation 1:

 The sorted form of [3, 4, 2, 8] is [2, 3, 4, 8].
Explanation 2:

 The sorted form of [1] is [1].

"""