# LeetCode: https://leetcode.com/problems/clone-graph/
# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
#
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
#
# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2,
# and so on. The graph is represented in the test case using an adjacency list.
#
# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
#
# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

from collections import deque
from typing import Dict, List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph_longer(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return
        visited = set()
        new_root = Node(val=node.val)
        node_map = {node: new_root}
        visited.add(node)
        que = [child for child in node.neighbors]

        while que:
            current = que.pop()
            if current in visited:
                continue
            visited.add(current)
            new_node = Node(val=current.val)
            node_map[current] = new_node
            for child in current.neighbors:
                que.append(child)

        que = [node]
        visited.clear()
        while que:
            current = que.pop()
            mapped_new = node_map[current]
            if current in visited:
                continue
            visited.add(current)
            for child in current.neighbors:
                que.append(child)
                mapped_new.neighbors.append(node_map[child])

        return new_root

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return
        node_map = {node: Node(val=node.val)}
        que = [node]

        while que:
            curr = que.pop()
            for neighbour in curr.neighbors:
                if neighbour not in node_map:
                    node_map[neighbour] = Node(val=neighbour.val)
                    que.append(neighbour)
                node_map[curr].neighbors.append(node_map[neighbour])
        return node_map[node]


def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
    if not adj_list:
        return None
    nodes = {index: Node(index) for index in range(1, len(adj_list) + 1)}
    for index, neighbors in enumerate(adj_list, start=1):
        nodes[index].neighbors = [nodes[value] for value in neighbors]
    return nodes[1]


def graph_to_adj(node: Optional[Node]) -> Dict[int, List[int]]:
    if not node:
        return {}
    result = {}
    seen = {node.val}
    queue = deque([node])
    while queue:
        current = queue.popleft()
        result[current.val] = sorted(neighbor.val for neighbor in current.neighbors)
        for neighbor in current.neighbors:
            if neighbor.val not in seen:
                seen.add(neighbor.val)
                queue.append(neighbor)
    return result


node = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
cloned = Solution().cloneGraph(node)

print(graph_to_adj(cloned))
assert cloned is not None
assert graph_to_adj(cloned) == {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
