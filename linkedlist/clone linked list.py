"""
class ListNode: 
    def __init__(x):
        self.val = x
        self.next = None
        self.random = None
"""
def clonelist(root):
    head=root
    while(head!=None):
        temp=head.next
        head.next= ListNode(head.val)
        head.next.next=temp
        head=head.next.next
    head=root
    while(head!=None):
        head.next.random=head.random.next
        head=head.next.next
    root=root.next
    head=root
    while(head.next!=None):
        head.next=head.next.next
        head=head.next
    return root
    


"""
Clone a Linked List
Problem Description

Given a doubly linked list of integers with one pointer of each node pointing to the next node (just like in a single link list) while the second pointer, however, can point to any node in the list and not just the previous node.

You have to create a copy of this list and return the head pointer of the duplicated list.



Problem Constraints
1 <= length of the list <= 100000

1 <= Value of node <= 100000



Input Format
The only argument given is head pointer of the doubly linked list.



Output Format
Return the head pointer of the duplicated list.



Example Input
Input 1:

1 -> 2 -> 3 -> 4 -> 5
random pointer of each node 
1 -> 5 2 -> 4 3 -> 3 4 -> 2 5 -> 1
Input 2:

1 -> 2 -> 3 -> 4 -> 5
random pointer of each node 
1 -> 5 2 -> 4 3 -> 3 4 -> 2 5 -> 1


Example Output
Output 1:

1 -> 2 -> 3 -> 4 -> 5
random pointer of each node 
1 -> 5 2 -> 4 3 -> 3 4 -> 2 5 -> 1
Output 2:

1 -> 2 -> 3 -> 4 -> 5
random pointer of each node 
1 -> 5 2 -> 4 3 -> 3 4 -> 2 5 -> 1


Example Explanation
Explanation 1:

 Just clone the given list.
Explanation 2:

 Just clone the given list
"""