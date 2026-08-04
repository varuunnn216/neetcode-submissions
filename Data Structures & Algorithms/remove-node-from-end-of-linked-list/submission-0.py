# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        front_p = dummy
        back_p = dummy

        for _ in range(n):
            front_p = front_p.next

        while front_p.next is not None:
            front_p = front_p.next
            back_p = back_p.next

        back_p.next = back_p.next.next

        return dummy.next