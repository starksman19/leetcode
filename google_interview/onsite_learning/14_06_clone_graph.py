# Given a reference to a node in a connected undirected graph, return a deep copy of the graph.

from collections import deque
from typing import Dict, List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        pass


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
