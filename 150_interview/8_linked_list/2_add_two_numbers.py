# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(node: ListNode, multiplayer, suma):
            if not node:
                return suma
            return traverse(node.next, multiplayer * 10, suma + (node.val * multiplayer))

        num1 = traverse(l1, 1, 0)
        num2 = traverse(l2, 1, 0)
        ret = num1 + num2
        ret_str = str(ret)
        root = ListNode(int(ret_str[-1]))
        prev = root
        for i in range(len(ret_str) - 2, -1, -1):
            prev.next = ListNode(int(ret_str[i]))
            prev = prev.next
        return root


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

# Expected output
expected = ListNode(7, ListNode(0, ListNode(8)))

print(Solution().addTwoNumbers(l1, l2))
assert Solution().addTwoNumbers(l1, l2) == expected
