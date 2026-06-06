# LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/
# Given the heads of two sorted linked lists, merge them into one sorted linked list and return its head.

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ret_list = ListNode()
        new_list_pointer = ret_list
        pointer1 = list1
        pointer2 = list2

        while pointer1 and pointer2:
            if pointer1.val < pointer2.val:
                new_list_pointer.next = pointer1
                pointer1 = pointer1.next
            else:
                new_list_pointer.next = pointer2
                pointer2 = pointer2.next
            new_list_pointer = new_list_pointer.next
        new_list_pointer.next = pointer1 or pointer2
        return ret_list.next


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


list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])

print(linked_list_to_list(Solution().mergeTwoLists(list1, list2)))
assert linked_list_to_list(
    Solution().mergeTwoLists(build_linked_list([1, 2, 4]), build_linked_list([1, 3, 4]))
) == [1, 1, 2, 3, 4, 4]

list1 = build_linked_list([])
list2 = build_linked_list([])

print(linked_list_to_list(Solution().mergeTwoLists(list1, list2)))
assert (
    linked_list_to_list(Solution().mergeTwoLists(build_linked_list([]), build_linked_list([])))
    == []
)
