# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None
import sys 
sys.setrecursionlimit(10**7)
class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, root):
	    if(root==None or root.next==None):
	        return root
	    current=root
	    next=root.next
	    while(next !=None and current.val==next.val):
	        next=next.next
	    current.next=self.deleteDuplicates(next)
	    return current

"""
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None
import sys
sys.setrecursionlimit(10**7)
class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def swapPairs(self, root):
	    if(root==None or root.next==none):
	        return root
	    head=root
	    while(head!=None):
	        temp=head.next.next
	        head.next.next=head
	    if(root==None or root.next==None):
	        return root
	    current=root
	    prev=None
	    next=None
	    counter=0
	    while(current!=None and counter<2):
	        next=current.next
	        current.next=prev
	        prev=current
	        current=next
	        counter+=1
	    root.next=self.swapPairs(next)
	    return prev

"""