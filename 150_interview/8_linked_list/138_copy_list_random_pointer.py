# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
#
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node.
# Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state.
# None of the pointers in the new list should point to nodes in the original list.
#
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
#
# Return the head of the copied linked list.
#
# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        pass


# AI generated examples

# Tworzenie węzłów
node0 = Node(7)
node1 = Node(13)
node2 = Node(11)
node3 = Node(10)
node4 = Node(1)

# next pointers
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

# random pointers
node0.random = None
node1.random = node0
node2.random = node4
node3.random = node2
node4.random = node0

head = node0

# Kopia
copied = Solution().copyRandomList(head)


# sprawdzamy wartości
assert copied.val == 7
assert copied.next.val == 13
assert copied.next.next.val == 11
assert copied.next.next.next.val == 10
assert copied.next.next.next.next.val == 1

# sprawdzamy random (czy wskazują poprawnie w nowej liście)
assert copied.random is None
assert copied.next.random == copied
assert copied.next.next.random == copied.next.next.next.next
assert copied.next.next.next.random == copied.next.next
assert copied.next.next.next.next.random == copied

# upewniamy się że to deep copy
assert copied is not head
assert copied.next is not node1


node0 = Node(1)
node1 = Node(2)

node0.next = node1

node0.random = node1
node1.random = node1

head = node0

copied = Solution().copyRandomList(head)

assert copied.val == 1
assert copied.next.val == 2

assert copied.random == copied.next
assert copied.next.random == copied.next

assert copied is not head
assert copied.next is not node1

node0 = Node(3)
node1 = Node(3)
node2 = Node(3)

node0.next = node1
node1.next = node2

node0.random = None
node1.random = node0
node2.random = None

head = node0

copied = Solution().copyRandomList(head)

assert copied.val == 3
assert copied.next.val == 3
assert copied.next.next.val == 3

assert copied.random is None
assert copied.next.random == copied
assert copied.next.next.random is None

assert copied is not head
assert copied.next is not node1
assert copied.next.next is not node2


node0 = Node(42)
node0.random = node0

head = node0

copied = Solution().copyRandomList(head)

assert copied.val == 42
assert copied.random == copied
assert copied is not head
