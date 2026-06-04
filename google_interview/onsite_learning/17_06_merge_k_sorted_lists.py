# Given an array of k sorted linked-list heads, merge all lists into one sorted linked list and return its head.

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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


lists = [build_linked_list([1, 4, 5]), build_linked_list([1, 3, 4]), build_linked_list([2, 6])]

print(linked_list_to_list(Solution().mergeKLists(lists)))
assert linked_list_to_list(
    Solution().mergeKLists(
        [build_linked_list([1, 4, 5]), build_linked_list([1, 3, 4]), build_linked_list([2, 6])]
    )
) == [1, 1, 2, 3, 4, 4, 5, 6]

lists = []

print(linked_list_to_list(Solution().mergeKLists(lists)))
assert linked_list_to_list(Solution().mergeKLists([])) == []
