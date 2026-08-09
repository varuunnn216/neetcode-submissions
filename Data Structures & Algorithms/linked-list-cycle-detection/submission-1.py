# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_p = head
        slow_p = head

        while fast_p is not None and fast_p.next is not None:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                return True
        
        return False
        