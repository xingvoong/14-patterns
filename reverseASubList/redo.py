'''
I: head = [1, 2, 3, 4, 5], left = 2, right = 4
O: [1, 4, 3, 2, 5]
C:

- need to move the pointer to the position of left and right
where the reverse process happen
+ to reverse a linked list:
- I need to have 3 pointers: prev, current, and next
- I need to do this with a while loop
- In the end, I need to change the pointer so that they return
the correct postion


'''

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

  # move the 2 pointers until they reach the proper starting point in the list
  cur, prev =  head, None
  while left > 1:
    prev = cur
    cur = cur.next
    left, right = left - 1, right - 1

  # the 2 pointers that will fix the final connections
  tail, con = cur, prev

  # iterrate reverse the nodes until n becomes 0:
  while right:
    third = cur.next
    cur.next = prev
    prev = cur
    cur = third
    right -= 1

  # adjust the final connections as explained in the algorithm
  if con:
    con.next = prev
  else:
    head = prev

  tail.next = cur
  return head
