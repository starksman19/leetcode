# LeetCode: https://leetcode.com/problems/reverse-linked-list/
# Given the head of a singly linked list, reverse the list and return the new head.

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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


head = build_linked_list([1, 2, 3, 4, 5])

print(linked_list_to_list(Solution().reverseList(head)))
assert linked_list_to_list(Solution().reverseList(build_linked_list([1, 2, 3, 4, 5]))) == [
    5,
    4,
    3,
    2,
    1,
]

head = build_linked_list([1, 2])

print(linked_list_to_list(Solution().reverseList(head)))
assert linked_list_to_list(Solution().reverseList(build_linked_list([1, 2]))) == [2, 1]
