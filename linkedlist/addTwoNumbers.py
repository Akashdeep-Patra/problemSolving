# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None
import sys
sys.setrecursionlimit(10**7)
def add(a,b,carry):
    if(a==None and b==None):
        if(carry==1):
            return ListNode(1)
        return None
    if(a==None):
        temp=b.val+carry
        b.val=(temp)%10
        carry=(temp)//10
        b.next=add(a,b.next,carry)
        return b
    if(b==None):
        temp=a.val+carry
        a.val=(temp)%10
        carry=(temp)//10
        a.next=add(a.next,b,carry)
        return a
    temp=a.val+b.val+carry
    a.val=temp%10
    carry=temp//10
    a.next=add(a.next,b.next,carry)
    return a
class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def addTwoNumbers(self, a, b):
	    return add(a,b,0)



"""
Add Two Numbers as Lists
Problem Description

You are given two linked lists, A and B representing two non-negative numbers.

The digits are stored in reverse order and each of their nodes contain a single digit.

Add the two numbers and return it as a linked list.



Problem Constraints
1 <= |A|, |B| <= 105



Input Format
The first argument of input contains a pointer to the head of linked list A.

The second argument of input contains a pointer to the head of linked list B.



Output Format
Return a pointer to the head of the required linked list.



Example Input
Input 1:

 
 A = [2, 4, 3]
 B = [5, 6, 4]
Input 2:

 
 A = [9, 9]
 B = [1]


Example Output
Output 1:

 
 [7, 0, 8]
Output 2:

 
 [0, 0, 1]


Example Explanation
Explanation 1:

 A = 342 and B = 465. A + B = 807. 
Explanation 2:

 A = 99 and B = 1. A + B = 100. 
"""