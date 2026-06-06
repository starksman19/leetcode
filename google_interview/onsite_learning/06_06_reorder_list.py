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
    def reorderList_worse(self, head: Optional[ListNode]) -> None:
        node_log = []
        head_copy = head
        while head_copy:
            node_log.append(head_copy)
            head_copy = head_copy.next

        l, r = 0, len(node_log) - 1
        while l < r:
            node_log[l].next = node_log[r]
            l += 1

            node_log[r].next = node_log[l]
            r -= 1

        node_log[l].next = None
        return node_log[0]

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_part = slow.next
        slow.next = None

        prev = None
        temp = second_part
        while temp:
            next_ = temp.next
            temp.next = prev
            prev = temp
            temp = next_

        second_part = prev
        first_part = head

        while second_part:
            temp_part_1 = first_part.next
            temp_part_2 = second_part.next

            first_part.next = second_part
            first_part.next.next = temp_part_1

            first_part = temp_part_1
            second_part = temp_part_2
        return head


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
