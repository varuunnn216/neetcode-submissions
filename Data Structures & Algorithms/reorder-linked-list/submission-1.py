# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_p = head
        fast_p = head

        while fast_p.next is not None and fast_p.next.next is not None:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        second_half_head = slow_p.next
        slow_p.next = None
        prev_node = None
        current_node = second_half_head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        second_half_head = prev_node

        first_half = head
        second_half = second_half_head

        while second_half is not None:
            first_temp = first_half.next
            second_temp = second_half.next

            first_half.next = second_half
            second_half.next = first_temp

            first_half = first_temp
            second_half = second_temp