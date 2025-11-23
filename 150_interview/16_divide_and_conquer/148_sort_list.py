# Definition for singly-linked list.
# Given the head of a linked list, return the list after sorting it in ascending order.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge_lists(l: ListNode, r: ListNode):
            placeholder = ListNode(float("-inf"))
            return_node = placeholder
            while l and r:
                if l.val < r.val:
                    placeholder.next = l
                    l = l.next
                else:
                    placeholder.next = r
                    r = r.next
                placeholder = placeholder.next
            placeholder.next = l or r
            return return_node.next

        if not head or not head.next:
            return head

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)

        return merge_lists(left, right)


t1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
t2 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))

a = Solution().sortList(t1)
b = Solution().sortList(t2)
