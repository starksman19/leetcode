# LeetCode: https://leetcode.com/problems/linked-list-cycle/
# Given the head of a linked list, return true if the list contains a cycle.

from typing import List, Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional["ListNode"] = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass


def build_cycle_list(values: List[int], pos: int) -> Optional[ListNode]:
    if not values:
        return None
    nodes = [ListNode(value) for value in values]
    for index in range(len(nodes) - 1):
        nodes[index].next = nodes[index + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


head = build_cycle_list([3, 2, 0, -4], 1)

print(Solution().hasCycle(head))
assert Solution().hasCycle(head) == True

head = build_cycle_list([1, 2], -1)

print(Solution().hasCycle(head))
assert Solution().hasCycle(head) == False
