"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continously following the next pointer.  Internally, pos is used to denote the index of the node that tail's next pointer is connected to.  Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list.  Otherwise, return false.
"""
# Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, x):
#       self.val = x
#       self.next = None
"""
I: head
O: boolean, true or false
C:
+ The number of the nodes in the list is in the range [0, 10^4]
+ -10^5 <= Node.val <= 10^5
+ pos is -1 or a valid index in the linked-list
+ can you solve it using O(1) (i.e constant) memory?

E: head is null

"""


def hasCycle(head):
    if head is None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


"""
Complexity Analysis:
space: O(1), only 2 pointers.
time: O(N), a while loop
"""
