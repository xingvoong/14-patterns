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
'''
1: move the pointers until they reach the proper starting point in the list
2: Iteratively reverse the nodes until n becomes 0
3: Adjust the final connections as explained in the algorithm (the last few nodes)
'''

class solution(object):
  def reverseBetween(head, left, right):
    """
    :type head: ListNode
    :type left: int
    :type right: int
    :rtype: ListNode
    """

    # empty list
    if not head:
      return None

    # move the 2 pointers until they reach the proper starting point
    # in the list
    cur, prev = head, None
    while m > 1:
      prev = cur
      cur = cur.next
      m, n = m - 1, n - 1

    # the two pointers that will fix the final connections.
    tail, con = cur, prev

    # iteratively reverse the nodes until n becomes 0:



'''
I: head, left, right
head = [5], left = 1, right = 1

O:

C:

E:

'''