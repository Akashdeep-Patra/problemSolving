# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None
def findMid(root):
    slow=root
    fast=root
    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
    return slow
def compare(root1,root2):
    while(root1!=None or root2!=None):
        if(root1==root2):
            return True
        if((root1==None and root2!=None) or (root1!=None and root2==None) or (root1.val!=root2.val)):
            return False
        root1=root1.next
        root2=root2.next
    return True
class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, root):
	    if(root==None or root.next==None):
	        return 1
	    mid=findMid(root)
	    current=root
	    prev,next=None,None
	    while(next!=mid):
	        next=current.next
	        current.next=prev
	        prev=current
	        current=next
	   # print(next.val)
	    return 1 if (compare(prev,next) or compare(prev,next.next)) else 0


"""
Palindrome List
Problem Description

Given a singly linked list A, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.



Problem Constraints
1 <= |A| <= 105



Input Format
The first and the only argument of input contains a pointer to the head of the given linked list.



Output Format
Return 0, if the linked list is not a palindrome.

Return 1, if the linked list is a palindrome.



Example Input
Input 1:

A = [1, 2, 2, 1]
Input 2:

A = [1, 3, 2]


Example Output
Output 1:

 1 
Output 2:

 0 


Example Explanation
Explanation 1:

 The first linked list is a palindrome as [1, 2, 2, 1] is equal to its reversed form.
Explanation 2:

 The second linked list is not a palindrom as [1, 3, 2] is not equal to [2, 3, 1].
"""