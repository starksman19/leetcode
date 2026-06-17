# LeetCode: https://leetcode.com/problems/merge-k-sorted-lists/
# Given an array of k sorted linked-list heads, merge all lists into one sorted linked list and return its head.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists_first_shot(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        root = ListNode(val=float("inf"))
        temp = root

        while temp:
            current_smallest = ListNode(val=float("inf"))
            found_idx = None
            for i in range(len(lists)):
                if lists[i] and lists[i].val <= current_smallest.val:
                    current_smallest = lists[i]
                    found_idx = i
            if found_idx is None:
                break
            if lists[found_idx]:
                lists[found_idx] = lists[found_idx].next
            temp.next = current_smallest
            temp = temp.next

        return root.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not lists[0]:
            return None
        root = ListNode()
        temp = root

        heap = []
        counter = 0
        for node in lists:
            heapq.heappush(heap, [node.val, counter, node])
            counter += 1

        while heap:
            _, counter, node = heapq.heappop(heap)
            temp.next = node
            temp = temp.next
            future_node = node.next
            if future_node:
                heapq.heappush(heap, [future_node.val, counter, future_node])
                counter += 1

        return root.next


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
