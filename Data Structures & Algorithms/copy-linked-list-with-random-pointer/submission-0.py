"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        old_to_new = {}

        current_node = head
        while current_node is not None:
            old_to_new[current_node] = Node(current_node.val)
            current_node = current_node.next

        current_node = head
        while current_node is not None:
            copied_node = old_to_new[current_node]

            copied_node.next = old_to_new[current_node.next] if current_node.next else None
            copied_node.random = old_to_new[current_node.random] if current_node.random else None

            current_node = current_node.next

        return old_to_new[head]