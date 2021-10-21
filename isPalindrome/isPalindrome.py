"""
Given the head of a singly linked list, return true if it is a palindrome.
Example 1:
Input:  head = [1, 2, 2, 1]
Output: true

Example 2:
Input: head = [1, 2]
Output: false

Constraints:
- the number of nodes in the list is in the range [1, 10^5]
- 0 <= Node.val <= 9

Follow up: could you do it in O(n) time and O(1) space?
I: head of a linked list
O: boolean, whether it is a palindrome
C: The number of nodes in the list is in the range [1, 10^5]
E: 0 <= Node.val <= 9

Break down to sub problems
1: copy linked list to array list
2: compare array list and reverse of array list
3: return result

"""
# Definition for single-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool

    """
    if head is None:
        return True
    vals = []
    current_node = head
    while current_node:
        vals.append(current_node.val)
        current_node = current_node.next
    return vals == vals[::-1]


"""
time:  O(N) for copying linked list to array list
space: O(N) for array list
"""
