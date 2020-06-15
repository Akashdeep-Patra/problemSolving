# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None
def delete(start,root,sec_node,k):
    if(root==None):
        return start.next
    if(k==0 and sec_node==None):
        sec_node=root
        return delete(start.next,root,sec_node.next,k)
    if(k==0 and sec_node.next==None):
        start.next=start.next.next
        return
    elif(k!=0):
        return delete(start,root.next,sec_node,k-1)
    return delete(start.next,root,sec_node.next,k)

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def removeNthFromEnd(self, root, k):
	   if(root==None or (root.next==None and k==1)):
	        return None
	   # ans=delete(root,root,None,k)
	   # return root if ans==None else ans
	   sec_node=root
	   top=root
	   while(sec_node.next!=None):
	       if(k!=0):
	           sec_node=sec_node.next
	           k-=1
	       else:
	           sec_node=sec_node.next
	           top=top.next
	   if(k!=0):
	       return root.next
	   top.next=top.next.next
	   return root
	           
	       

"""
Remove Nth Node from List End
Problem Description

Given a linked list A, remove the B-th node from the end of list and return its head.

For example, Given linked list: 1->2->3->4->5, and B = 2. After removing the second node from the end, the linked list becomes 1->2->3->5.

NOTE: If B is greater than the size of the list, remove the first node of the list.

NOTE: Try doing it using constant additional space.



Problem Constraints
1 <= |A| <= 106



Input Format
The first argument of input contains a pointer to the head of the linked list.

The second argument of input contains the integer B.



Output Format
Return the head of the linked list after deleting the B-th element from the end.



Example Input
Input 1:

A = [1, 2, 3, 4, 5]
B = 2
Input 2:

A = [1]
B = 1


Example Output
Output 1:

[1, 2, 3, 5]
Output 2:

 [] 


Example Explanation
Explanation 1:

In the first example, 4 is the second last element.
Explanation 2:

In the second example, 1 is the first and the last element.
"""