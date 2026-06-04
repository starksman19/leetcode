# LeetCode: https://leetcode.com/problems/reorder-list/
# Given the head of a singly linked list, reorder it from L0 -> L1 -> ... -> Ln
# into L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 ...
#
# Modify the list in-place.

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pass


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


head = build_linked_list([1, 2, 3, 4])

Solution().reorderList(head)
print(linked_list_to_list(head))
assert linked_list_to_list(head) == [1, 4, 2, 3]

head = build_linked_list([1, 2, 3, 4, 5])

Solution().reorderList(head)
print(linked_list_to_list(head))
assert linked_list_to_list(head) == [1, 5, 2, 4, 3]
