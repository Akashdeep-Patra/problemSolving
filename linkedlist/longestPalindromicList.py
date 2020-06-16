# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
def length(root):
    counter=0
    while(root!=None):
        counter+=1
        root=root.next
    return counter
def compare(root1,root2):
    counter=0
    while(root1!=None and root2!=None):
        if(root1.val!=root2.val):
            break
        root1=root1.next
        root2=root2.next
        counter+=1
    return counter
class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, root):
        l=length(root)
        counter=0
        current=root
        prev,next=None,None
        ans=0
        while(current!=None):
            next=current.next
            current.next=prev
            prev=current
            current=next
            ans=max(ans,compare(next,prev)*2,compare(next,prev.next)*2+1)
            counter+=1
        return ans
            
            




"""
Longest Palindromic List
Problem Description

Given a linked list of integers. Find and return the length of the longest palindrome list that exists in that linked list.

A palindrome list is a list that reads the same backward and forward.

Expected memory complexity : O(1)



Problem Constraints
1 <= length of the linked list <= 2000

1 <= Node value <= 100



Input Format
The only argument given is head pointer of the linked list.



Output Format
Return the length of the longest palindrome list.



Example Input
Input 1:

 2 -> 3 -> 3 -> 3
Input 2:

 2 -> 1 -> 2 -> 1 ->  2 -> 2 -> 1 -> 3 -> 2 -> 2


Example Output
Output 1:

 3
Output 2:

 5


Example Explanation
Explanation 1:

 3 -> 3 -> 3 is largest palindromic sublist
Explanation 2:

 2 -> 1 -> 2 -> 1 -> 2 is largest palindromic sublist.
"""