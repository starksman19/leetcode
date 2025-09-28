class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        copy = head
        while copy:
            if copy in visited:
                return True
            visited.add(copy)
            copy = copy.next
        return False
