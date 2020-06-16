# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, root):
        intersect=None
        slow=root
        fast=root
        while(intersect==None):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                intersect=slow
        head=root
        while(head.next!=intersect.next):
            # print(head.val)
            head=head.next
            intersect=intersect.next
        intersect.next=None
        return root
            


"""
Remove Loop from Linked List
Problem Description

Given a linked list which contains some loop.

You need to find the node, which creates a loop, and break it by making the node point to NULL.



Problem Constraints
1 <= number of nodes <= 1000



Input Format
Only argument is the head of the linked list.



Output Format
return the head of the updated linked list.



Example Input
Input 1:

 
1 -> 2
^    |
| - - 
Input 2:

3 -> 2 -> 4 -> 5 -> 6
          ^         |
          |         |    
          - - - - - -


Example Output
Output 1:

 1 -> 2 -> NULL
Output 2:

 3 -> 2 -> 4 -> 5 -> 6 -> NULL


Example Explanation
Explanation 1:

 Chain of 1->2 is broken.
Explanation 2:

 Chain of 4->6 is broken.
"""