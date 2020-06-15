# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None
def merge(root1,root2):
    if(root1==None):
        return root2
    if(root2==None):
        return root1
    root1.next=merge(root2,root1.next)
    return root1
def merge_iter(root1,root2):
    head=root1
    ans=root1
    root1=root1.next
    flag=0
    while(root1!=None and root2!=None):
        if(flag==0):
            head.next=root2
            root2=root2.next
            head=head.next
            flag=1
        else:
            head.next=root1
            root1=root1.next
            head=head.next
            flag=0
    if(root1!=None):
        head.next=root1
    if(root2!=None):
        head.next=root2
    return ans
def find_mid(root):
    slow=root
    fast=root
    while(fast!=None and fast.next!=None ):
        slow=slow.next
        fast=fast.next.next
    return slow
        
def reverse(root):
    if(root==None):
        return None
    if(root.next==None):
        return root
    rest=reverse(root.next)
    root.next.next=root
    root.next=None
    return rest
def reverse_iter(root):
    if(root==None or root.next==None):
        return root
    current=root
    prev=None
    while(current!=None):
        next=current.next
        current.next=prev
        prev=current
        current=next
    return prev
class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reorderList(self, root):
	    if(root==None or root.next==None or root.next.next==None):
	        return root
	    mid=find_mid(root)
	    rev=reverse_iter(mid.next)
	    mid.next=None
	    ans=merge_iter(root,rev)
	    return ans
	    




"""
Reorder List
Problem Description

Given a singly linked list A

 A: A0 → A1 → … → An-1 → An 
reorder it to:

 A0 → An → A1 → An-1 → A2 → An-2 → … 
You must do this in-place without altering the nodes' values.



Problem Constraints
1 <= |A| <= 106



Input Format
The first and the only argument of input contains a pointer to the head of the linked list A.



Output Format
Return a pointer to the head of the modified linked list.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5] 
Input 2:

 A = [1, 2, 3, 4] 


Example Output
Output 1:

 [1, 5, 2, 4, 3] 
Output 2:

 [1, 4, 2, 3] 


Example Explanation
Explanation 1:

 The array will be arranged to [A0, An, A1, An-1, A2].
Explanation 2:

 The array will be arranged to [A0, An, A1, An-1, A2].

"""