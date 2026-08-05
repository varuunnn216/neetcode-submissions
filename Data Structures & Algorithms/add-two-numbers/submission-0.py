# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur_tail = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            l1_digit = l1.val if l1 is not None else 0
            l2_digit = l2.val if l2 is not None else 0

            total = l1_digit + l2_digit + carry
            new_digit = total % 10
            carry = total // 10

            cur_tail.next = ListNode(new_digit)
            cur_tail = cur_tail.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        return dummy.next