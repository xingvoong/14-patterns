# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # deal with case of null 
        if not head:
            return head 
        
        if head.next:
            #point the next list node to the current list node 
            downstream = head.next
            
            # move on the the next list node
        else:
            return head
        
# init
- make a prev pointer that point to null
- make a cur pointer that point to head
- make a next pointer that point to head.next

#reverse pointer
cur.next = prev

# update cur and next references
prev = cur
cur = next
next = next.next

# to stop
if next is None:
    prev = cur
    cur = next

return head

def reverseList(head):
    if not head:
        return head
    
    prev = None
    cur = head
    next = head.next
    while next:
        cur.next = prev
        prev = cur
        cur = next
        next = next.next
    
    return cur

# 