'''
Given the head of a single linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list

Input: head = [1, 2, 3, 4, 5], left = 2, right = 4
Output: [1, 4, 3, 2, 5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
- The number of nodes in the list is n.
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n
'''
# Definition of single-linked list.
# class ListNode(object):
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

class solution(object):
  def reverseBetween(head, left, right):
    """
    :type head: ListNode
    :type left: int
    :type right: int
    :rtype: ListNode
    """